You can create sound from image files now. Imagine displaying an image from the forest with the actual forest sound in the background–Just adds to the drama. For this to run, have an image file and sound file (in .mp3 format) ready.

In this tutorial, we will learn how to use Optical Character Recognition (OCR) and Speech Synthesis, and then combine them into a single working program.

With one line of code, we can perform optical character recognition using the Python Library pytesseract.

Converting Generated Text to speech
In Python, you can convert speech to text in a variety of ways.
We will use Google Text to Speech to convert our decoded text into audio in this project.

gTTS(Google Text to Speech)
As the following example shows, doing text-to-speech with one line of code is very simple.

>>> from gtts import gTTS
>>> gTTS('Welcome To InterviewBit').save('interviewbit.mp3')