num_peo = int(input("Type the amount of people"))
heights = []
for n in range(0,num_peo):
    a = int(input("Height?"))
    heights.append(a)
heights.sort()
size = len(heights)
if size%2 == 1:
    bob = size//2
    he1 = heights[bob]
    print("The median of people is", he1)
if size == 0:
    he1 = heights[0]
    print("The median of people is", he1)
if size%2 == 0:
    bob = size//2
    bob2 = bob-1
    bobby1 = heights[bob]
    bobby2 = heights[bob2]
    d = bobby2+bobby1
    e = d//2
    print ("The median of people is",e)