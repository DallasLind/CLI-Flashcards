# CLI-Flashcards

### What is this project?
This is my first foray into using Python, PostgreSQL, and Peewee for a project. What I've created is a simple flashcard game meant to played in the Command Line that tests your knowledge of Japanese! This is one of my projects assigned through the Software Engineering Immersive program at General Assembly. 

### Example
```
Ready to practice your Japanese? Don't worry, we're not nearly as vigilant as Duolingo. Select 'c' to create your flashcard, 'r' to read through the cards, 'd' to delete, and 'p' to test your knowledge! 
What would you like to do? 

>p

How many words would you like to study this session? 

>4

茶
>Tea
Amount of correct: 1

私 
>I

Amount of correct: 2
先生
>Sensei

Amount of correct: 3
コーラ
>Cola

Amount of correct: 4

Would you like to practice again? Please type 'y' for yes and 'n' stop your session. 
>n

Thanks for practicing today!
```

### Languages and Technologies Used
* Python
* Peewee
* Postgres

### Challenges
I actually found this project refreshing and fun to implement! I think at the moment that I am struggling with some aspects of Peewee and CRUD functionality, but this is something I'm planning on working on sooner than later.

### Build Status
![](https://img.shields.io/badge/BUILD-IN%20PROGRESS-informational)

### Future Plans
* Implement Update Successfully 
* Ensure Delete can actually delete duplicates without running into errors
* Shuffle Deck 

### How to Install
1. Clone this repo 
``` git@github.com:DallasLind/CLI-Flashcards.git ```

2. Enter into your root directory 
``` cd CLI-Flashcards ```
3. Install dependencies
```pip install peewee```

4. Run!
``` pipenv run python3 flashcards.py ```

### Sidenote
Just a heads up, this app is best utilized with a Japanese keyboard plugin! 
