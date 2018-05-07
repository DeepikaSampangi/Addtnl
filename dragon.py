import random
import time

def displayIntro():
    print('You are in a land of dragons')
    time.sleep(2)
    print('''In front there r 2 caves, Choose one, One has a dragon and other is safe''', '\n')

def chooseCave():
    cave = " "
    while(cave != '1' and cave != '2'):
        print("Choose a Cave:(1 0r 2) ?  ")
        cave = input()
    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if(chosenCave == str(friendlyCave)):
        print('U get the treasure')
    else:
        print('Eats u off')

playAgain = 'yes'

while(playAgain == 'yes' or playAgain == 'y'):
    displayIntro()

    caveNumber = chooseCave()

    checkCave(caveNumber)

    print('Wanna Play again? (y or n): ')
    playAgain = input()