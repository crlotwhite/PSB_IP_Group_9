import random

from random import randint

randomInt = random.randint(1, 25)

userExp = 0
opponentExp = 0

def UserAction(choice):

choice = vars(input('Enter your choice (attack or heal):'))
 

if (choice == attack):
    Target = vars(input('Select your target:'))

    if (Target == Warrior):
        attackInt = randomInt
        defendInt = random.radiant (1, attackInt) #Since the defendInt should not be higher than the actual attackInt
        attackSum = attackInt - defendInt
        userExp += attackSum
        opponentExp += defendInt


    elif (Target == Tanker):
        attackInt = randomInt
        defendInt = random.radiant (1, attackInt)
        attackSum = attackInt - defendInt
        userExp += attackSum
        opponentExp += defendInt



    else (print('Error, please select a valid target.'))

elif (choice == heal):
    Heal()

else (print('Error, in your choice, write it correctly.'))