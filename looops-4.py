number = int(input("Type a number!"))
fibo2 = 1
fibo = 0
n = 0
while n==0:
    fibo = fibo + fibo2
    fibo2 = fibo + fibo2
    fet = fibo + fibo2
    if fet>=number:
        print(fet)
        n = 1