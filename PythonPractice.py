from random import *
from time import * 

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        sleep(1)
        t -= 1
    return True



def guessNumber(x):
    randomNumber = randint(1, x)
    guess = 0
    while(guess != randomNumber):
        guess = int(input("Can you guess the random Number?"))
        if guess > randomNumber:
            print("Your guess is bigger than the number")
        elif guess < randomNumber: 
            print("Your guess is less than the number")
        else:
            print(f"Good Job you guessed the number, it was {randomNumber}")
            


def computerGuessNum(x):
    low = 0
    high = x
    correct = False
    while(not correct):
        number = randint(low, high)
        print(correct)
        correct = bool(int(input(f"My guess is {number}, was I correct? (0) No (1)Yes ")))
        if(not correct):
            correction = input("Was I too [high] or [low]?")
            if(correction.strip().lower() == "high"):
                high = number - 1
            else:
                low = number + 1


def RockPaperScissors():
    options = ["rock", "paper", "scissors"]
    print("Let's play a game of Rock, Paper, Scissors shoot, ready?")
    print("Ready")
    countdown(1)
    print("Set")
    countdown(1)
    print("Go!")
    computerChoice = choice(options)
    userChoice = input()
    def defineWinner(comp, user):
        comp = comp.lower()
        user = user.lower()
        if((comp == "rock" and user == "scissors") or (comp == "scissors" and user == "paper") or (comp == "paper" and user=="rock")):
            return "Computer"
        else:
            return "User"
    while userChoice.strip().lower() not in options:
        print("Please enter a valid choice")
        userChoice = input()
    if computerChoice == userChoice:
        print("It's a tie!")
        return
    print(f"The winner is the {defineWinner(computerChoice,userChoice)}")


def hangMan(word):
    word = word.lower()
    usedLetters = []
    mysteryWord = []
    lives = 6
    for letter in word:
        mysteryWord.append("_")
    while ("_" in mysteryWord) and (lives <= 6):
        print("You have used : " , " ".join(usedLetters))
        print("The word, so far, is " , " ".join(mysteryWord))
        guess = input("What is your next guess?")
        guess = guess.lower().strip()
        if(lives == 0):
            print("You ran out of lives :(")
            return
        if(len(guess) > 1):
            print("Please enter one letter")
            continue 
        if(guess in usedLetters):
            print("Please enter a letter you haven't already guessed")
            continue
        if(guess in word): 
            print("That is in the word")
            usedLetters.append(guess)
            for i in range(len(word)):
                if guess == word[i]:
                    mysteryWord.pop(i)
                    mysteryWord.insert(i, guess)
        else:
            print("That is not in the word")
            usedLetters.append(guess)
            lives -=1
            print(f"You have {lives} many tries left")
    print(f"You guessed it, the word was {word}")
    
hangMan("Abhorrent")