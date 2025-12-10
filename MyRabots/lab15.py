import os
import time

frames = [
    "◯      ",
    "  ◯    ",
    "    ◯  ",
    "      ◯"
]

while True:
    for f in frames:
        os.system("cls")  # для Windows, для Linux заменить на clear
        print(f)
        time.sleep(0.2)
