#this is a number guessing game.
import random

guesses_taken = 0

name = raw_input("Hello! What is your name? ")

print "Want to play a game, %s?" % name
print "I am thinking of a number between 1 and 20... Can you guess what it is?"

number = random.randint(1,20)

while guesses_taken < 5:
    print "Take a guess!"
    guess = input()
    guess = int(guess)

    guesses_taken = guesses_taken + 1

    if guess < number:
        print "Your guess is too low..."

    if guess > number:
        print "Your guess is too high..."

    if guess == number:
        break

if guess == number:
    guesses_taken = str(guesses_taken)
    print "Way to go %s! You guessed the correct number in %s guesses" % (name, 
        guesses_taken)
if guess != number:
    number = str(number)    
    print "Nope. The number I was thinkking of was %s" % number