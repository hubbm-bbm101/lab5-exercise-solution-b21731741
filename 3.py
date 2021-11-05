import random
randomNumber = random.randint(1,100)
while True:
    inputNumber = int(input("Give me a number between 1 AND 100!"))
    if inputNumber == randomNumber:
        print("You win!")
        break
    if inputNumber < randomNumber:
        print("Increase your number!")
    else:
        print("Decrease your number")
