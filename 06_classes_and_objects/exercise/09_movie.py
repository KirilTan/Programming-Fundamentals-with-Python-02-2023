class Movie:
    __watched_movies = 0

    def __init__(self, name: str, director: str):
        self.name = name
        self.director = director
        self.watched = False

    def change_name(self, new_name: str) -> None:
        self.name = new_name

    def change_director(self, new_director: str) -> None:
        self.director = new_director

    def watch(self) -> None:
        self.watched = True
        Movie.__watched_movies += 1

    def __repr__(self) -> str:
        return_text = (f"Movie name: {self.name}; "
                       f"Movie director: {self.director}. "
                       f"Total watched movies: {Movie.__watched_movies}")
        return return_text


# Example usage:
first_movie = Movie("Inception", "Christopher Nolan")
second_movie = Movie("The Matrix", "The Wachowskis")
third_movie = Movie("The Predator", "Shane Black")
first_movie.change_director("Me")
third_movie.change_name("My Movie")
first_movie.watch()
third_movie.watch()
first_movie.watch()
print(first_movie)
print(second_movie)
print(third_movie)
