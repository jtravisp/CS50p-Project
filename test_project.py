from tmdbapi import getmovie, getid


def test_id():
    assert getid("Casablanca") == 289

def test_movie():
    assert getmovie(289) == "Casablanca"



if __name__ == "__main__":
    main()