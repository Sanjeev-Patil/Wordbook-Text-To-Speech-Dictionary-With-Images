# Wordbook-Text-To-Speech-Dictionary-With-Images

# METHODOLOGY
# ALGORITHMIC DETAILS
Algorithm (For Wordbook):
Step1: Initialize the modules required ‘from tkinter import *’ to create the GUI window.
       ‘from tkinter import messagebox’ to display message box.
       ‘import json’ to access the words and their meanings.
       ‘import pyttsx3’ to convert text to speech. 
       ‘from difflib import get_close_matches’ to compare sets of data and return the best set of values.
       ‘from PIL import ImageTk, Image’ to load images from user system to tkinter window’.
       ‘import os, sys’ to interact with the operating system. 
Step2: Create instance of ‘engine’ class to convert text to speech. 
Step 3: Define a function ‘wordaudio()’ to convert the input word from user to audio. 
Step 4: Define a function ‘meaningaudio()’ to convert the displayed meaning to audio. 
Step 5: Define a function ‘iexit()’ to exit the window, containing message box. 
Step 6: Define a function ‘clear()’ to delete everything on the window. 
Step 7: Define a function ‘search()’ to load data from ‘data.json’ file and fetch the word using object ‘enterwordentry.get()’,using a loop compare the entered word           with word present in json file and convert the entered word into lower case using method ‘word.lower().'
Step 8: Define a function ‘imgdisplay()’ to display the word and image related to searched word by accessing the folder of images stored on the user’s system. 
Step 9: Create an object ‘root’ and ‘Tk()’ class and main method ‘root.mainloop()’ present inside ‘Tk()’ class containing different methods to set the dimension,               title, background and all the buttons for creating wordbook GUI window. 

# Algorithm (For web scraping):

Step 1: Initialize the modules required ‘import json’ to access the words and their meanings.
        ‘from selenium import webdriver’ to automate web browser interaction from Python through web driver.
        ‘from bs4 import BeautifulSoup’ to scrape information from web pages.
        ‘import requests’ to send HTTP/1.1 requests extremely easily.
        ‘import urllib.request’ to open the specified URL.
        ‘import os, sys’ to interact with the operating system. 
Step 2: To read json file use method ‘json.load()’. Step 3: Provide driver path ‘webdriver.Chrome()’ to link selenium to web browser, use ‘minimize_window method()’ to         minimize the window that webdriver is using and ‘driver.execute_script()’ method synchronously executes JavaScript in the current window. 
Step 4: Define function ‘idownload()’ to search images on Google chrome and download the images related to words present in json file.

This project implemented interactive way of finding the meanings of word in comparison to printed dictionaries using python programming.

![image](https://user-images.githubusercontent.com/91845572/226107633-3e5b0a79-5e6c-4389-a7fd-69064b54a9d5.png)

Application Interface

This figure shows general interface of the application.
A search bar is present where words can be entered, below it there is a search button to initiate word search and a mic button for text-to-speech of the searched word.
Meanings are shown on the blank space below the search bar and there is also another mic button to read the meaning along with clear button ‘X’ which is used to clear the interface after searching the word.
To close the application click the 'Exit' button.

![image](https://user-images.githubusercontent.com/91845572/226107911-4e4425fb-155e-4fd0-b4a3-fc360ebff61f.png)

Searching Word

After entering a word on the search bar and clicking the search button the meaning and the image for the word will be shown. 
The image will be displayed on the left.
On the above figure word ‘grass’ is searched and the image related to the grass is shown with meaning on the blank space below the search bar.


![image](https://user-images.githubusercontent.com/91845572/226108045-b3733eae-2c53-47fe-9f1c-ef3d1e610778.png)

Entering Incorrect Word

When incorrect word is entered, Wordbook will suggest a correct word for it.
A dialog box will appear asking the user to search the suggested word.
In the above figure an incorrect word is searched and Wordbook is suggesting correct word for is searched and Wordbook is suggesting correct
word for it.

![image](https://user-images.githubusercontent.com/91845572/226112936-42e7bffe-ef38-4615-9767-a1b0de62cf6b.png)

Word Suggested By The Application

After clicking the yes button on the dialog box suggesting the correct word, Wordbook will automatically search the word and display its meaning along with the image related to the word.

