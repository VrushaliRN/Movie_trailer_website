import fresh_tomatoes
import media


"""This section is to provide the information for each movie
in the Movie Class which is in the Media Module."""

titanic = media.Movie(
                    "Titanic",
                    "A story of two lovers and famous ship",
                    "http://www.movieposter.com/posters/archive/main/"
                    "14/A70-7475",
                    "https://www.youtube.com/watch?v=tXbGHqiAmME")

aquaman = media.Movie("Aquaman", "A water superhero, protector of sea",
                      "http://www.movieposter.com/posters/archive/main/"
                      "247/MPW-123824",
                      "https://www.youtube.com/watch?v=WDkg3h8PCVU")


frozen = media.Movie("Frozen", "it is a heartfelt story of the"
                     "love between the two sisters set in the "
                     "premise of a magical ice kingdom",
                     "http://www.movieposter.com/posters/"
                     "archive/main/199/MPW-99705",
                     "https://www.youtube.com/watch?v=VqgZmrurLg0")


avengers = media.Movie("The Avengers", "story of superheroes come together"
                       " to protect the earth from evil powers",
                       "http://www.movieposter.com/posters/"
                       "archive/main/247/MPW-123738",
                       "https://www.youtube.com/watch?v=hA6hldpSTF8")


taken = media.Movie("Taken",
                    "story of a CIA agent and about his operations",
                    "http://www.movieposter.com/"
                    "posters/archive/main/154/MPW-77018",
                    "https://www.youtube.com/watch?v=3Tz9tQr1Zgo")


annabelle = media.Movie("Annabelle",
                        "annabelle is a dall with "
                        "evil spiritual powers inside it.",
                        "http://www.movieposter.com/"
                        "posters/archive/main/241/MPW-120696",
                        "https://www.youtube.com/watch?v=jdUysoK6tdQ")

"""import fresh_tomatoes" allows this"
" code to turn into a movie website by using "
"the function "open_movies_page"
The "open_movies_page" function takes a list of movies, then creates and opens
an html webpage or website that shows those (given) movies"""
movies = [titanic, aquaman, frozen, avengers, taken, annabelle]
fresh_tomatoes.open_movies_page(movies)

