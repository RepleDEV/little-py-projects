# Import numpy for random number generation
import numpy as np 
# Import sys for sys.exit() function
import sys 

# Message
print("Welcome to Guess The Number!")
# Message
print("The system will generate a random number upwards from 0 (Zero) to the number that you choose, and you have to guess that number!")
# Spacer
print('')

# Input for choosing to start game or not
inp = input('Start Game? (Y/N) ')

# Checks if user answered N (NO)
if (inp.upper() == 'N'): 
    # Message
    print('Exiting...')
    # Exits
    sys.exit(1)

# Input for max number threshold
num = input("How high do you want the number to be generated? (ONLY ACCEPTING NUMBERS) ")

# Checks if user inputs data types other than number (e.g. String)
try:
    # Updates the num variable to an integer
    num = int(num)
except:
    # Illegal input type. Law broken. Please transfer 500 dollars worth of BitCoin to save your chicken McNuggets.
    print("Error, illegal input type. Please restart")

    # Exits the system and steals your chicken McNuggets if you haven't paid 500 dollars worth of BitCoin to our StarBucks account.
    sys.exit(1)

# Generates a random number from 0 until the max threshold of the number that the user specified using numpy
rng = int(np.random.uniform(0.0, num, 1))

# Message
print('Alright! The computer has picked a number from 0 to ' + str(num) + '! '  'Guess the number!')

# Status. False = User still incorrect; True = User has answered correctly.
status = False;
# Number or attempts. Or the number of times you have failed. Or the number of times you haven't gave up :D
attempts = 0;

# While the status is still False, the system will keep asking the correct number to the user.
while (status == False):
    # Spacer
    print('')
    # Input for the value guessed by the user
    nGuess = input("Your value guess? ")

    # If the guessed number was below the Randomly Generated Number
    if (int(nGuess) < rng):
        # It tells the user that their guess was too low and they should go back to school
        print('A little too low!')
        # Adds 1 to your attempts
        attempts += 1
    # If the number that the user guessed was too high? 
    elif (int(nGuess) > rng):
        # Well, the system tells that they guessed too high, and should go back to learning the alphabet
        print('A little too high!')
        # Also adds 1 to your attempts
        attempts += 1

    # If they were correct though? (Ain't gonna be first try obviously cuz my system is smarter than any human! Ahahahah!)
    if (int(nGuess) == rng) :
        # And this also adds 1 to your total attempts. Thank me later
        attempts += 1
        # It congratulates them for beating the system. Even tho it wasn't the first try.
        print('Correct!! The number that the system has randomly picked was ' + str(rng) + '!')
        # Congratulations. You won... I guess... BUT NOT FOR LONG THOUGH, SINCE I WILL OUTSMART YOUR OUTSMARTING!
        print('Congratulations! You won!!')

        print('Your number of attempts: ' + str(attempts) + '!')
        # Spacer
        print('')
        # Updates the status to True, indicating that the user has won. Finally (after 1000 tries)
        status = True;

# Tells the user that the game is exiting, and that you are done playing, and should really go to sleep.
print('Exiting Game...')