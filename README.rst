Altify
======

.. image:: https://github.com/ParhamP/altify/blob/master/images/gif.gif?raw=true

Altify automizes the task of inserting alternative text attributes for
image tags. Altify uses Microsoft Computer Vision API's deep learning
algorithms to caption images in an HTML file and returns a new HTML file
in which alt attributes are filled out with their corresponding
captions.

Notice: Altify will now ignore any image tag whose alt attribute has
content or is just an empty string. (In compliance with standard web
practices)

Dependencies
------------

-  Python 2.7
-  BeautifulSoup

Install and Use
---------------

1) Get a Microsoft API Key for Free
+++++++++++++++++++++++++++++++++++

https://www.microsoft.com/cognitive-services/en-us/sign-up.

2) Install via pip
++++++++++++++++++

Open up terminal and enter: ``pip install altify``

3) Use
++++++

``altify path_to_your_html api_key``

4) Enjoy!
+++++++++

A new HTML file called altify.html is created next to the HTML file you
selected.


Captioned Images Samples
------------------------

.. image:: https://github.com/ParhamP/altify/blob/master/images/pic.png?raw=true

Donald Trump wearing a suit and tie

.. image:: https://github.com/ParhamP/altify/blob/master/images/piano.jpg?raw=true

A piano keyboard

.. image:: https://github.com/ParhamP/altify/blob/master/images/animal.jpg?raw=true

A squirrel eating

.. image:: https://github.com/ParhamP/altify/blob/master/images/cat.jpg?raw=true

A close up of a cat looking at the camera

.. image:: https://github.com/ParhamP/altify/blob/master/images/lady.jpg?raw=true

A woman wearing a red hat

.. image:: https://github.com/ParhamP/altify/blob/master/images/lake.jpg?raw=true

A small boat in a lake surrounded by mountains

Author
------
Parham Pourdavood

Disclaimer
----------

Humans are currently better at captioning images than machines. Use
responsibly!
