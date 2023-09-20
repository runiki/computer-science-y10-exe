a = input("Type in the current date in the DD/MM/YYYY format. For example, 09/08/2023")
b = input("Type in your birthday in the DD/MM/YYYY format. For example, 09/08/2023, I will tell you your age")
c = int(a[0:2])
d = int(a[3:5])
e = int(a[6:10])
c1 = int(b[0:2])
d1 = int(b[3:5])
e1 = int(b[6:10])
if e>e1:
    if d>d1:
        if c1>c:
            print(e - e1 + 1)
    if d1>d:
        if c>c1:
            print(e - e1 - 1)
    if d==d:
        if c>c1:
            print(e - e1 - 1)
        if c1>c:
            print(e-e1+1)
        
elif e==e1:
    print ("0")
