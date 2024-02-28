#Write a program that takes in a user input and prints out how many vowels are in the response

users_input = input("Enter a phrase or sentence: ")
vowel = 0

lowercase = users_input.lower() #so it wont be case sensitive
vowels = {'a', 'e', 'i', 'o', 'u'}

for char in lowercase:
    if char in vowels:
        vowel += 1

#Create a list of names of 4 letters or more and capitalize each name
names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']        

new_names = [name.capitalize() for name in names if len(name) >= 4]