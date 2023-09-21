line = "123"
line2 = "456"
line3 = "789"
one = 1
two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7
eight = 8
nine = 9
print ("The first player will be X")
print ("The second player will be O")
print (line)
print (line2)
print (line3)
n = 9
x = 1
for x in range(n):
    x = x+1
    move1 = int(input("Player 1's turn, type your number"))
    if move1 == one: 
        line = "X" + line[1:3]
    elif move1 == two:
        line = line[0:1]+"X"+line[2:3]
    elif move1 == three:
        line = line[0:2]+"X"
    elif move1 == four:
        line2 = "X"+line2[1:3]
    elif move1 == five:
        line2 = line2[0:1]+"X"+line2[2:3]
    elif move1 == six:
        line2 = line2[0:2]+"X"
    elif move1 == seven:
        line3 = "X"+line3[1:3]
    elif move1 == eight:
        line3 = line3[0:1]+"X"+line2[2:3]
    elif move1 == nine:
        line3 = line3[0:2]+"X"
    print (line)
    print(line2)
    print(line3)
    move2 = int(input("Player 2's turn, type your number"))
    if move2 == one: 
        line = "O" + line[1:3]
    elif move2 == two:
        line = line[0:1]+"O"+line[2:3]
    elif move2 == three:
        line = line[0:2]+"O"
    elif move2 == four:
        line2 = "O"+line2[1:3]
    elif move2 == five:
        line2 = line2[0:1]+"O"+line2[2:3]
    elif move2 == six:
        line2 = line2[0:2]+"O"
    elif move2 == seven:
        line3 = "O"+line3[1:3]
    elif move2 == eight:
        line3 = line3[0:1]+"O"+line2[2:3]
    elif move2 == nine:
        line3 = line3[0:2]+"O"
    print (line)
    print(line2)
    print(line3)