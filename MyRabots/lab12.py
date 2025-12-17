import math

radius = 10
aspect_ratio = 0.5  
size = 25

for y in range(size):
    for x in range(size):
        center_x = size // 2
        center_y = size // 2
        
        dx = x - center_x
        dy = (y - center_y) / aspect_ratio
        
        distance = math.sqrt(dx**2 + dy**2)
        
        if abs(distance - radius) < 0.7:
            print("●", end="")
        else:
            print(" ", end="")
    print()