"""Class definition for Movie."""


class Movie:
    """Movie class to be instantiated corresponding to individual movies.

    Note:
        Only constructor/initializer is required hence ignoring pylint
        warning - 'Too few public methods'

    Attributes:
        title (str): Movie title name
        poster_image_url (str): Url for the image of the movie
        trailer_youtube_trailer (str): Youtube url for the trailer of the movie
    """

    def __init__(self, title, img_url, yt_trailer):
        """Initializer for Movie class.

        Args:
            title (str): Movie title name
            image_url (str): Url for the image of the movie
            yt_trailer (str): Youtube url for the trailer of the movie
        """
        self.title = title
        self.poster_image_url = img_url
        self.trailer_youtube_url = yt_trailer
