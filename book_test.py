import os
os.system("clear")

from author import Author, Gender
from book import Book

class BookTest:
    def __init__(self, *args):
        author1 = None
        author2 = None
        author3 = Author("John", "john@gmail.com", gender=Gender.MALE)

        print(author1)
        print(author2)
        print(author3)  # Test __str__(self)
        author3.set_email("changedemail@email.com")  # Test email setter
        print("name is: " + author3.get_name())  # Test getter
        print("email is: " + author3.get_email())  # Test getter
        print("gender is: " + str(author3.get_gender()))  # Convert Gender to string
        print(
            "Author after changed email: "
            + str(author3)  # pay attention! author3 now has a changed email
        )
        print("========================")

        book1 = None
        book2 = None
        book3 = Book("Some Book", author3, 19.95, 99)  # Ensure author3 is passed here

        print(book1)
        print(book2)
        print(book3)

        # Test Getters and Setters
        book3.set_price(29.95)
        book3.set_qty(28)
        print("name is: " + book3.get_name())
        print("price is: " + str(book3.get_price()))
        print("qty is: " + str(book3.get_qty()))
        print("Author is: " + str(book3.get_author()))
        # Author's __str__(self)
        print("Author's name is: " + book3.get_author().get_name())
        print("Author's email is: " + book3.get_author().get_email())
        print("Book after changed price and quantity: " + str(book3))

if __name__ == "__main__":
    BookTest()

    # this is good enough for me :D