# Copyright 2016 Parham Pourdavood

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from bs4 import BeautifulSoup
from caption import caption
from upload import upload
import urlparse



def is_url(url):
	"""
	check to see if the address is a URL or a local path

	parameters
	----------
	url:		str

	returns
	-------
	True or False:		Bool
	"""
    return urlparse.urlparse(url).scheme != ""



def apply(html_file, api_key):

	'''
	it takes an html file and creates a new html file in which all the alt attribute of img tags
	are filled out with their related caption. (made by caption function in caption module)

	parameters
	----------
	html_file:		HTML
	api_key:		str
	                Microsoft's api_key
	'''

	with open(html_file) as f:
		html_data = f.read()

	#Using a third party library called beautifulSoup for parse and manipulate HTML DOM
	parsed_html = BeautifulSoup(html_data, 'html.parser')

	#assign all the image tags to img_tages
	img_tags = parsed_html.find_all('img')

	#goes over each img tag and see if its alt attribute has a value. If it doesn't,
	#it will fill out the alt with the corresponding caption for the image.
	for each_image in img_tags:
		value = each_image.get("alt")
		if value == None or value == "":
			each_image["alt"] = caption(each_image["src"], api_key)
	output_file = open("newAlt.html", 'a')
	output_file.write(parsed_html.prettify())
