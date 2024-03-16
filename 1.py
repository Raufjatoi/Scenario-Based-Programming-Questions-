'''1. Movie Recommendation System:
Imagine you work for a streaming service that wants to personalize movie recommendations for its
users. Develop a program that:
 Asks the user for their age and favorite movie genre (e.g., comedy, action, drama).
 Based on the user's age and genre preference, recommends at least three specific movies from
the service's library using pre-defined data (including title, genre, and release year).
 If the user has no specific genre preference, recommend a mix of popular movies from different
genres '''

#importin random 
import random 
## taken the movie data from Gpt
movies = [
    {
        "name": "Inception",
        "age_recommendation": 14,
        "genre": ["Action", "Adventure", "Sci-Fi"],
        "year": 2010,
        "duration": 148,
        "imdb_rating": 8.8
    },
    {
        "name": "The Shawshank Redemption",
        "age_recommendation": 18,
        "genre": ["Drama"],
        "year": 1994,
        "duration": 142,
        "imdb_rating": 9.3
    },
    {
        "name": "Pulp Fiction",
        "age_recommendation": 18,
        "genre": ["Crime", "Drama"],
        "year": 1994,
        "duration": 154,
        "imdb_rating": 8.9
    },
    {
        "name": "The Dark Knight",
        "age_recommendation": 14,
        "genre": ["Action", "Crime", "Drama"],
        "year": 2008,
        "duration": 152,
        "imdb_rating": 9.0
    },
    {
        "name": "The Godfather",
        "age_recommendation": 18,
        "genre": ["Crime", "Drama"],
        "year": 1972,
        "duration": 175,
        "imdb_rating": 9.2
    },
    {
        "name": "Forrest Gump",
        "age_recommendation": 14,
        "genre": ["Drama", "Romance"],
        "year": 1994,
        "duration": 142,
        "imdb_rating": 8.8
    },
    {
        "name": "The Matrix",
        "age_recommendation": 18,
        "genre": ["Action", "Sci-Fi"],
        "year": 1999,
        "duration": 136,
        "imdb_rating": 8.7
    },
    {
        "name": "Interstellar",
        "age_recommendation": 14,
        "genre": ["Adventure", "Drama", "Sci-Fi"],
        "year": 2014,
        "duration": 169,
        "imdb_rating": 8.6
    },
    {
        "name": "The Silence of the Lambs",
        "age_recommendation": 18,
        "genre": ["Crime", "Drama", "Thriller"],
        "year": 1991,
        "duration": 118,
        "imdb_rating": 8.6
    },
    {
        "name": "The Lord of the Rings: The Return of the King",
        "age_recommendation": 14,
        "genre": ["Adventure", "Drama", "Fantasy"],
        "year": 2003,
        "duration": 201,
        "imdb_rating": 8.9
    },
    {
        "name": "Schindler's List",
        "age_recommendation": 18,
        "genre": ["Biography", "Drama", "History"],
        "year": 1993,
        "duration": 195,
        "imdb_rating": 8.9
    },
    {
        "name": "Gladiator",
        "age_recommendation": 18,
        "genre": ["Action", "Adventure", "Drama"],
        "year": 2000,
        "duration": 155,
        "imdb_rating": 8.5
    },
    {
        "name": "The Green Mile",
        "age_recommendation": 18,
        "genre": ["Crime", "Drama", "Fantasy"],
        "year": 1999,
        "duration": 189,
        "imdb_rating": 8.6
    },
    {
        "name": "Saving Private Ryan",
        "age_recommendation": 16,
        "genre": ["Drama", "War"],
        "year": 1998,
        "duration": 169,
        "imdb_rating": 8.6
    },
    {
        "name": "The Departed",
        "age_recommendation": 16,
        "genre": ["Crime", "Drama", "Thriller"],
        "year": 2006,
        "duration": 151,
        "imdb_rating": 8.5
    },
    {
        "name": "The Prestige",
        "age_recommendation": 14,
        "genre": ["Drama", "Mystery", "Sci-Fi"],
        "year": 2006,
        "duration": 130,
        "imdb_rating": 8.5
    },
    {
        "name": "The Usual Suspects",
        "age_recommendation": 18,
        "genre": ["Crime", "Mystery", "Thriller"],
        "year": 1995,
        "duration": 106,
        "imdb_rating": 8.5
    },
    {
        "name": "Fight Club",
        "age_recommendation": 18,
        "genre": ["Drama"],
        "year": 1999,
        "duration": 139,
        "imdb_rating": 8.8
    },
    {
        "name": "Goodfellas",
        "age_recommendation": 16,
        "genre": ["Biography", "Crime", "Drama"],
        "year": 1990,
        "duration": 146,
        "imdb_rating": 8.7
    },
    {
        "name": "The Sixth Sense",
        "age_recommendation": 16,
        "genre": ["Drama", "Mystery", "Thriller"],
        "year": 1999,
        "duration": 107,
        "imdb_rating": 8.1
    }
]

def view():
    for i in range (2):
     num_movies = len(movies)
     num_to_display = min(20, num_movies)
     random_movies = random.sample(movies, num_to_display)
     for movie in random_movies:
        print(f'Demo movie ::  no {i+1}' )
        print(f"Name: {movie['name']}")
        print(f"Age Recommendation: {movie['age_recommendation']}")
        print(f"Genre: {', '.join(movie['genre'])}")
        print(f"Year: {movie['year']}")
        print(f"Duration: {movie['duration']} minutes")
        print(f"IMDb Rating: {movie['imdb_rating']}")
        print()
        break

def view_top_3():
   e = 1
   print(f'Top 3 movies are :: ')
   for movie in movies:
        print(f"name : {movie['name']} , age : {movie['age_recommendation']} genra : {movie['genre']} , \n year : {movie['year']} , duration : {movie['duration']} rating : {movie['imdb_rating']}")
        if e == 3:
           break
        e += 1

def user_sug ():
   e = 1
   print('Suggestions : ')
   for movie in movies:
      if movie['age_recommendation'] == 18 :
        print((f"name : {movie['name']} , genra : {movie['genre']} , \n year : {movie['year']} , duration : {movie['duration']} rating : {movie['imdb_rating']}"))              
        if e == 3:
         break
        e += 1      
      elif movie["age_recommendation"] == 16 :
        print((f"name : {movie['name']} , genra : {movie['genre']} , \n year : {movie['year']} , duration : {movie['duration']} rating : {movie['imdb_rating']}"))              
        if e == 3:
         break
        e += 1
      elif movie["age_recommendation"] == 14 :
        print((f"name : {movie['name']} , genra : {movie['genre']} , \n year : {movie['year']} , duration : {movie['duration']} rating : {movie['imdb_rating']}"))
        if e == 3:
         break
        e += 1              
      else:
         pass
    
def main():
   while True:
      print('MOVIE RECOMMENDATION 🎬 : ')
      c = input('Enter S to suggest ya movie or V to view some : ').upper()
      if c == 'S':
         age = int(input('Enter ya age : '))
         genra = input('Enter ya genre : ')
         if age == 18 or 16 or 14:
            user_sug()
         else:
            view()
      elif c == 'V':
         view()
      else:
         print('Good bye 👋')
         break
if __name__ == '__main__':
   main()
        


         
      
