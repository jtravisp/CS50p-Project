import pandas as pd
import sys
import requests
import os

# from tmdbapi import gettopten, gettoptengenre
# import matplotlib.pyplot as plt

apikey = os.getenv('MOVIEDB_API_KEY')


GENRE_IDS = {
    "Action": 28,
    "Adventure": 12,
    "Animation": 16,
    "Comedy": 35,
    "Crime": 80,
    "Documentary": 99,
    "Drama": 18,
    "Family": 10751,
    "Fantasy": 14,
    "History": 36,
    "Horror": 27,
    "Music": 10402,
    "Mystery": 9648,
    "Romance": 10749,
    "Science Fiction": 878,
    "TV Movie": 10770,
    "Thriller": 53,
    "War": 10752,
    "Western": 37
}

def main():
    menu()


def menu():
    print("<<<<<<<<<<Python Movie Database (PMDB)>>>>>>>>>>")
    _ = input("""                
                1: Get Top 10 Movies by Revenue in a Year (all genres)
                2: Get Top 10 Movies by Revenue in a Year by Genre
                3: Exit

              Please enter your choice: """)

    if _ == "1":
        year = int(input("Year: "))
        df = gettopten(year)
        print(df)

    elif _ == "2":
        year = int(input("Year: "))
        print("Select a genre: ")              
        for _, genre in enumerate(GENRE_IDS.keys(), start=1):
            print(f"{_}: {genre}")
        choice = int(input("Enter your choice: "))
        # look up the genre ID based on the user's choice
        genres = list(GENRE_IDS.values())
        if choice < 1 or choice > len(genres):
            print("Invalid choice")
            return
        # User list was 1-indexed, su subtract 1 to find id in 0-indexed list
        genre_id = genres[choice-1]
        # call the function with the selected genre ID
        df = gettoptengenre(year, genre_id)
        print(df)

    elif _=="3":
        sys.exit
    
    else:
        print("Please make a choice.")
        menu()


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


# Future implementation
def plot_pdf():
    ...
    '''
    https://www.tutorialspoint.com/save-the-plots-into-a-pdf-in-matplotlib
    d = {'Column 1': [i for i in range(10)], 'Column 2': [i * i for i in range(10)]}

    df = pd.DataFrame(d)

    df.plot(style=['o', 'rx'])
    plt.savefig("myImagePDF.pdf", format="pdf", bbox_inches="tight")
    plt.show()
    '''


if __name__ == "__main__":
    main()