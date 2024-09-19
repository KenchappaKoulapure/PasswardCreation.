import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to th passward generator.... ")

nr_latters = int(input("How many latters you want?... "))
nr_numbers = int(input("how many number u want?.. "))
nr_symbols = int(input("how many symbols u want"))


passward = " "

for char in range(0, nr_latters):
    passward += random.choice(letters)
    for char in range(0,nr_numbers):
        passward += random.choice(numbers)
        for char in range(0, nr_symbols):
            passward += random.choice(symbols)

print(passward)
