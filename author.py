import os
os.system("clear")

from enum import Enum

class Gender(Enum): # I hope this is what you meant :D 
    MALE = "Male"
    FEMALE = "Female"
    NON_BINARY = "Non-Binary"

class Author:
    def __init__(self, name, email, gender: Gender = Gender.MALE):
        self.__name = name
        self.__email = email
        self.__gender = gender

    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email

    def get_gender(self):
        return self.__gender
    
    def __str__(self):
        return f"Author name = {self.__name}, email = {self.__email}, gender = {self.__gender.value}"


# author = Author("John", "john@gmail.com", gender=Gender.MALE) # Creating an Author instance
# print(author.__str__())                                       # Printing the author details
                                                                # only if we want to print with this file

    