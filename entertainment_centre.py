import fresh_tomatoes
import media


#This section is used to initialize the values in the Movie Class in the Media Module for each movie

titanic = media.Movie("Titanic",
                        "A story of two lovers and famous ship",
                        "http://www.movieposter.com/posters/archive/main/14/A70-7475",
                        "https://www.youtube.com/watch?v=tXbGHqiAmME")

                        
aquaman = media.Movie("Aquaman",
                     "A water superhero, protector of sea",
                     "http://www.movieposter.com/posters/archive/main/247/MPW-123824",
                     "https://www.youtube.com/watch?v=WDkg3h8PCVU") 


frozen = media.Movie("Frozen",
                    "it is a heartfelt story of the love  between the two sisters set in the premise of a magical ice kingdom",
                    "http://www.movieposter.com/posters/archive/main/199/MPW-99705",
                    "https://www.youtube.com/watch?v=VqgZmrurLg0")


avengers = media.Movie("The Avengers",
                     "it is a story where all superheroes come together to protect the earth from evil powers",
                     "http://www.movieposter.com/posters/archive/main/247/MPW-123738",
                     "https://www.youtube.com/watch?v=hA6hldpSTF8")


taken = media.Movie("Taken",
                    "a former CIA operative who sets about tracking down his teenage daughter Kim and her best friend Amanda after the two girls are kidnapped by Albanian sex traffickers while traveling in France during a vacation.",
                    "http://www.movieposter.com/posters/archive/main/154/MPW-77018",
                    "https://www.youtube.com/watch?v=3Tz9tQr1Zgo")


annabelle = media.Movie("Annabelle",
                        "annabelle is a dall with evil spiritual powers inside it.",
                        "http://www.movieposter.com/posters/archive/main/241/MPW-120696",
                        "https://www.youtube.com/watch?v=jdUysoK6tdQ")

                        

#"import fresh_tomatoes" allows to turn this code into a movie website by using function "open_movies_page"  
#The "open_movies_page" function takes a list or array of movies, then outputs or creates and opens
#an html webpage or website that shows those movies
movies = [titanic, aquaman, frozen, avengers, taken, annabelle]
fresh_tomatoes.open_movies_page(movies)
