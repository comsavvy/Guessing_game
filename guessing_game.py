import random as rd
from functools import wraps
from concurrent.futures import ThreadPoolExecutor
from typing import Tuple, Literal


def thread(func):
    """
        Threading the game here
    """
    @wraps(func)
    def inner_func(*args: Tuple, **kwargs: int):
        with ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(func, *args, **kwargs)
    return inner_func


def prompt(just_display_time_left: int, greater: bool=True):
    """
        Prompt message to user so as to get a clue of the secret number,
    """
    if greater:
        if just_display_time_left != 0:
            print('Too long, try again!')
        else:
            print(f'{"="*8}\nToo long\n{"="*8}\n')
    else:
        if just_display_time_left != 0:
            print('Too small, try again!')
        else:
            print(f'{"="*9}\nToo small\n{"="*9}\n')

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


@thread
def game_guessing(secretNo: Tuple=(1, 20), time: int=5) -> None:
    """
        GAME!\n
        This contains all the process used for the guessing game which include:
        * Secret Number
        * Time of execution
    """
    secret_number = rd.randint(*secretNo)  # This is the secret number which is between the specified number
    set_time = time  # This is the number of times to guess (Which we can change and it will not affect the program)
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
        print(f'{"="*8} You Won! {"="*8}\n')
    else:        
        print(f'The secret number is {secret_number}\n'
        f'\n{"="*9} You lose! {"="*9}\n')


def main():
    """
        Game order of re-running falls here.
    """
    secret_number = (1, 30) # Modifying the secret number
    time = 7 #  Changing the time of guess
    print(f"Hello! " 
        f"I have number between {secret_number[0]}-{secret_number[1]} \n"
        f"Can you guess my number? \n"
        f"Best of luck!")    
    game_guessing(secret_number, time)
    while True:
        play = input("Do you want to play again? [Y/N] ").capitalize().startswith('Y')
        if play:
            game_guessing(secret_number, time)
        else:
            break


if __name__ == "__main__":
    main()
