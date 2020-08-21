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
    secret_number = rd.randint(1, 21)
    guess_count = 1
    time_left = 5
    while guess_count <= 5:
        try:
            guess= int(input('Guess: '))
            just_display_time_left = time_left-1
            if guess > secret_number:
                prompt(just_display_time_left)
            elif guess < secret_number:                
                prompt(just_display_time_left, greater= False)
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