import random

computer =random.choice(["snake","water","gun"])

player=input("enter your choice(snake,water,gun):")
def game(player):
    if computer==player:
        print("this match is draw")
    else:
        if computer=="water" and player=="gun":
            print("computer won this match.")
        elif computer=="gun" and player=="snake":
            print("computer won this match.")
        elif computer=="snake" and player=="water":
            print("computer won this  match.")
        elif computer=="water" and player=="snake":
            print("player won this match.")
        elif computer=="gun" and player=="water":
            print("player won this match.")
        elif computer=="snake" and player=="gun":
            print("player won this match.")
        else:
            print("somthing wrong.")
print(f"computer={computer} and player={player}  ")
game(player)