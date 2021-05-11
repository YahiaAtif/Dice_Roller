import random

while True:

    dice = random.randint(1, 6)

    def rool_the_dice(dice):
        switcher = {
            1: "[     ]\n[  0  ]\n[     ]",
            2: "[0    ]\n[     ]\n[    0]",
            3: "[0    ]\n[  0  ]\n[    0]",
            4: "[0   0]\n[     ]\n[0   0]",
            5: "[0   0]\n[  0  ]\n[0   0]",
            6: "[ 0 0 ]\n[ 0 0 ]\n[ 0 0 ]"
        }
        return switcher.get(dice)

    print(rool_the_dice(dice))

    Answer = input("Do you want to roll the dice again(y/n)? ")
    if Answer != 'y':
        exit(0)