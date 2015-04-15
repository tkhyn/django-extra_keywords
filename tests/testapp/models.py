from django.utils.translation import ugettext_lazy as _l, \
                                     ungettext_lazy as _n

test_string = _l('This is a lazily translated string')

n = 1
test_nstring = _n('This is a translated string using singular',
                  'This is a translated string using plural', n)
