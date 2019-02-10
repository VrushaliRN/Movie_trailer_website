import webbrowser

class Movie:
    #This provides documentation about the class "Movie"
    """ This class movie related information """
      
    #Initializing and creating space in memory for what we are creating in this movie_website_trailer_project
    #"selfmade" is the object being created
    def __init__(selfmade, the_movie_title, movie_storyline, image_poster, youtube_trailer):
        selfmade.title = the_movie_title
        selfmade.storyline = movie_storyline
        selfmade.image_poster_url = image_poster
        selfmade.trailer_youtube_url = youtube_trailer

    #instance method is here:
    def show_trailer(selfmade):
        webbrowser.open(selfmade.youtube_url_trailer)
        
