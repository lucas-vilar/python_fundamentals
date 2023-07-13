# Intersection returns values that are in both set A and set B

# Creating a simple movie recommendation system
watched_movies = {'Spider-man' : ['Super-hero', 'Action', 'Marvel'], 'John Wick' : ['Action', 'Violence']}

all_movies = {'Finding nemo' : ['animation'], 'The avengers' : ['super-hero', 'Marvel', 'Action'], 'The Batman' : ['Super-hero', 'DC'], 'Saw' : ['Horror'], 'Pride and Prejudice' : ['Romance'], 'Jumanji' : ['Action']}

# Creating the intersection between the genres of both movies
movies_intesection = set(watched_movies['Spider-man']).intersection(set(watched_movies['John Wick']))

recommended_movies = []

for movie, genre in all_movies.items():
    # If the intersection between movies_intesection and current movie is not empty, the movie will be recommended
    if set(genre).intersection(movies_intesection) != set():
        recommended_movies.append(movie)

print(recommended_movies)
