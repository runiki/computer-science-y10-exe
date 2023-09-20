num_peo = int(input("Type the amount of people"))
heights = []
for n in range(0,num_peo):
    a = int(input("Height?"))
    heights.append(a)

total = 0
smallest = heights[0]
for n in range(0, len(heights)):
    total = total+heights[n]
    if heights[n] < smallest:
        smallest = heights[n]
average = total / num_peo
print ("The average is", average)
heights.sort()
balls = heights[0]
balls2 = heights[-1]
print ("The range is", balls2 - balls)

