import random


def welcome_msg():
    print("""
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
WELCOME TO THE NUMBER GUESSING GAME!!!
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
    """)
    return random.randint(1, 10)


def attempts_reset():
    return 0


def start_game():
    sec_num = welcome_msg()
    attempts = attempts_reset()
    high_score = 12
    print("The current High Score is {}".format(high_score))
    while True:
        guess = input("\nPick a number between 1 and 10: ")
        try:
            guess = int(guess)
        except ValueError:
            print("\nThat's not an integer, Please Try Again.")
        else:
            if guess > 0 and guess < 11:
                attempts += 1
                if guess == sec_num:
                    if attempts == 1:
                        print("\nWOW! You guessed it right in {} attempt".format(attempts))
                    else:
                        print("\nYou guessed it right in {} attempts.".format(attempts))
                    if attempts < high_score:
                        print("\nYou have just set a new High Score at: {}".format(attempts))
                        high_score = attempts
                    elif attempts > high_score:
                        print("\nHigh Score is: {}. You got this keep trying!".format(high_score))
                    guess = input("\nWould you like to play again? ENTER [y]es/[n]o: ")
                    guess = str(guess)
                    if guess == "y":
                        print("Awesome, Good Luck!")
                        sec_num = welcome_msg()
                        print("The current High Score is {}".format(high_score))
                        attempts = attempts_reset()
                        continue
                    elif guess == "n":
                        print("\nNo worries, come back anytime! Exiting Game")
                        break
                    else:
                        print("\nNot a valid response. Leaving Game!")
                        break
                elif guess < sec_num:
                    print("\nYou need to guess higher.")
                elif guess > sec_num:
                    print("\nYou need to guess Lower.")
            else:
                print("\nThat's not inside the number range. Please try again!")


if __name__ == '__main__':
    start_game()
