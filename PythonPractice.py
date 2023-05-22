from random import *
from time import *
import sys
from math import *

# Function to count down from t seconds
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        sleep(1)
        t -= 1
    return True

# Function to guess a random number
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

# Function for the computer to guess a number
def computerGuessNum(x):
    low = 0
    high = x
    correct = False
    while(not correct):
        number = randint(low, high)
        print(correct)
        correct = bool(int(input(f"My guess is {number}, was I correct? (0) No (1) Yes ")))
        if(not correct):
            correction = input("Was I too [high] or [low]?")
            if(correction.strip().lower() == "high"):
                high = number - 1
            else:
                low = number + 1

# Function to play Rock, Paper, Scissors game
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

    # Function to define the winner
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

# Function to play Hangman game
def hangMan(word):
    word = word.lower()
    usedLetters = []
    mysteryWord = []
    lives = 6
    for letter in word:
        mysteryWord.append("_")
    while ("_" in mysteryWord) and (lives <= 6):
        print("You have used:", " ".join(usedLetters))
        print("The word, so far, is:", " ".join(mysteryWord))
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
            lives -= 1
            print(f"You have {lives} tries left")
    print(f"You guessed it, the word was {word}")

# Function to find the average of a list of numbers
def findAverage(numList):
    average = sum(numList) / len(numList)
    return int(average)

# Function to check if a number is prime
def primeOrNot(num):
    prime = -1
    for i in range(num - 1):
        if (num % (i + 1) == 0):
            prime += 1
    print(prime)
    return (prime == 0)

# Function to count the number of vowels in a word
def vowelsInAWord(word):
    vowelList = ["a", "e", "i", "o", "u"]
    vowelCount = sum(1 for letter in word.lower() if letter in vowelList)
    return vowelCount

# Function to reverse a string
def stringReverse(word):
    reverseWord = ""
    for i in range(len(word)):
        reverseWord += word[(len(word) - 1) - i]
    return reverseWord

# Function to find the factorial of a number
def findFactorial(number):
    if number == 1:
        return 1
    else:
        return number * findFactorial(number - 1)

# Function to check if a word is a palindrome
def isPalindrome(word):
    reverseWord = word.lower()[::-1]
    if word.lower() == reverseWord:
        return True
    return False

# Function to find even numbers from user input
def evenNumbers():
    numList = []
    user = ""
    while user != "break":
        user = input("Enter a number (or 'break' to stop): ")
        if user != "break":
            numList.append(int(user))
    print("Calculating...")
    evenNumbers = [num for num in numList if num % 2 == 0]
    return evenNumbers

# Function to find the maximum and minimum numbers in a list
def maxAndMin(lst):
    return [max(lst), min(lst)]

# Function to find the length of the longest non-repeating substring
def longestNonrepeat(word):
    longest = ""
    i = 0
    streak = True
    while streak:
        longest += word[i]
        i += 1
        try:
            if word[i] == word[i + 1]:
                streak = False
        except:
            return word
    return len(longest)

# Function to find the kth largest element in a list
def kthElement(lst, kth):
    sortedList = sorted(lst)
    return sortedList[-kth]

# Class representing a binary tree node
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to check if a binary tree is a valid binary search tree (BST)
def isValidBST(node, lower=float('-inf'), upper=float('inf')):
    if node is None:
        return True

    if node.val <= lower or node.val >= upper:
        return False

    return (
        isValidBST(node.left, lower, node.val) if node.left is not None else True and
        isValidBST(node.right, node.val, upper) if node.right is not None else True
    )

# Function to find all triplets in a list that sum to zero
def checkTriplets(numList):
    tripList = []
    for i in numList:
        for x in numList:
            for j in numList:
                if i == j or i == x:
                    break
                else:
                    if sum([i, x, j]) == 0:
                        tripList.append([i, x, j])
    removeDupes = []
    removeDupes = [triplet for triplet in tripList if triplet not in removeDupes]             
    return removeDupes

# Function to find the longest substring without repeating characters
def longestSub(word):
    currentLongest = ""
    seenLets = []
    longest = ""
    for i in range(len(word)):
        if word[i] not in seenLets:
            currentLongest += word[i]
            seenLets.append(word[i])
        else:
            if len(longest) < len(currentLongest):
                longest = currentLongest
            currentLongest = ""
            seenLets = []
    return longest

# Function to find the maximum sum subarray in a list
def maxSubarraySum(nums):
    max_sum = float('-inf')
    curr_sum = 0
    start = 0
    end = 0
    subarray_start = 0
    subarray_end = 0

    for i, num in enumerate(nums):
        if curr_sum <= 0:
            start = i  # Start a new subarray
            curr_sum = num
        else:
            curr_sum += num

        if curr_sum > max_sum:
            max_sum = curr_sum
            subarray_start = start
            subarray_end = i

    return nums[subarray_start:subarray_end + 1]


# Function that find the max multiplied triplet
def maxMultTrip(nums):
    currProd = prod(nums[:3])
    maxProd = currProd
    for i in range(len(nums) - 2):
        currProd = prod(nums[i:i+3])
        print(currProd, maxProd)
        maxProd = max(currProd, maxProd)
    return maxProd
nums = [-10, -5, 0, 1, 2, 3]
result = maxMultTrip(nums)
print(result)  # Expected output: 150


