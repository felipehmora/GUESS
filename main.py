import random

guessTaken = 0
minNumber = 0
maxNumber = 20

print('Hello! What is your name?')
username = input()

number = random.randint(minNumber, maxNumber)


print('Well, ' + username + ' I am thinking in a number between ' + str(minNumber) + ' and ' + str(maxNumber))

while guessTaken < 6:
    print("Take a guess: ")
    guess = input()
    guess = int(guess)

    guessTaken = guessTaken + 1

    if guess < number:
        print("Your number is too low")
    if guess > number:
        print("Your number is too high")
    if guess == number:
        break

if guess == number :
    guessTaken = str(guessTaken)
    print("Good job " + username + " You guessed my number in " + guessTaken + " guesses") 

if guess != number:
    number = str(number)
    print("No, the number I was thinking of was " + number)