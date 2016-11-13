# Deep-Alt

![Image for demo](images/gif.gif)

Deep-Alt automizes the task of inserting description for alt attributes of img tags for web deveopers. Deep-alt uses Microsoft Computer Vision API's deep learning algorithms to caption images in an HTML file and returns a new HTML file in which alt attributes are filled out with their corresponding captions.


## Dependencies

- Microsoft Computer Vision API - v1.0
- BeautifulSoup
- Uploads.im API
- Python 2.7


## Install and Usage

### Get a Microsoft API Key for Free
[https://www.microsoft.com/cognitive-services/en-us/sign-up](https://www.microsoft.com/cognitive-services/en-us/sign-up "API Key").


### Download on Github

1. Go to the directory you wish to download the program
2. Open the terminal and enter `git clone https://github.com/ParhamP/deep-alt.git`
3. Now use the following command to receive the new HTML in your Desktop:
`python "path_to_deep-alt/src/main.py" "path_to_your_html" "api_key"`
4. A new HTML with alt attributes filled out is in your desktop. Enjoy!

### Or Install via NPM

1. `npm install -g deep-alt`
2. open terminal and enter: `python /usr/local/lib/node_modules/deep-alt/src/main.py "path_to_your_html" "api_key"`
3. A new HTML with alt attributes filled out is in your desktop. Enjoy!


## How It was Built

1. Parses the html using BeautifulSoup.
2. Find all the image tags
3. If the image's source is an internet URL, send a request to Microsoft's API to caption
4. If the image is local, stream it using uploads.im API, and then with its URL, send request to Microsoft's API to caption
5. Fill out the alt attributes for all the images
6. Write the edited HTML to the Desktop




## Captioned Images Samples


![Image for demo](images/piano.jpg)

A piano keyboard

![Image for demo](images/animal.jpg)

A squirrel eating

![Image for demo](images/cat.jpg)

A close up of a cat looking at the camera

![Image for demo](images/lady.jpg)

A woman wearing a red hat

![Image for demo](images/lake.jpg)

A small boat in a lake surrounded by mountains