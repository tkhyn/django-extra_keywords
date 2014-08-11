Extra keywords for Django
=========================

|copyright| 2014 Thomas Khyn

Tested with Django 1.4 to 1.7 and all supported versions of Python.

About
-----

The django ``makemessage`` management command parses the code of an application
to generate .pot and .po files, provided the strings to be translated are
called by the gettext-like functions (gettext, ugettext, ngettext,
ugettext_lazy, etc.) or the ``_`` alias.

However, it is quite common to use other aliases than ``_``, for example for
lazy translation, where ``_l`` can be used.

Before version 1.7, Django does not provide a way to specify other aliases
that may be used for translation strings. This plugin fills this gap, without
having to patch the django code itself.

From version 1.7, it is possible to use the ``xgettext_options`` in a custom
``makemessages`` command. Using this app saves you the hassle of programming
a custom command.


Installation
------------

As straightforward as it can be, using ``pip``::

   pip install django-extra_keywords


Usage
-----

Simply add ``'extra_keywords'`` to your ``INSTALLED_APPS``. Note that it does
not make any sense to have this application installed in production and that it
may only used in a development settings module.

Then, you can:

- either define ``GETTEXT_EXTRA_KEYWORDS`` in your ``settings`` module as a
  tuple or list containing the keywords you would like to add::

   GETTEXT_EXTRA_KEYWORDS = ('_l', '_n:1,2')

- or use it from the command line, using the ``--extra-keyword`` option (with
  no s, to add several keywords you have to repeat the option)::

   manage.py makemessages [...] --extra-keyword=_l [...]


Keyword format
--------------

When using aliases for one-argument functions (``ugettext``, ``ugettext_lazy``
...), simply use the alias as a keyword. When using aliases for several
arguments functions, you need to specify them, according to the following
table:

.. table::

   =============  ==============
   Function type  Keyword format
   =============  ==============
   gettext\*      X
   ngettext\*     X:1,2
   pgettext\*     X:1c,2
   npgettext\*    X:1c,2,3
   =============  ==============

Example: if ``_n`` is an alias for ``ungettext``, the keyword to use in
``GETTEXT_EXTRA_KEYWORDS`` or the ``makemessages`` command is ``'_n:1,2'``.


.. |copyright| unicode:: 0xA9
