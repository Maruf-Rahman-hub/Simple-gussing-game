import random
User = input("Enter Your name: ")
print(f"Hello {User} welcome to a guess game\n!!!WISH YOU  BEST OF LUCK!!! \n****************************")
comp = random.randint(1,10) 
for i in range(3):
    player = int(input("Enter a number between 1 to 10: "))
        
    if player == comp:
        print(f"You gussed correct number.computer chose {comp}")
        break#if the user entered a correct num it will break the loop
    elif player > comp:
        print(f"You gussed uncorrect number,number is lower than {player}")
    elif player < comp:
        print(f"You gussed uncorrect number,number is higher than {player}") 
print(f"the number was {comp}")
            
