import random
import time
ran = random.randint(1, 20)
print('Try to guess the number!')
print("The number I'm thinking about is between 1 and 20")
time.sleep(0.10)

input1 = int(input())
if input1 > ran:
    print('The number that i think about is lower than', input1)
    print("You have 2 chances left!")

if input1 < ran:
    print("The number that i think about is higher than", input1)
    print("You have 2 chances left!")

if input1 == ran:
    print('The number was', ran)
    print("You win!")
    time.sleep(2)
    exit()

time.sleep(0.10)

input2 = int(input())
if input2 > ran:
    print('The number that i think about is lower than', input2)
    print("You have 1 chance left!")

if input2 < ran:
    print("The number that i think about is higher than", input2)
    print("You have 1 chance left!")

if input2 == ran:
    print('The number was', ran)
    print("You win!")
    time.sleep(2)
    exit()

time.sleep(0.10)

input3 = int(input())
if input3 != ran:
    print('The number was', ran)
    print("You lose!")
    time.sleep(2)
    exit()

if input3 == ran:
    print('The number was', ran)
    print("You win!")
    time.sleep(2)
    exit()
