from peewee import *
from datetime import date
import gc
db = PostgresqlDatabase('japanese', user='postgres', password='', host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class FlashCards(BaseModel):
    word_japanese = CharField()
    word_english = CharField()

def menu():
    print("Ready to practice your Japanese? Don't worry, we're not nearly as vigilant as Duolingo. Select 'c' to create your flashcard, 'r' to read through the cards, 'u' to update existing cards, 'd' to delete, and 'p' to test your knowledge!")
    choice = input('What would you like to do?')
    if choice == 'c':
        create()
    elif choice == 'r': 
        read()
    elif choice == 'u': 
        update()
    elif choice == 'd': 
        delete()
    elif choice == 'p': 
        play()
    else: 
        print('Sorry that is not a valid choice, please try again')
        menu()

def create():
    print("Please input the Japanese character (Kanji, Hiragana, or Katakana) and it's English equivalent!")
    new_word_japanese = input("What is the word in Japanese you'd like to study?")
    new_word_english = input("What is the English meaning?")
    new_word = FlashCards(word_japanese = new_word_japanese, word_english = new_word_english)
    new_word.save()
    print('Thanks for adding to the flash cards!')

def read():
    for obj in gc.get_objects():
        if isinstance(obj, FlashCards):
            print obj.new_word

def 

def play():
    correct = 0
    incorrect = 0
    a = int(input("How many words would you like to study this session? "))

    for new_word in FlashCards.select():
        if a > 0:
            a -= 1
            if input(f"{new_word.japanese}\n") == new_word.english:
                correct += 1
                print(f"Amount of correct: {correct}")

            else:
                incorrect += 1
                print(f"Amount of incorrect: {incorrect}")
                if input("Would you like to see the answer? y/n") == 'y':
                    print(f"The answer is {new_word.english}")

menu()
    
