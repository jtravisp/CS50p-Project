import requests
import os
import pandas as pd

apikey = os.getenv('MOVIEDB_API_KEY')


def main():
    print(gettopten(2022))


def gettoptengenre(year, genre_id):
    response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={apikey}&language=en-US&sort_by=revenue.desc&include_adult=false&include_video=false&page=1&primary_release_year={year}&with_genres={genre_id}&with_watch_monetization_types=flatrate")
    if response.status_code == 200:
        topmovies = response.json()['results']
        columns = ['rank', 'movie', 'revenue']
        df = pd.DataFrame(columns=columns)

        for i, movie in enumerate(topmovies):
            revenue = requests.get(f"https://api.themoviedb.org/3/movie/{(movie['id'])}?api_key={apikey}&language=en-US")
            revenue = revenue.json()
            df.loc[len(df)] = [i+1, movie['title'], revenue['revenue']]

        df.set_index('rank', inplace=True)  # Set rank as the index
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]  # Drop the unnamed 0-index column
        return df.head(10)

if __name__ == "__main__":
    main()