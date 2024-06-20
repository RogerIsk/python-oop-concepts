class Book:
    def __init__(self, name, author, price, qty):
        self.__name = name
        self.__author = author  # This should be an Author object
        self.__price = price
        self.__qty = qty

    def get_name(self):
        return self.__name

    def get_author(self):
        return self.__author  # Ensure this is returning an Author object

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_qty(self):
        return self.__qty

    def set_qty(self, qty):
        self.__qty = qty

    def __str__(self):
        return f"Book[name={self.__name}, author={self.get_author().get_name()}, price={self.__price}, qty={self.__qty}]"

#author = Author("John", "john@gmail.com", gender=Gender.MALE)        # without this I get an error
#book = Book("How to sleep good", author=author, price=29.95, qty=16) # took me a while to figure out the author thing
#print(author.__str__())
#print(book.__str__())