num_peo = int(input("Type the number of people"))

heights=[]

for x in range(num_peo):
    height = int(input("Height?"))
    heights.append(height)

even_sum = 0
for height in heights:
    if height % 2 == 0:
        even_sum = even_sum + height
print (even_sum)
