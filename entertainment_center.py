import media
import fresh_tomatoes

# movie trailor list with individual trailors as tuples.
# add to the list below to add more trilors
movie_trailor_list = [
    ("Harry Potter and the Sorceror's Stone",
     "http://www.gstatic.com/tv/thumb/movieposters/28630/p28630_p_v8_at.jpg",
     "https://www.youtube.com/watch?v=fcPYNxGM7BA"),
    ("Harry Potter and the Chamber of Secrets",
     "http://t0.gstatic.com/images?q=tbn:ANd9GcTltzcooPkGcy1fKKqzSuO8U6S9XBpNDR9MuYc9SS_L5AbAn66O",
     "https://www.youtube.com/watch?v=q_V45YQ-EaA"),
    ("Harry Potter and the Prisoner of Azkaban",
     "http://www.gstatic.com/tv/thumb/movieposters/34483/p34483_p_v8_ap.jpg",
     "https://www.youtube.com/watch?v=1ZdlAg3j8nI"),
    ("Harry Potter and the Goblet fo Fire",
     "https://imgix.ranker.com/user_node_img/57/1133862/original/harry-potter-and-the-goblet-of-fire-films-photo-u6?w=650&q=50&fm=jpg&fit=fill&bg=fff",
     "https://www.youtube.com/watch?v=3EGojp4Hh6I"),
    ("Harry Potter an the Order of Phoenix",
     "https://vignette.wikia.nocookie.net/harrypotter/images/b/b9/OOTP_DVD.jpg/revision/latest?cb=20100705125254",
     "https://www.youtube.com/watch?v=y6ZW7KXaXYk"),
    ("Harry Potter and the Half Blood Prince",
     "http://www.gstatic.com/tv/thumb/movieposters/176377/p176377_p_v8_ak.jpg",
     "https://www.youtube.com/watch?v=sg81Lts5kYY"),
    ("Harry Potter and the Deathly Hallows – Part 1",
     "http://t3.gstatic.com/images?q=tbn:ANd9GcTobkzVSJU5oZ9Pv_6bM0_o4RF_zFA9jyNwdHATG90vKxyhOk5x",
     "https://www.youtube.com/watch?v=Su1LOpjvdZ4"),
    ("Harry Potter and the Deathly Hallows - Part 2",
     "http://t3.gstatic.com/images?q=tbn:ANd9GcTgXSuLAFerQGZdPCWv8EHI_ucQq6RTl3xf91F4aN54PDA_oCtB",
     "https://www.youtube.com/watch?v=Iv_Aym8gW2Q")
]

movie_list = []
for trailor in movie_trailor_list:
    movie_list.append(media.Movie(*trailor))
    print(movie_list)

fresh_tomatoes.open_movies_page(movie_list)
