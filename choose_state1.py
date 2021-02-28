from random import randint

def choose_state(userMaxAtk, userLowestHp, aiLowestHp):
    bias = 0 # the higher the bias value, the higher chance to heal
    choose = ""

    if aiLowestHp = 100:
        choose = "attack"
    elif aiLowestHp > (100 - 15) and aiLowestHp != 100:
        bias += 2
    elif aiLowestHp <= (100 - 15) and aiLowestHp > 50:
        bias += (100 - aiLowestHp)

    if aiLowestHp < userMaxAtk:
        bias += 25
    elif aiLowestHp == userMaxAtk:
        bias += 15
    elif aiLowestHp > userMaxAtk:
        bias += 5

    if userLowestHp >= 20:
        bias += userLowestHp


    random = randint(1, 130) # the 130 value is the maximum bias level
    if random <= bias:
        choose = "heal"
    else:
        choose = "attack"

    return choose
