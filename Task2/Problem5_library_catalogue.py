library_catalogue = {
    "book1": {
        "title": "Batman: Year One",
        "author": "Frank Miller",
        "publication_year": 1987
    },
    "book2": {
        "title": "Batman: The Dark Knight Returns",
        "author": "Frank Miller",
        "publication_year": 1986
    },
    "book3": {
        "title": "Batman: Hush",
        "author": "Jeph Loeb",
        "publication_year": 2002-2003
    },
    "book4": {
        "title": "Batman: The Killing Joke",
        "author": "Alan Moore",
        "publication_year":  1988
    },
    "book5": {
        "title": "Batman: Arkham Asylum",
        "author": "Grant Morrison",
        "publication_year": 1989
    }
}

# Example usage:
for book_id, book_details in library_catalogue.items():
    print(f"Book ID: {book_id}")
    print(f"Title: {book_details['title']}")
    print(f"Author: {book_details['author']}")
    print(f"Publication Year: {book_details['publication_year']}")
    print()
