# Homework 3
# number 1
def count_vowels(text):
    count = 0
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    for i in range (len(text)):
        if text[i] in vowels:
            count += 1
    return count


print(count_vowels ("Lilli"))

# number 2
def hamming(text1, text2):
    i = 0
    count = 0

    while (i < len(text1)):
        if (text1[i] != text2[i]):
            count += 1
        if len(text1) != len(text2):
            return 0
        i += 1
    return count


print(hamming ("Jisoo", "Jimin"))

# number 3
class Vehicle():
    def __init__(self, fuel_type, color):
        self.fuel_type = fuel_type
        self.color = color

class Car(Vehicle):
    def __init__(self, fuel_type: str, color: str, doors: str):
        Vehicle.__init__(self, fuel_type, color)
        self.doors = doors
        print(f" Color: {self.color}, Fuel Type: {self.fuel_type}, Doors: {self.doors}.")

class Bus(Vehicle):
    def __init__(self, fuel_type: str, color: str, passengers: str):
        Vehicle.__init__(self, fuel_type, color)
        self.passengers = passengers
        print(f" Color: {self.color}, Fuel Type: {self.fuel_type}, Passengers: {self.passengers}.")

Car("black", "hybrid", "4")
Bus("hybrid", "yellow", "10")

# number 4
class Book():
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author
    def __str__(self):
        details = ''
        details += f"{self.name}, {self.author}"
        return details
book1 = Book("Divergent", "Veronica Roth")
print(book1)

# number 5
class BookShelf():
    def __init__(self):
        self.moje_books = []

    def add_book_list(self, books: list):
       for book in books:
            if isinstance(book, Book):
                self.moje_books.append(book)

    def books_by_author(self, author):
        result = []
        for book in self.moje_books:
            if book.author == author:
                result.append(book.name)
        return result

    def get_books(self):
        result = []
        for book in self.moje_books:
            result.append(book.name)
        return result

    def clear_shelf(self):
        self.moje_books.clear()

shelf = BookShelf()

booklist = [Book("Divergent", "Veronica Roth"), Book("Insurgent", "Veronica Roth"), Book("Ogniem i mieczem", "Henryk Sienkiewicz")]
shelf.add_book_list(booklist)
booklist2 = ["Kogel mogel", "Niezgodna", "Uwierz w ducha", Book("Allegiant", "Veronica Roth")]
shelf.add_book_list(booklist2)

print(shelf.books_by_author("Veronica Roth"))
print(shelf.get_books())
print(shelf.clear_shelf())
print(shelf.books_by_author("Henryk Sienkiewicz"))
print(shelf.get_books())