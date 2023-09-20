import math
side = float(input("please input a side:"))
angle = float(input("Please input an angle"))
angle = math.radians(angle)
side2 = math.tan(angle) * side
area = 0.5 * side2 * side
print(area)
print (math.pi)