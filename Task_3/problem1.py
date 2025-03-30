
library_catalogue = {"Atomic Habits":{"author": "James Clear","year": 2018},
                     "Harry Potter and the Deathly Hallows":{"author" :"J.K","year": 2007},
                     "The Alchemist": {"author": "Paulo Coelho", "year": 1988}}

for title,details in library_catalogue.items():
    print(f"Title: {title},Author: {details['author']},Year: {details['year']}")