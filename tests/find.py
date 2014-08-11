from .base import TestCase


class FindLazyTests(TestCase):

    def test_find_lazy(self):
        self.call_command(['_l'])
        self.assertInPoFile('msgid "This is a lazily translated string"')


class FindNGettextTests(TestCase):

    def test_find_ngettext(self):
        self.call_command(['_n:1,2'])

        self.assertInPoFile('msgid "This is a translated string using singular"')
        self.assertInPoFile('msgid_plural '
                            '"This is a translated string using plural"')
