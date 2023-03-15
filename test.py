import requests
import os
import pandas as pd
from tmdbapi import getmovie

apikey = os.getenv('MOVIEDB_API_KEY')


def main():
    print(getmovie(289))



'''
# implement to simplify code
def get_top_movies(response):
    topmovies = response.json()['results']
    columns = ['Rank', 'Movie', 'Revenue']
    df = pd.DataFrame(columns=columns)

    for i, movie in enumerate(topmovies):
        revenue = requests.get(f"https://api.themoviedb.org/3/movie/{(movie['id'])}?api_key={apikey}&language=en-US")
        revenue = revenue.json()
        df.loc[len(df)] = [i+1, movie['title'], revenue['revenue']]

    df.set_index('Rank', inplace=True)
    return df.head(10)

def gettopten(year):
    response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={apikey}&language=en-US&sort_by=revenue.desc&include_adult=false&include_video=false&page=1&primary_release_year={year}&vote_count.gte=500&vote_average.gte=7&with_watch_monetization_types=flatrate")
    if response.status_code == 200:
        return get_top_movies(response)
    else:
        print("Failed to retrieve data")

def gettoptengenre(year, genre_id):
    response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={apikey}&language=en-US&sort_by=revenue.desc&include_adult=false&include_video=false&page=1&primary_release_year={year}&with_genres={genre_id}&with_watch_monetization_types=flatrate")
    if response.status_code == 200:
        return get_top_movies(response)
    else:
        print("Failed to retrieve data")
'''        

if __name__ == "__main__":
    main()