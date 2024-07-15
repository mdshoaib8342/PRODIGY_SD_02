import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False
    
    print("Welcome to the Guess the Number game!")
    print("I have selected a number between 1 and 100.")
    
    while not guessed_correctly:
        try:
            guess = int(input("Please enter your guess: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
            
if __name__ == "__main__":
    guess_the_number()