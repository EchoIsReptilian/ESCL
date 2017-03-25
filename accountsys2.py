#!/usr/bin/python
import hashlib
import sha3
import os
import sys
import getpass

filedir = 'accounts/'

def getHash(userinput):
    userinput = bytes(userinput, encoding='ascii')
    userinput = hashlib.sha3_512(userinput)
    userinput = userinput.hexdigest()
    userinput = str(userinput, encoding='ascii')

    return userinput


def createAccount():
    username = input("Please enter your desired username: ")

    username = getHash(username)
    username = filedir + username

    try:
        accountTest = open(username, 'r')

        print("Error, that username already exists, please choose another")
        createAccount()

    except IOError:
        pass

    password = getpass.fallback_getpass("Please enter your desired password: ")
    passwordConfirm = getpass.fallback_getpass("Please confirm your password: ")

    if password != passwordConfirm:
        print("Sorry, your passwords do not match. Please try again")

        os.system('cls')
        os.system('clear')
        createAccount()

    password = getHash(password)

    account = open(username, 'w')
    account.write(password)

    print("Complete")


def signin():

    username = input("Please enter your username: ")
    username = getHash(username)
    username = filedir + username

    try:
        accountTest = open(username, 'r')

    except IOError:
        print("Username not found!")
        signin()

    password = getpass.fallback_getpass("Please enter your password: ")

    password = getHash(password)

    if accountTest.read() == password:
        print("You have sucessfully signed in")

    else:
        print("You entered the wrong password")
        signin()


def main():
    userChoice = input("Would you like to\n"
                       "1. Sign in? \n"
                       "2. Sign up? \n")
    
    if userChoice == "1":
        signin()

    elif userChoice == "2":
        createAccount()
        main()

    elif userChoice == "42":
        print("THE ULTIMATE ANSWER! BUT WHAT IS THE ULTIMATE QUESTION?")

    else:
        print("Please enter 1 or 2.")
        main()

if __name__ == '__main__':
    main()
