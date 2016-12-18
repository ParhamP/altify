from setuptools import setup

with open("README.rst", "rb") as f:
    long_description = f.read()

setup(
  name = 'altify',
  packages=['altify'],
  version = '3.9',
  scripts=['altify/altify'],
  description = "Uses deep learning to caption img tags within a web page and fills out their alt attribute with the related caption",
  long_description=long_description,
  author = 'Parham Pourdavood',
  author_email = 'ppourdavood@gmail.com',
  url = 'https://github.com/parhamp/altify',
  download_url = 'https://github.com/parhamp/altify/tarball/3.3',
  keywords = ['alt', 'caption', 'images', 'deep learning'], # arbitrary keywords
  classifiers = [],
  install_requires = ['beautifulsoup4', 'html5lib'],
  license="Apache-2.0"
)
