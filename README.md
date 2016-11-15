# Altify

![Image for demo](images/gif.gif)

Altify automizes the task of inserting alternative text attributes for image tags. Altify uses Microsoft Computer Vision API's deep learning algorithms to caption images in an HTML file and returns a new HTML file in which alt attributes are filled out with their corresponding captions.

Notice: Altify will now ignore any image tag whose alt attribute has content or is just an empty string. (In compliance with standard web practices)

## Dependencies

- BeautifulSoup
- Python 2.7
- html5lib


## Install and Usage (Latest Version)

### 1) Get a Microsoft API Key for Free
[https://www.microsoft.com/cognitive-services/en-us/sign-up](https://www.microsoft.com/cognitive-services/en-us/sign-up "API Key").


### 2) Install via pip

Open up terminal and enter: `pip install altify`

### 3) Use

`altify path_to_your_html api_key`

### 4) Enjoy!

A new HTML file called altify.html is created next to the HTML file you selected. (Or Desktop, when using older versions)


## How It was Built

1. Parses the html using BeautifulSoup.
2. Find all the image tags.
3. Stream images using uploads.im API, and then with its URL, send request to Microsoft's API to caption.
4. Filter images that are smaller than 200px width.
4. Fill out the alt attributes for all the images.
5. Write an edited HTML file next to the file you selected.


## Captioned Images Samples


![Image for demo](images/pic.png)

Donald Trump wearing a suit and tie

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




## Disclaimer

Humans are currently better at captioning images than machines. Use responsibly!
