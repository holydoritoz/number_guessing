import random
from replit import clear
from art import logo

ramdon_number=random.randint(1,100)

def easy():
    global difficulty
    attempts=10
    while difficulty == 'easy' and attempts > 0 and attempts <= 10:
        guess=int(input('Make a guess: '))
        if guess == ramdon_number:
            print(f"You got it. It's {ramdon_number}")
        elif guess < ramdon_number:    
            attempts -=1 
            print(f'Too low, you got left {attempts} attempts')
        elif guess > ramdon_number:
            attempts -=1 
            print('Too high, you got left {attempts} attempts')
    else:
        print(f'You lose! You have: {attempts} attempts')
        

def hard():
    attempts=5
    global difficulty
    while difficulty=='hard' and attempts > 0 and attempts <= 5:
        guess=int(input('Make a guess: '))
        if guess == ramdon_number:
            print(f"You got it. It's {ramdon_number}")
        elif guess < ramdon_number:    
            attempts -=1 
            print(f'Too low, you got left {attempts} attempts')
        elif guess > ramdon_number:
            attempts -=1 
            print('Too high, you got left {attempts} attempts')
    else:
        print(f'You lose! You have: {attempts} attempts')

print(logo)
print("I'm thinking of a number between 1 and 100")
difficulty=input('Choose a difficulty. Type "easy" or "hard": ')
if difficulty == 'easy':
    easy()
else:
    hard()

