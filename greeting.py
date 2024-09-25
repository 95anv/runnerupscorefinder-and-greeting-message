import random

birthdayDictionary = {"Bharat": "13 January", "Arun": "15 August", "Rahul": "19 May"}

def BirthdayGreeting(person, birthday):
    adjectives = ["great", "cool", "awesome", "wonderful", "amazing", "spectacular"]
    adjective = random.choice(adjectives)
    greeting = ("Hey {}, \nwishing you a very happy birthday this {}.\nI hope you have a {} year ahead!\n\n ~Anubhav❤️\n").format(person, birthday, adjective)
    greeting += ("_____________________________________________________\n")
    return greeting

for person, birthday in birthdayDictionary.items():
    print(BirthdayGreeting(person, birthday))