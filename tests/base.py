import os
import shutil

import django
from django.utils import unittest
from django.core.management import call_command
from django.conf import settings

# nose should not look for tests in this module
__test__ = False
__unittest = True


class TestCase(unittest.TestCase):

    locale = 'fr'

    def setUp(self):
        self.locale_dir = os.path.join(os.path.dirname(__file__), 'locale')
        try:
            os.mkdir(self.locale_dir)
        except OSError:
            pass
        settings.GETTEXT_EXTRA_KEYWORDS = ()

    def tearDown(self):
        shutil.rmtree(self.locale_dir)

    def set_setting(self, val):
        settings.GETTEXT_EXTRA_KEYWORDS = val

    def call_command(self, extra_kw=()):
        loc = self.locale
        if django.VERSION >= (1, 6):
            loc = [loc]
        call_command('makemessages', locale=loc, extra_keywords=extra_kw)

    @property
    def po_ctnt(self):
        ctnt = getattr(self, '_po_ctnt', None)
        if ctnt:
            return ctnt

        po_file = open(os.path.join(self.locale_dir, self.locale,
                                    'LC_MESSAGES', 'django.po'), 'r')
        self._po_ctnt = po_file.read()
        po_file.close()

        return self._po_ctnt

    def assertInPoFile(self, s, msg=None):
        self.assertTrue(s in self.po_ctnt, msg)

    def assertCountInPoFile(self, s, count, msg=None):
        self.assertEqual(self.po_ctnt.count(s), count, msg)
