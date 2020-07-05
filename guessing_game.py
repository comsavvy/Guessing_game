import random as rd
def guessingFuc():
    secret_number= rd.randint(1, 21)
    guess_count= 1
    timeLeft= 5
    while guess_count <= 5:
        try:
            guess= int(input('Guess: '))
            justDisplayTimeLeft= timeLeft-1
            if guess > secret_number:
                if justDisplayTimeLeft is not 0: 
                    print('Too long, try again!')
                else:
                    print('Too long')
            elif guess < secret_number:                
                if justDisplayTimeLeft is not 0: 
                    print('Too small, try again!')
                else:
                    print('Too small')
            else:
                break
            guess_count += 1        
            if justDisplayTimeLeft is not 0:
                print(f"Time left is {justDisplayTimeLeft}")
            else:
                pass
            timeLeft= timeLeft-1
        except ValueError:
            print('Invalid pin')
        except TypeError:
            print('Invalid type!')
    if secret_number is guess:
        print('You Won!')
    else:
        print ('You lose!')
#Game start here
print("Hello! I have number between 1-20 \nCan you guess my number? \nBest of luck!")
if __name__ == "__main__":
    guessingFuc()
    while True:
        play= input("Do you want to play again? [Y/N] ").capitalize()
        if play=='Y' or play== 'Yes':
            guessingFuc()
        else:
            break
