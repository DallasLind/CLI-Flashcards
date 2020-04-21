from peewee import *
from datetime import date
import gc

db = PostgresqlDatabase('japanese', user='postgres', password='',
                        host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class FlashCards(BaseModel):
    word_japanese = CharField()
    word_english = CharField()

db.create_tables([FlashCards])

def menu():
    print("Ready to practice your Japanese? Don't worry, we're not nearly as vigilant as Duolingo. Select 'c' to create your flashcard, 'r' to read through the cards,  and 'p' to test your knowledge! ")
    choice = input('What would you like to do? ')
    if choice == 'c':
        create()
    elif choice == 'r': 
        read()
    elif choice == 'p': 
        play()
    else: 
        print('Sorry that is not a valid choice, please try again')
        menu()

def create():
    japanese = input("Please input the Japanese character of the word you'd like to study \n")
    english = input("Please input the English equivalent \n")
    card = FlashCards(word_japanese=japanese, word_english=english)
    card.save()
    print(f"{card.word_japanese} and {card.word_english}")
    menu()



def read():
    print("Flashcards")
    for card in FlashCards.select(): 
        print(f"\nJapanese: {card.word_japanese} \nEnglish: {card.word_english}")
    menu()

def play():
    correct = 0
    incorrect = 0
    a = int(input("How many words would you like to study this session? "))

    for new_word in FlashCards.select():
        if a > 0:
            a -= 1
            if input(f"{new_word.word_japanese}\n") == new_word.word_english:
                correct += 1
                print(f"Correct: {correct}")

            else:
                incorrect += 1
                print(f"Amount of incorrect: {incorrect}")
                if input("Would you like to see the answer? y/n") == 'y':
                    print(f"The answer is {new_word.word_english}")
    
    play_again = str(input("Would you like to practice again? Please type 'y' for yes and 'n' stop your session. "))
    if play_again == 'y':
        play()
    else:
            print("Thanks for practicing today!")
            menu()

menu()