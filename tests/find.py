from .base import TestCase


class FindLazyTests(TestCase):

    def assert_pass(self):
        self.assertInPoFile('msgid "This is a lazily translated string"')

    def test_find_lazy(self):
        self.call_command(['_l'])
        self.assert_pass()

    def test_find_lazy_setting(self):
        self.set_setting(['_l'])
        self.call_command()
        self.assert_pass()


class FindNGettextTests(TestCase):

    def assert_pass(self):
        self.assertInPoFile('msgid "This is a translated string using singular"')
        self.assertInPoFile('msgid_plural '
                            '"This is a translated string using plural"')

    def test_find_ngettext(self):
        self.call_command(['_n:1,2'])
        self.assert_pass()

    def test_find_ngettext_setting(self):
        self.set_setting(['_n:1,2'])
        self.call_command()
        self.assert_pass()
