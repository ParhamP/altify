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

import json
import requests

def upload(image_address):
	"""
	It uses uploads.im api to stream the images that are local.

	parameters
	----------
	image_address:		str
                        the local address of the image(e.g, 'images/photo.jpg')

    returns
    -------
    main_url:			str
                        the url of new uploaded image
	"""

	# A post request to uploads.im API to get the url of the uploaded image
	url = "http://uploads.im/api"
	files = {'media': open(image_address, 'rb')}
	request = requests.post(url, files=files)
	data = json.loads(request.text)
	image_url = data[u'data'][u'img_url']
	main_url = image_url.encode('ascii','ignore')
	return(main_url)