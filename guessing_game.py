import random as rd
from concurrent.futures import ThreadPoolExecutor


def prompt(just_display_time_left: int, greater: bool=True):
    """
        Prompt message to user so as to get a clue of the secret number,
    """
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

def prompt_timeleft(time: int):
    """
        Prompting the user time left for the guessing
    """
    if time != 0:
        print(f"Time left is {time}")
    else:
        pass

def _to_continue():
    """
        After making a mistake, user will be asked 'Do you want to continue [Y|N]?'
    """
    asn = input('You want to continue [Y|N]? ').lower().startswith('y')
    return asn


def guessingFuc():
    """
        GAME!\n
        This contains all the process used for the guessing game which include:
        * Secret Number
        * Time of execution
    """
    secret_number = rd.randint(1, 21)  # This is the secret number which is between 1-20
    set_time = 5  # This is the number of time to guess (Which we can change and it will not affect the program)
    guess_count = 1  # Counting the guessing count
    time_left = set_time  # Time left to guess
    while guess_count <= set_time:
        try:
            just_display_time_left = time_left-1  # This is only useful for the prompt method and the time-left
            guess_count += 1 # Guess count
            guess = int(input('Guess: ')) # Guess here
            if guess > secret_number:
                prompt(just_display_time_left)
            elif guess < secret_number:                
                prompt(just_display_time_left, greater=False)
            else:
                break            
            prompt_timeleft(just_display_time_left)
            time_left -= 1
        except ValueError:
            print('Invalid pin')            
            if _to_continue():
                pass
            else:
                break
            prompt_timeleft(just_display_time_left)  
            time_left -= 1
    if secret_number == guess:
        print('You Won!')
    else:        
        print(f'The secret number is {secret_number}'
        f'\nYou lose!\n')


def main():
    """
        Game order of re-running falls here.
    """
    rerun()
    while True:
        play = input("Do you want to play again? [Y/N] ").capitalize().startswith('Y')
        if play:
            rerun()
        else:
            break


def game():
    """
        Guessing Game start here,
    """
    print(f"Hello! " 
    f"I have number between 1-20 \n"
    f"Can you guess my number? \n"
    f"Best of luck!")
    main()


if __name__ == "__main__":
    game()
