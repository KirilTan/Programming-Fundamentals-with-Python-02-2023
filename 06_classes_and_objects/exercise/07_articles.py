class Article:
    def __init__(self, title: str, content: str, author: str):
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new_content: str) -> None:  # changes the old content to the new one
        self.content = new_content

    def change_author(self, new_author: str) -> None:  # changes the old author with the new one
        self.author = new_author

    def rename(self, new_title: str) -> None:  # changes the old title with the new one
        self.title = new_title

    def __repr__(self):  # returns the following string "{title} - {content}: {author}"
        return_text = f"{self.title} - {self.content}: {self.author}"
        return return_text


# Example usage:
article = Article(
    "Highest Recorded Temperature",
    "Temperatures across Europe are unprecedented, according to scientists.",
    "Ben Turner"
)
article.edit(
    "Syracuse, a city on the coast of the Italian island of Sicily, registered temperatures of 48.8 degrees Celsius"
)
article.rename(
    "Temperature in Italy"
)
article.change_author(
    "B. T."
)
print(article)
