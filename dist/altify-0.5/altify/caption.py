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

import httplib, urllib, base64, ast, json

def caption(image_src, api_key):
	"""
	It takes an image URL and an API key to send a request to Microsoft Computer Vision API
	and returns a caption(string) for the image. 

	Parameters
	----------
	image_src:		str
	api_key:		str
	                Microsoft's api_key

	Returns
	-------
	captioned_data:	str
	"""
	headers = {
		# Request headers
		'Content-Type': 'application/json',
		'Ocp-Apim-Subscription-Key': api_key,
	}

	params = urllib.urlencode({
		# Request parameters
		'maxCandidates': '1',
	})

    #data is the data that takes the image source. It is converted to str using a json method
	data = json.dumps({"Url": image_src}, separators=(',',':'))


	try:
		conn = httplib.HTTPSConnection('api.projectoxford.ai')
		conn.request("POST", "/vision/v1.0/describe?%s" % params, data, headers)
		response = conn.getresponse()
		data = ast.literal_eval(response.read())
		#captioned_data is a JSON that we need to navigate in order to get to the caption text.
		captioned_data = data['description']['captions'][0]["text"]
		return(captioned_data)
		conn.close()
	except Exception as e:
		print("")