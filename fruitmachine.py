# Fruit Machine
from random import choice

# symbols
symbols = ['Cherry','Lemon','Bell','Skull','Orange','Star']

# money
dollars = 1
cents = 0

play = input("do you want to play? (y,n) ")

while play == "yes" or play == "y":

    # three rollers
    roller1 = choice(symbols)
    roller2 = choice(symbols)
    roller3 = choice(symbols)

    print("you rolled:")
    print(roller1,roller2,roller3)

    play = input("do you want to play? (y,n) ")
