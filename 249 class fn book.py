# Create a method in the Book class.
# Insert a function that returns a formatted string
# with the book title and author,
# and execute it on the b1 object.

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Book title:{self.title}\nBook author:{self.author}")

b1 = Book("Abc","Kalam")
b1.display()