"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can
totally do that by clicking: File -> Download Workspace in the file menu after
you fork the snapshot of this workspace.

"""
# Importing our random library
import random


# Our welcome message function and welcome banner
def welcome_msg():
    print("""
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
WELCOME TO THE NUMBER GUESSING GAME!!!
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
    """)
    return random.randint(1, 10)


# Our attempts reset function to start each new game at 0
def attempts_reset():
    return 0


# Our start game function
def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    Meets requirments with >>>
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )

    Exceeds requirements with >>>
    -------------------------------------
    1. As a player my guess should be within the number range. If my guess is outside the number
        range i should be told to try again.
    2. As a player of the game after i guess correctly i should be prompted if i would like to
        play again.
    3. As a player of the game, at the start of the game i should be shown the high score(least amount
        of points) so that i know what i am supposed to beat.
    4. Every time a player decides to play again, the random number to the guess is updated so
        players are guessing something new each time.
    """
    # write your code inside this function

    # Calling for the random number to be set
    sec_num = welcome_msg()

    # Pre setting the attempts to 0
    attempts = attempts_reset()

    # Pre setting a default high score to 12, Only because I'm a die hard Seahawks Fan!!!
    high_score = 12

    # Informing the user of the current high score
    print("The current High Score is {}".format(high_score))

    # Starting my loop for the game
    while True:
        # Asking the user to input a number between the given range
        guess = input("\nPick a number between 1 and 10: ")
        try:
            # Checking if the input from the user is an integer
            guess = int(guess)
        except ValueError:
            # If the user inputs anything other than an integer run the exception and prompt user
            print("\nThat's not an integer, Please Try Again.")
        else:
            # Checking if the integer was inside the given range 1 to 10
            if guess > 0 and guess < 11:
                # Counting the attempt even if the user guesses outside the range
                attempts += 1
                # Checking if the user guesses the secret number
                if guess == sec_num:
                    # Checking if the user guessed the secret number in 1 attempt
                    if attempts == 1:
                        # If it was 1 attempt prompt the user this message
                        print("\nWOW! You guessed it right in {} attempt".format(attempts))
                    else:
                        # If it took more than 1 attempt prompt the user this message
                        print("\nYou guessed it right in {} attempts.".format(attempts))
                    # Checking if the amount of the attempts was lower than the high score
                    if attempts < high_score:
                        # If it was then prompt the user they set a new high score
                        print("\nYou have just set a new High Score at: {}".format(attempts))
                        # Setting the high_score variable to attempts taken
                        high_score = attempts
                    # Checking if the amount of the attempts was higher than the high score
                    elif attempts > high_score:
                        # If it was then prompt the user of the current high score
                        print("\nHigh Score is: {}  You got this keep trying!".format(high_score))
                    # Prompting the user if they would like to play again
                    guess = input("\nWould you like to play again? ENTER [y]es/[n]o: ")
                    # Setting the guess variable to string format for the input
                    guess = str(guess)
                    # Checking if the input from user is a [y] for yes
                    if guess == "y":
                        # If it is print a good luck message
                        print("Awesome let's go, Good Luck!")
                        # Resetting the random number and returning the user to the welcome banner
                        sec_num = welcome_msg()
                        # Resetting the attempts for the new game
                        attempts = attempts_reset()
                        # Continuing the game
                        continue
                    # Checking if the input from user is a [n] for no
                    elif guess == "n":
                        # If it is print an Exiting Game message
                        print("\nNo worries, come back anytime! Exiting Game")
                        # Stopping the loop and the program
                        break
                    else:
                        # If the user inputs anything other than "y" or "n" print this message
                        print("\nNot a valid response. Exiting Game!")
                        # Exiting the game due to invalid input from user
                        break
                # Checking if the integer input from user is lower than the sec_num
                elif guess < sec_num:
                    # If it is then print the guess higher hint message
                    print("\nYou need to guess higher.")
                # Checking if the integer input from user is higher than the sec_num
                elif guess > sec_num:
                    # If it is then print the guess lower hint message
                    print("\nYou need to guess Lower.")
            # If the guess was outside the given range, prompting the user to try again
            else:
                print("\nThat's not inside the number range. Please try again!")


# Kick off the program by calling the start_game function.
if __name__ == '__main__':
    start_game()
