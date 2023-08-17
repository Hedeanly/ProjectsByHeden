from random import randint
#create a list of play options
t = ["rock", "paper", "scissors"]
#assign a random play to computer
computer = t[randint(0,2)]
#set player to false
player = False

while player == False:
    player = input("rock,paper,scissors?: ")
    if player == computer:
        print("Tie")
    elif player == "rock":
        if computer == "paper":
            print("you lose!", computer, "covers", player)
        else:
            print("u win!", player, "smashes", computer)
    elif player == "paper":
        if computer == "scissors":
            print("u lose!", computer, "cut", player)
        else:
            print("u win", player, "cover", computer)
    elif player == "scissors":
        if computer == "rock":
            print("u lose", computer, "smashes", player)
        else:
            print("u win", player, "cut", computer)
    else:
        print("invalid play, check spelling")
    #player set to true
    player = False
    computer = t[randint(0,2)]
