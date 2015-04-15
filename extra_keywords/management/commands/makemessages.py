"""
There were 2 options to add arguments to xgettext
1. add arguments to the list built in process function, this would require
   copying the function and adding 3 lines to it ...
2. add arguments afterwards, when _popen / popen_wrapper is called, by
   monkey-patching the _popen / popen_wrapper function

Given the size of this file, you have probably guessed that it's the
2nd solution that is used here

(c) 2014 Thomas Khyn
MIT license (see LICENSE.txt)
"""

from optparse import make_option

import django
from django.core.management.commands import makemessages as makemessages_core
from django.core.management.base import CommandError
from django.conf import settings

try:
    # django >= 1.6
    from django.core.management.utils \
    import popen_wrapper as popen_wrapper_core
    _popen_core = None
except ImportError:
    # django < 1.6
    from django.core.management.commands.makemessages \
    import _popen as _popen_core
    popen_wrapper_core = None


def _process_args(args, extra_keywords):
    if args and args[0] == 'xgettext':
        for i, a in enumerate(args):
            if '--keyword=' in a:
                to_ins = ['--keyword=%s' % kw for kw in extra_keywords]
                args[i:i] = to_ins
                break
    return args


_arg_kwargs = dict(
    dest='extra_keywords',
    action='append', nargs='+', type=int,
    help='If you use import aliases for ugettext and its variations, you can '
         'specify them here to make sure that xgettext will find your '
         'translatable strings.'
)


class Command(makemessages_core.Command):

    if django.VERSION >= (1, 8):
        def add_arguments(self, parser):
            super(Command, self).add_arguments(parser)
            parser.add_argument('--extra-keywords', **_arg_kwargs)
    else:
        option_list = makemessages_core.Command.option_list + (
            make_option('--extra-keyword', **_arg_kwargs),)

    def handle(self, *args, **options):

        extra_keywords = set(options.pop('extra_keywords'))
        extra_keywords.update(getattr(settings, 'GETTEXT_EXTRA_KEYWORDS', ()))

        if popen_wrapper_core:
            # django >= 1.6
            def popen_wrapper_xtra_kw(args, os_err_exc_type=CommandError):
                return popen_wrapper_core(_process_args(args, extra_keywords),
                                          os_err_exc_type)
            makemessages_core.popen_wrapper = popen_wrapper_xtra_kw
        else:
            # django < 1.6
            def _popen_xtra_kw(cmd):
                return _popen_core(' '.join(_process_args(cmd.split(' '),
                                                          extra_keywords)))
            makemessages_core._popen = _popen_xtra_kw

        try:
            try:
                # django < 1.8
                super(Command, self).handle_noargs(**options)
            except AttributeError:
                super(Command, self).handle(**options)
        finally:
            # restore popen_wrapper or _popen
            if popen_wrapper_core:
                # django >= 1.6
                makemessages_core.popen_wrapper = popen_wrapper_core
            else:
                # django < 1.6
                makemessages_core._popen = _popen_core

    def handle_noargs(self, **options):
        # for django < 1.8
        return self.handle(**options)
