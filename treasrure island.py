print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# welcome to treasure island 
print("welcome to treasure island.")
print("your mission is to find the treasure.")
# the user have the choice to move left or right
choice1= input('you\'ve at a cross road. Where do you want to go? Type "left"  or "right": ').lower()
if choice1 >= "left":
    print ("You walk down the path on your left and come across a cave. You enter it")
    choice2 = input('you\'ve come to lake. There is a island at the middle of the lake. Type "wait" to wait for boat or type "swim" to swim across. ').lower()
    if choice2 >= "wait":
        choice3 = input("you have reached the island unharmed . There is a house with 3 doors. One red, one yellow , one blue. Which colour do you choose ?").lower()
        if choice3 == "red":
            print("It is a room full of fire. Game over. ")
        elif choice3 == "yellow":
            print("You found the treasure. You win the game !")
        elif choice3 == "blue":
            print("you enter the room of beasts . Game over")
        else:
            print("you choose a door that dont exist game over")

    else:
        print("you got attacked by angry trout. Game over")
else:
    print("you fell into hole. Game over")