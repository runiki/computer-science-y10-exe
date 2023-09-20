a = input("Type a sentence")
n = a.find(" ")
n2 = a.find(" ", n + 1)
e = (a[n:n2])
b = e.capitalize()
print (b) 


