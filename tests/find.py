from .base import TestCase


class FindLazyTests(TestCase):

    def test_find_lazy(self):
        self.call_command(['_l'])
        self.assertInPoFile('This is a lazily translated string')
