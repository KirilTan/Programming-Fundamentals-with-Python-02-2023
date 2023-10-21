def sort_names(list_of_names: list) -> list:

    """This function takes a list of names and returns a sorted list of names.
    The names are sorted from longest to shortest. If the names are the same length they sorted alphabetically."""

    return sorted(list_of_names, key=lambda x: (-len(x), x))


names = input().split(", ")

print(sort_names(names))
