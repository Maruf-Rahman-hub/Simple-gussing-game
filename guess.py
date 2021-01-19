import random
num = random.randint(1 , 10)
for i in range(3):
    guess = int(input("Enter a number :"))
    if guess > num:
        print("Sorry your number is greater!")
    elif guess < num:
        print("Sorry your number is lower!")
    else:
        print("You are correct")        