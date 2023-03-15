import requests
import os
import pandas as pd


apikey = os.getenv('MOVIEDB_API_KEY')

# Implement:
    # Get number of times an actor appears in a year
   # Get top 10 rated by year
    # Plot top 10 in a year 

def main(): # for testing purposes
    title = input("Movie Title: ")
    movie_id = getid(title)
    print(movie_id)

  
def getid(title):
    # Get movie id from movie title
    response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={apikey}&language=en-US&query={title}&page=1&include_adult=false")
    if response.status_code == 200:
        o = response.json()
        return o['results'][0]['id']
    else:
        print("Failed to retrieve data")


def getmovie(movie_id):
    # Get movie title from movie ID
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={apikey}&language=en-US")
    if response.status_code == 200:
        o = response.json()
        return o['original_title']
    else:
        print("Failed to retrieve data")

def gettopten(year):
    response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={apikey}&language=en-US&sort_by=revenue.desc&include_adult=false&include_video=false&page=1&primary_release_year={year}&vote_count.gte=500&vote_average.gte=7&with_watch_monetization_types=flatrate")
    if response.status_code == 200:
        topmovies = response.json()['results']
        columns = ['Rank', 'Movie', 'Revenue']
        df = pd.DataFrame(columns=columns)

        for i, movie in enumerate(topmovies):
            revenue = requests.get(f"https://api.themoviedb.org/3/movie/{(movie['id'])}?api_key={apikey}&language=en-US")
            revenue = revenue.json()
            df.loc[len(df)] = [i+1, movie['title'], revenue['revenue']]

        df.set_index('Rank', inplace=True)
        return df.head(10)
    
    else:
        print("Failed to retrieve data")

def gettoptengenre(year, genre_id):
    response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={apikey}&language=en-US&sort_by=revenue.desc&include_adult=false&include_video=false&page=1&primary_release_year={year}&with_genres={genre_id}&with_watch_monetization_types=flatrate")
    if response.status_code == 200:
        topmovies = response.json()['results']
        columns = ['Rank', 'Movie', 'Revenue']
        df = pd.DataFrame(columns=columns)

        for i, movie in enumerate(topmovies):
            revenue = requests.get(f"https://api.themoviedb.org/3/movie/{(movie['id'])}?api_key={apikey}&language=en-US")
            revenue = revenue.json()
            df.loc[len(df)] = [i+1, movie['title'], revenue['revenue']]

        df.set_index('Rank', inplace=True)
        return df.head(10)
    
    else:
        print("Failed to retrieve data")


if __name__ == "__main__":
    main()