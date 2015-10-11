__author__ = "Brandon Chaffee"
__date__ = "10/11/2015"

import webbrowser

class Movie():
        """...class Movie docstring...
        this class is used to initialized and show the trailer of each instance of the class Movie in the webbrowser
        """
	def __init__(self, movie_title, movie_storyline, trailer_youtube, poster_image):
                """...constructor docstring...
                the constructor creates instance variables for each of the parameters from the Movie class instances
                """
		self.title = movie_title
		self.storyline = movie_storyline
		self.trailer_youtube_url = trailer_youtube
		self.poster_image_url = poster_image

	def show_trailer(self):
                """...show_trailer docstring...
                show_trailer method takes in the trailer instance variable and opens the corresponding video in the web browser
                """ 
		webbrowser.open(self.trailer) 
