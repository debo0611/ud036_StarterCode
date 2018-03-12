"""Module containing the main helper functions to create trailer website."""

import webbrowser
import os
import re


def read_template(file):
    """read a template file and return the content as string."""
    with open("templates/{}".format(file)) as outfile:
        return outfile.read()


MAIN_PAGE_HEAD = read_template("page_head.html")
MAIN_PAGE_CONTENT = read_template("page_content.html")
MOVIE_TILE_CONTENT = read_template("tile_content.html")


def create_movie_tiles_content(movies):
    """create movie tiles.

    create movie tiles content section by concatenating
    individual movie tiles
    """
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        print(movie.title)
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += MOVIE_TILE_CONTENT.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    """construct and open the movies html page on a browser."""
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = MAIN_PAGE_CONTENT.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(MAIN_PAGE_HEAD + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
