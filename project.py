import pandas as pd
import sys
from tmdbapi import getid, getmovie, gettopten, gettoptengenre
# import matplotlib.pyplot as plt

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