# Install an external module and use it to perform an operation of your interest.
# installed pyttsx3 module for voice makiing or reading the text 
import pyttsx3

engine = pyttsx3.init()
engine.say("Hello, World!, This is my first module import program to read the text in voice.")
engine.runAndWait()

