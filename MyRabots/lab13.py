width = 30
height = 12

for y in range(height, -1, -1):
    line = ""
    for x in range(width + 1):
        fx = x / 3
        
        if abs(fx - y) < 0.3:
            line += "*"
       
        elif x == 0 and y == 0:
            line += "+"
        elif x == 0:
            line += "|"
        elif y == 0:
            line += "-"
        else:
            line += " "
    print(line)
