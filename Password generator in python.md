# password generator in python
# It generate strong password of 8 character long
from string import punctuation   # punctuation contains all special characters
import string
import random as rd


class PasswordGenerator:
    def __init__(self):
        self.__passwordInList = []
        self.__password = 0
        self.__numberList = [num for num in range(0, 10)]
        self.__specialCharacters = list(punctuation)
        self.__lowercaseLetters = list(string.ascii_lowercase)
        self.__uppercaseLetters = list(string.ascii_uppercase)
        self.__listOfAll = []
        self.__listOfAll.append(self.__numberList)
        self.__listOfAll.append(self.__lowercaseLetters)
        self.__listOfAll.append(self.__uppercaseLetters)
        self.__listOfAll.append(self.__specialCharacters)

    def password(self):
        for i in range(0, 8):
            chosen = rd.choice(self.__listOfAll)
            self.__passwordInList.append(rd.choice(chosen))

        self.__password = "".join(map(str, self.__passwordInList))  # changing list to string
        print(self.__password)


password = PasswordGenerator()
print(password.password())

