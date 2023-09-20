date = input("Type in your birthdate in the form of DD/MM/YY for e.g, 09/02/2015")
name = input("Now type in your name")
date2 = input("Type the birthdate of another person in the form of DD/MM/YY")
name2 = input("Now type in the name of this second person")
d = date[0:2]
m = date[3:5]
y = int(date[6:10])
d2 = date2[0:2]
m2 = date2[3:5]
y2 = int(date2[6:11])
result2 = y >= y2
if y > y2:
    print(f"{name} is older than {name2}!")
elif y2 > y:
    print(f"{name2} is older than {name}!")
elif y2 == y:
    if m2==m:
        if d2>d:
            print(f"{name} is older than {name2}!")
        if d>d2:
            print(f"{name2} is older than {name}!")
        if d==d2:
            print("Woah... you both have the same birthday!")
    if m2 > m:
        print(f"{name} is older than {name2}!")
    if m > m2:
        print(f"{name2} is older than {name}!")






    
        

