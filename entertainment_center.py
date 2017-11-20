import media
import fresh_tomatoes

# create new object from Movie class (title, short description, poster
# image, youtube link)

toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://goo.gl/whcxwn",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://goo.gl/CoQehK",
    "http://www.youtube.com/watch?v=-9ceBgWV8io")

the_blind_side = media.Movie(
    "The Blind Side",
    "The story of Michael Oher, football player",
    "https://goo.gl/rmM1Tj",
    "https://www.youtube.com/watch?v=gvqj_Tk_kuM")


school_of_rock = media.Movie(
    "School of Rock",
    "2003 American musical comedy film",
    "https://goo.gl/htpL7E",
    "https://www.youtube.com/watch?v=5afGGGsxvEA")

ratatouille = media.Movie(
    "Ratatouille",
    "A story about cat and chief",
    "https://goo.gl/QIS1lc",
    "https://www.youtube.com/watch?v=niD-jahFURU")

midnight_in_paris = media.Movie(
    "Midnight in Paris",
    "A romantic comedy set in Paris",
    "https://goo.gl/N5o95E",
    "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie(
    "Hunger Games",
    "A story about compete in the Hunger Games.",
    "https://goo.gl/FLrxOS",
    "https://www.youtube.com/watch?v=mfmrPu43DF8")


movies = [
    toy_story,
    avatar,
    the_blind_side,
    school_of_rock,
    ratatouille,
    midnight_in_paris,
    hunger_games]

# open page in browser

fresh_tomatoes.open_movies_page(movies)


# print (media.Movie.VALID_RATINGS)

print (media.Movie.__module__)
