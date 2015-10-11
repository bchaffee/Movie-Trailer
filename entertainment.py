__author__ = "Brandon Chaffee"
__date__ = "10/11/2015"

# entertainment.py creates instances of media.Movie


import fresh_tomatoes
import media


#each of the following is an instance of media.Movie
interstellar = media.Movie(
    "Interstellar",
    "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
    "https://www.youtube.com/watch?v=0vxOhd4qlnA",
    "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SX640_SY720_.jpg")

forrest_gump = media.Movie(
    "Forrest Gump",
    "Forrest Gump, while not intelligent, has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him.",
    "https://www.youtube.com/watch?v=uPIEn0M8su0",
    "https://1001scribbles.files.wordpress.com/2012/04/forrest-gump-poster1.jpg")

finding_nemo = media.Movie(
    "Finding Nemo",
    "After his son is captured in the Great Barrier Reef and taken to Sydney, a timid clownfish sets out on a journey to bring him home.",
    "https://www.youtube.com/watch?v=wZdpNglLbt8",
    "http://img3.wikia.nocookie.net/__cb20150108180911/disney/images/8/89/Finding_Nemo_-_Poster.jpg")

spirited_away = media.Movie(
    "Spirited Away",
    "During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beasts.",
    "https://www.youtube.com/watch?v=ByXuk9QqQkk",
    "http://ia.media-imdb.com/images/M/MV5BMjYxMDcyMzIzNl5BMl5BanBnXkFtZTYwNDg2MDU3._V1_SX640_SY720_.jpg")

braveheart = media.Movie(
    "Braveheart",
    "When his secret bride is executed for assaulting an English soldier who tried to rape her, William Wallace begins a revolt and leads Scottish warriors against the cruel English tyrant who rules Scotland with an iron fist.",
    "https://www.youtube.com/watch?v=j53_WxqPZ7c",
    "https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg")
inception = media.Movie(
    "Inception",
    "A thief who steals corporate secrets through use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
    "https://www.youtube.com/watch?v=66TuSJo4dZM",
    "http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX640_SY720_.jpg")

# creates array of each Movie instance
movies = [
    interstellar,
    forrest_gump,
    finding_nemo,
    spirited_away,
    braveheart,
    inception]

fresh_tomatoes.open_movies_page(movies)
