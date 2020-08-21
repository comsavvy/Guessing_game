import random as rd
from concurrent.futures import ThreadPoolExecutor


def prompt(just_display_time_left, greater=True):
    if greater:
        if just_display_time_left != 0:
            print('Too long, try again!')
        else:
            print('Too long')
    else:
        if just_display_time_left != 0:
            print('Too small, try again!')
        else:
            print('Too small')


def guessingFuc():
    secret_number = rd.randint(1, 21)  # This is the secret number which is between 1-20
    guess_count = 1  # Counting the guessing count
    set_time = 5  # This is the number of time to guess (Which we can change and it will not affect the program)
    time_left = set_time  # Time left to guess
    while guess_count <= set_time:
        try:
            guess = int(input('Guess: '))
            just_display_time_left = time_left-1  # This is only useful for the prompt method and the time-left
            if guess > secret_number:
                prompt(just_display_time_left)
            elif guess < secret_number:                
                prompt(just_display_time_left, greater=False)
            else:
                break
            guess_count += 1        
            if just_display_time_left != 0:
                print(f"Time left is {just_display_time_left}")
            else:
                pass
            time_left = time_left-1
        except ValueError:
            print('Invalid pin')
            break
    if secret_number is guess:
        print('You Won!')
    else:
        print('You lose!')


def rerun():
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(guessingFuc)


def main():
    rerun()
    while True:
        play = input("Do you want to play again? [Y/N] ").capitalize().startswith('Y')
        if play:
            rerun()
        else:
            break


# Game start here
print("Hello! I have number between 1-20 \nCan you guess my number? \nBest of luck!")
if __name__ == "__main__":
    main()