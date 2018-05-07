import random
import time
print("I will flip a coin 1000 times. Guess No of times heads show up")
input()
flips = 0
heads = 0

while(flips < 1000):
    if(random.randint(0,1) == 1):
        heads +=1
    flips +=1
    if(flips == 900):
        print('900 flips and there have been' + str(heads) + 'heads')
        time.sleep(2)
    if(flips == 100):
        print('100 flips and there have been' + str(heads) + 'heads')
        time.sleep(2)
    if(flips == 500):
        print('500 flips and there have been' + str(heads) + 'heads')
        time.sleep(2)

print()
print('Out of 1000 coin tosses: ')
print('\t','Heads came up: ',heads)
tails = (1000 - int(heads))
print('\t','Tails :', tails , '\n')
print('Were u close ?')