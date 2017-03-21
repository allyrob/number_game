#this is a number guessing game.
import random

guesses_taken = 0
guesses_taken_2 = 0

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
    print "Better luck next time!"

round2 = int(raw_input("Want to try again? - type 1 for yes and 2 for no"))

if round2 == 1:
    print "OK, here we go... I am thinking of a number between 1 and 50"
elif round2 == 2:
    print "Thanks for playing, use CTRL+ C to exit"
    


number_2 = random.randint(1,50)
while guesses_taken_2 < 5:
    print "Take a guess!"
    guess_2 = input()
    guess_2 = int(guess_2)

    guesses_taken_2 = guesses_taken_2 + 1

    if guess_2 < number_2:
        print "Your guess is too low..."

    if guess_2 > number_2:
        print "Your guess is too high..."

    if guess_2 == number_2:
        break
if guess_2 == number_2:
    guesses_taken_2 = str(guesses_taken_2)
    print "Way to go %s! You guessed the correct number in %s guesses" % (name, 
        guesses_taken_2)
if guess_2 != number_2:
    number_2 = str(number_2)    
    print "Nope. The number I was thinkking of was %s" % number_2
    print "I'm tired, you should find a new game"


