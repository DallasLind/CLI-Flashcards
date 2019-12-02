from peewee import *

db = PostgresqlDatabase('cards', user='postgres', password='', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class FlashCards(BaseModel):
    title = CharField()
    character = CharField()
    romaji = CharField()

db.connect()

db.create_tables([Japanese])

def start():
    print("Ready to practice your Japanese? Don't worry, we're not nearly as vigilant as Duolingo. Select 'c' to create your flashcard, 'r' to read through, 'u' to update existing cards, 'd' to delete, and 's' to find a specific card!")
     if choice == 'c':
        create()
    elif choice == 'r': 
        read()
    elif choice == 'u': 
        update()
    elif choice == 'd': 
        delete()
    elif choice == 's': 
        find_card()
    else: 
        print('Sorry that is not a valid choice, please try again')
        intro()

def create():
    