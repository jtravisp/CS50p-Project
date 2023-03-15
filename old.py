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
