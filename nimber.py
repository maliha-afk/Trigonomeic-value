import random
computer_number=random.randint(1,20)
chance=5
def clue():
    if computer_number>10:
        print("hidden number is greater than 10")
    elif computer_number<10:
        print("hidden number is less than 10")


while True:
    my_number=int(input("guess a number: "))
    if my_number == computer_number:
        print("hurray! you gussed it right!")
        break
    
    if my_number!=computer_number:
        chance=chance-1
        print(f"you have {chance} chances left")
        clue2=input("Do you want any clue? Y/N: ")
        
        if chance==0:
          print("game over!")
          break
        
        elif clue2=="Y":
            clue()
        
        elif clue2 == "N":
            print ("okay")
            
         