from distutils.core import setup

setup(
  name = 'altify',
  packages=['altify'],
  version = '2.4',
  scripts=['altify/altify.py'],
  description = "Uses deep learning to caption img tags within a web page and fills out their alt attribute with the related caption",
  author = 'Parham Pourdavood',
  author_email = 'ppourdavood@gmail.com',
  url = 'https://github.com/parhamp/altify',
  download_url = 'https://github.com/parhamp/altify/tarball/0.1',
  keywords = ['alt', 'caption', 'images'], # arbitrary keywords
  classifiers = [],
  install_requires = ['beautifulsoup4', 'html5lib']
)
