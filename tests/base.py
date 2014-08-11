import os
import shutil

from django.utils import unittest
from django.core.management import call_command

# nose should not look for tests in this module
__test__ = False
__unittest = True


class TestCase(unittest.TestCase):

    def setUp(self):
        self.locale_dir = os.path.join(os.path.dirname(__file__), 'locale')
        os.mkdir(self.locale_dir)

    def tearDown(self):
        shutil.rmtree(self.locale_dir)

    def call_command(self, extra_kw=()):
        call_command('makemessages', locale=['fr'], extra_keywords=extra_kw)

    @property
    def po_ctnt(self):
        ctnt = getattr(self, '_po_ctnt', None)
        if ctnt:
            return ctnt

        po_file = open(os.path.join(self.locale_dir, 'fr',
                                    'LC_MESSAGES', 'django.po'), 'r')
        self._po_ctnt = po_file.read()
        po_file.close()

        return self._po_ctnt

    def assertInPoFile(self, s, msg=None):
        self.assertTrue(s in self.po_ctnt, msg)

    def assertCountInPoFile(self, s, count, msg=None):
        self.assertEqual(self.po_ctnt.count(s), count, msg)
