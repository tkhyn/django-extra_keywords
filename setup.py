"""
Generic distutils script
(c) 2014 Thomas Khyn
MIT license (see LICENSE.txt)
"""

from distutils.core import setup
import os

INC_PACKAGES = 'django_extra_keywords',  # string or tuple of strings
EXC_PACKAGES = ()  # tuple of strings

install_requires = (
    'Django>=1.6',
)

# imports __version__ variable
exec(open('django_extra_keywords/version.py').read())

# setup function parameters
data = dict(
    name='django-extra_keywords',
    version=__version__,
    description='Extra gettext keywords handling in Django',
    author='Thomas Khyn',
    author_email='thomas@ksytek.com',
    url='http://open.ksytek.com/django/extra_keywords',  # TODO: check url
    keywords=['i18n', 'translation', 'gettext', 'keywords'],
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Environment :: Plugins',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic'
    ]
)


# packages parsing from root packages, without importing sub-packages
root_path = os.path.dirname(__file__)
if isinstance(INC_PACKAGES, basestring):
    INC_PACKAGES = (INC_PACKAGES,)

packages = []
excludes = list(EXC_PACKAGES)
for pkg in INC_PACKAGES:
    pkg_root = os.path.join(root_path, pkg)
    for dirpath, dirs, files in os.walk(pkg_root):
        rel_path = os.path.relpath(dirpath, pkg_root)
        pkg_name = pkg
        if (rel_path != '.'):
            pkg_name += '.' + rel_path.replace(os.sep, '.')
        for x in excludes:
            if x in pkg_name:
                continue
        if '__init__.py' in files:
            packages.append(pkg_name)
        elif dirs:  # stops package parsing if no __init__.py file
            excludes.append(pkg_name)


def read(filename):
    return open(os.path.join(root_path, filename)).read()

data.update({
    'packages': packages,
    'long_description': read('README.txt')  # use reST in  README.txt !
})

setup(**data)
