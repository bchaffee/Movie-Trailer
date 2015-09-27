import webbrowser

class Movie():
	def __init__(self,movie_title, movie_storyline, trailer_youtube, poster_image):
		self.title = movie_title
		self.storyline = movie_storyline
		self.trailer_youtube_url = trailer_youtube
		self.poster_image_url = poster_image

	def show_trailer(self):
		webbrowser.open(self.trailer) 