# ud036_StarterCode
Source code for a Movie Trailer website.

# Installation
First, clone the project
`git clone https://github.com/debo0611/ud036_StarterCode.git`

Next, the only requirement is that you have python3 installed. Ensure you have python3 installed at system level or you are working on a python3 virtual environment.

# Running the script
From the terminal, just run the below

`python entertainment_center.py`

# Common issue
Ensure python points to python3 or use python3 to invoke the script

# Adding a new movie trailer to be displayed on the web browser
open the entertainment.py file and add an entry to the variable *MOVIE_TRAILER_LIST*
list. The entry should be in the form of a tuple with the below format --
**(*name_of_the_movie*, *movie_image_location*, *youtube_url_for_the_trailer*)**

Similarly, you can remove/modify an existing element in the list.
