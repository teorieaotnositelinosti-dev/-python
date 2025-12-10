RED = "\033[41m"     
WHITE = "\033[47m"   
RESET = "\033[0m"

for row in range(11):
    line = ""
    for col in range(21):
        if (4 <= row <= 6) or (8 >= col >= 6 and 2 <= row <= 8):
            line += WHITE + "  " + RESET
        else:
            line += RED + "  " + RESET
    print(line)

