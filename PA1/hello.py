# assignment: programming assignment 1
# author: Michael Coe
# date: 10/12/2020
# file: hello.py is a program that asks the user to enter user’s name,
#       age, and favorite movie and outputs a greeting message that
#       include the information about the user
# input: string data
# output: string data

name = input("Hello! What is your name? ")
age = int(input("\nWhat is your age? "))
favorite_movie = input("\nWhat is your favorite movie? ")
print("\nNice to meet you," + str(name) + '.')
print(f"\nYou are {age} years old and your favorite movie is {favorite_movie}.")