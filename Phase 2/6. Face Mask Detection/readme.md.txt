With the current pandemic times, a face mask is highly appreciated wherever we go. But it also becomes tiresome to manually detect people without a mask. This Python Project lets you detect a mask and prompt any error. This can be applied in malls or any public meeting place. 

What we will be doing in this project:

 Using Python, Keras, and OpenCV, we will develop a deep-learning model for face mask detection. 
We will develop a face mask detector model to detect whether a person is wearing a mask or not. 
Keras-based network architecture is used to train the model. 
First, the model is trained, and then the OpenCV program is used to test the model using a webcam.
Introduction to Image Processing

We need to understand how to handle images before implementing the face mask detection problem. An image is simply a collection of colors in red, green, and blue. As humans, we see images with objects and shapes in them, but a computer sees them as color arrays with values ranging from 0 to 255.

Computers perceive images differently from humans. But that’s the good news for us because if we get an array of the image, then it becomes a lot easier to implement any algorithm on the array.

Steps to Perform Image Processing :

Use Python or any other programming language you are using to load images.
Convert the images into an array.
And finally, apply some algorithms.
It is also good that we have a library called OpenCV that will allow us to read the image and return an array of colour pixels.