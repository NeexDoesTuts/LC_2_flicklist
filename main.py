from flask import Flask
import random

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"

    tomorrows_movie = get_random_movie()
    
    while movie == tomorrows_movie:
        tomorrows_movie = get_random_movie()

    content += "<h2>Tomorrow's movie</h2>"
    content += "<ul><li>" + tomorrows_movie + "</li></ul>"

    return content

def get_random_movie():
    # used https://www.randomlists.com/random-movies to 
    # generate a list of random movies
    movie_database = ["X-Men: Apocalypse", 
                        "Fifty Shades Darker", 
                        "Harry Potter and the Philosopher's Stone", 
                        "Ratatouille", 
                        "Miss Peregrine's Home for Peculiar Children", 
                        "The Space Between Us",
                        "Baby Driver", 
                        "The Autopsy of Jane Doe", 
                        "The Amazing Spider-Man", 
                        "Thor: The Dark World", 
                        "Tomorrow Everything Starts", 
                        "Straight Outta Compton", 
                        "Gone Girl", 
                        "Underworld: Blood Wars"]
    
    random_movie = random.choice(movie_database)
    return random_movie

app.run()
