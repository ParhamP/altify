from distutils.core import setup

setup(
  name = 'altify',
  packages=['altify'],
  version = '3.3',
  scripts=['altify/altify'],
  description = "Uses deep learning to caption img tags within a web page and fills out their alt attribute with the related caption",
  long_description="Altify automizes the task of inserting alternative text attributes for imgage tags. Altify uses Microsoft Computer Vision API's deep learning algorithms to caption images in an HTML file and returns a new HTML file in which alt attributes are filled out with their corresponding captions.",
  author = 'Parham Pourdavood',
  author_email = 'ppourdavood@gmail.com',
  url = 'https://github.com/parhamp/altify',
  download_url = 'https://github.com/parhamp/altify/tarball/0.1',
  keywords = ['alt', 'caption', 'images', 'deep learning'], # arbitrary keywords
  classifiers = [],
  install_requires = ['beautifulsoup4', 'html5lib'],
  license="Apache-2.0"
)
