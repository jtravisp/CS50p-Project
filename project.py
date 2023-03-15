import pandas as pd
# import matplotlib.pyplot as plt


def main():
    actor = input("Actor Name: ")
    year = input("Year: ")

    count = find_actorbyyear(actor, year)
    print(f"{actor} appears in productions from the year {year} on Netflix {count} times.")


def find_actorbyyear(actor, year):
    df = pd.read_csv('netflix_titles.csv')

    df['cast'] = df['cast'].str.split(', ')
    df = df.explode('cast')

    df_year = df[df['release_year'] == year]

    actor_counts = df.groupby(['cast']).size()
    count = actor_counts.get((actor), 0)

    return count


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