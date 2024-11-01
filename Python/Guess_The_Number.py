import random
import time

def Game():
    
    print("Let's play! I'm going to think of a number and you have to guess it.")
    time.sleep(3)
    print("What range of numbers do you want me to choose from?")
    Num1 = int(input("Number 1: "))
    Num2 = int(input("Number 2: "))
    
    Number = random.randint(Num1, Num2)

    Attempts = int(input("How many attempts do you want?: "))
    
    print(f"Let’s get started! You have {Attempts} attempts to guess.")
    time.sleep(1)
    for x in range(Attempts):
        UserNum = int(input("What number am I thinking of?: "))
    
        if UserNum == Number:
            print("Great! You guessed it!")
            PlayAgain()
            return
        else:
            Attempts -= 1
            print(f"I'm not thinking of that number; you have {Attempts} attempts left.")
            time.sleep(2)
            Hint = input("Do you want a hint? (yes/no) ")
            
            if (Hint.lower() == "yes") and (Number > UserNum):
                print("The number I'm thinking of is higher than the number you said...")
            elif (Hint.lower() == "yes") and (Number < UserNum):
                print("The number I'm thinking of is lower than the number you said...")
            else:
                print("Alright, let’s continue.")
            
    while (Attempts == 0):
        
        print(f"The number was {Number}!")
        
        VJ = input("Do you want to play again? (yes/no) ")
    
        if (VJ.lower() == "yes"):     
            Game()
        else:
            print("Thanks for playing!")
            break
            
def PlayAgain():
        
    VJ = input("Do you want to play again? (yes/no) ")
    
    if (VJ.lower() == "yes"):     
        Game()
    else:
        print("Thanks for playing!")
    return

Game()
