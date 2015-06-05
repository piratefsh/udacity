class Movie:
    """
    Attributes:
        title (str): movie title
        trailer_youtube_url (str): youtube url of movie trailer
        poster_image_url (str): image url of movie poster
    """
    def __init__(self, trailer_youtube_url, title, poster_image_url):
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
