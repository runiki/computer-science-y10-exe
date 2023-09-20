import random
import sys
from colorama import Fore
print(Fore.RED)
print ("Lets play a game!")
print(Fore.BLUE)
print("There shall be four doors, with ten rounds.")
print(Fore.GREEN)
print("One has a ghost, while the other three shall be safe.")
print(Fore.YELLOW)
print(Fore.BLUE)
print("You may peek through one of the doors by saying 'Peek'. However, you can only peek twice")
print("Good luck, and have fun.")
print(Fore.RED)
beginTF = input("Type I BEGIN to start the game.")

if beginTF == "I BEGIN":
    print(Fore.GREEN)
    print ("The game has begun. Be ready.")
    n = 10
    peek = 3
    
    for x in range(n):
        x = x+1
        doors = ("Round",x)
        print(Fore.RED)
        print (doors)
        doorlist = ["1","2","3","4"]
        ghost_door = int(random.choice(doorlist))
        chosen_door = input("Type in a door number 1 or 2 or 3 or 4, or 'Peek'")
        
        try:
            chosen_door = int(chosen_door)
        except ValueError:
            if chosen_door != "Peek":
                print ("Invalid input... Bye & Don't cheat bro" )
                sys.exit()
                
        if chosen_door == "Peek":
            chosen_door = 5
            print(Fore.BLUE)
            print ("The door with the ghost is door", ghost_door)
            print ("You peeked at the door and successfully avoided the ghost")
            peek = peek-1
            
            if chosen_door != ghost_door or chosen_door == "peek":
                print(Fore.YELLOW)
                print ("Next door...")
                
        if peek == 0:
            print ("You have already surpassed your peak limit. Do not cheat. BYE BYE!")
            sys.exit()
            
        if chosen_door == ghost_door:
            print(Fore.BLUE)
            print ("Your fate has chosen the wrong door...")
            sys.exit()
            
    if x == 10:
        print ("GG!!! You have defied all odds and won the game!")
        
else:
    print(Fore.BLUE)
    print ("Ok scaredy-cat. ")