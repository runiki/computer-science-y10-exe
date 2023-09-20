phonenum = input("Type your phone number, remember to put spaces!")
result = phonenum.startswith("852")
n = len(phonenum)
if result:
    if n == 13:
        print("You have a Hong Kong phone number.")
elif phonenum == ("999"):
    print("Woah... you are the HK police")
else:
    print("You do not have a Hong Kong Phone number.")
