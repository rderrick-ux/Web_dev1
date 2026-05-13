import datetime
import json
import os


class Base:
    def __init__(self, id):
        self.id = id
        self.created_at = str(datetime.datetime.now())
        self.updated_at = str(datetime.datetime.now())

    def save_file(self):
        filename = f"{self.id}.json"
        data = vars(self)

        if os.path.exists(filename):
            with open(filename, "r") as f:
                old_data = json.load(f)
            data["created_at"] = old_data["created_at"]
            data["updated_at"] = str(datetime.datetime.now())

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Saved {filename}")


class Book(Base):
    def __init__(self, id, title, author, year, pages, genre, is_borrowed=False):
        super().__init__(id)
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.genre = genre
        self.is_borrowed = is_borrowed


class User(Base):
    def __init__(self, id, name):
        super().__init__(id)
        self.name = name

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} is not available")


def load_all_json():
    for file in os.listdir("."):
        if file.endswith(".json"):
            with open(file, "r") as f:
                print(json.load(f))

book1 = Book("book1", "Harry Potter", "J.K. Rowling", 1999, 317, "Fantasy")
book2 = Book("book2", "Percy Jackson", "Rick Riordan", 2007, 312, "Mythology")
user1 = User("user1", "Janet")
user2 = User("user2", "Michael")

user1.borrow_book(book1)
user2.borrow_book(book2)

book1.save_file()
user1.save_file()
book2.save_file()
user2.save_file()

print("\nAll JSON files found:")
load_all_json()
