""" Class definition for Movie."""


class Movie:
    """
    Movie class to be instantiated corresponding to individual movies.
    Only constructor/initializer is required hence ignoring pylint
    warning - 'Too few public methods'
    """

    def __init__(self, title, img_url, yt_trailer):
        self.title = title
        self.poster_image_url = img_url
        self.trailer_youtube_url = yt_trailer
