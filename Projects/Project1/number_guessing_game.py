import random

def number_guessing_game():
    secret_number = random.randint(1,100)
    guess= None


    print("Welcome to the Gussing Number game!")
    print("I am thinking of a number between 1 to 100")
    print("Can you guess what it is?")

    while guess != secret_number:
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print("Too low! Try Again")

        elif guess > secret_number:
            print("Too high! Try Again")

        else:
            print("Congratulations! You guesses correct number")

number_guessing_game()     
               

