from random import randint

def choose_state(userMaxAtk, userLowestHp, aiLowestHp):
    chance = 0 # the higher the chance value, the higher chance to heal
    choose = ""

    if aiLowestHp = 100:
        choose = "attack"
    elif aiLowestHp > 85:
        chance += 2
    elif aiLowestHp > 50:
        chance += (100 - aiLowestHp)

    if aiLowestHp < userMaxAtk:
        chance += 25
    elif aiLowestHp == userMaxAtk:
        chance += 15
    elif aiLowestHp > userMaxAtk:
        chance += 5

    if userLowestHp >= 20:
        chance += userLowestHp


    random = randint(1, 130) # the 130 value is the maximum bias level
    if random <= chance:
        choose = "heal"
    else:
        choose = "attack"

    return choose
