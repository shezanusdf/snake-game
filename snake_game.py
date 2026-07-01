import msvcrt
import time 
import random

positions = [["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],]

snake = "🟩"
apple = "🍎"
# starting pos
row = 2
col = 2

# target pos
x = random.randint(0,9)
y = random.randint(0,9)

def main():
    global row, col
    DIRECTION = "RIGHT"
    drawBoard()
    positions[x][y] = apple
    while True:
        if msvcrt.kbhit():
            DIRECTION = take_input()
        move_direction(DIRECTION)
        positions[row][col] = snake
        drawBoard()
        if row == x and col == y:
            print("You won!")
            break
    

        time.sleep(0.2)


def drawBoard():
    print("------------------------")
    for i in range(10):
        print("|", "".join(positions[i]), "|") 
    print("------------------------")

def take_input():
    if msvcrt.kbhit():
        key = msvcrt.getch()

        if key == b'w':
            return "UP"
        if key == b's':
            return "DOWN"
        if key == b'd':
            return "RIGHT"
        if key == b'a':
            return "LEFT"
    return "RIGHT"

def move_direction(DIRECTION):
    global row, col

    positions[row][col] = "  "

    if DIRECTION == "UP" and row > 0:
        row -= 1
    elif DIRECTION == "UP" and row == 0:
        row = (len(positions) - 1)
    elif DIRECTION == "DOWN" and row < (len(positions) - 1):
        row += 1
    elif DIRECTION == "DOWN" and row == (len(positions) - 1):
        row = 0
    elif DIRECTION == "LEFT" and col > 0:
        col -= 1
    elif DIRECTION == "LEFT" and col == 0:
        col = (len(positions[row]) - 1)
    elif DIRECTION == "RIGHT" and col < (len(positions[row]) - 1):
        col += 1
    elif DIRECTION == "RIGHT" and col == (len(positions[row]) - 1):
        col = 0



if __name__ == "__main__":
    main()
