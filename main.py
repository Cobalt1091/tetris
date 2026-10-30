#!/usr/bin/python3
import time
import os
import threading
import keyboard
"""
O: 0
I: 1
S: 2
Z: 3
L: 4
J: 5
T: 6
"""
def translate(x, y):
    return(f"[{y}][{x+1}]")

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def keyboardListen(x):
    if keyboard.is_pressed('left'):
        return(x-1)
    elif keyboard.is_pressed('right'):
        return(x+1)


class Block:
    def __init__(self, blockType):
        self.blockType = blockType
        match self.blockType:
            case 0:
                self.shape1Mask = [[1, 1, 0, 0], [1, 1, 0, 0]]
                self.shape2Mask = [[1, 1, 0, 0], [1, 1, 0, 0]]
                self.shape3Mask = [[1, 1, 0, 0], [1, 1, 0, 0]]
                self.shape4Mask = [[1, 1, 0, 0], [1, 1, 0, 0]]

            case 1:
                self.shape1Mask = [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
                self.shape2Mask = [[1, 1, 1, 1]]
                self.shape3Mask = [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
                self.shape4Mask = [[1, 1, 1, 1]]

            case 2:
                self.shape1Mask = [[0, 1, 1, 0], [1, 1, 0, 0]]
                self.shape2Mask = [[1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0]]
                self.shape3Mask = [[0, 1, 1, 0], [1, 1, 0, 0]]
                self.shape4Mask = [[1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0]]

            case 3:
                self.shape1Mask = [[1, 1, 0, 0], [0, 1, 1, 0]]
                self.shape2Mask = [[0, 1, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0]]
                self.shape3Mask = [[1, 1, 0, 0], [0, 1, 1, 0]]
                self.shape4Mask = [[0, 1, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0]]

            case 4:
                self.shape1Mask = [[1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0]]
                self.shape2Mask = [[1, 1, 1, 0], [1, 0, 0, 0]]
                self.shape3Mask = [[1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]
                self.shape4Mask = [[0, 0, 1, 0], [1, 1, 1, 0]]

            case 5:
                self.shape1Mask = [[0, 1, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
                self.shape2Mask = [[1, 0, 0, 0], [1, 1, 1, 0]]
                self.shape3Mask = [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
                self.shape4Mask = [[1, 1, 1, 0], [0, 0, 1, 0]]

            case 6:
                self.shape1Mask = [[0, 1, 0, 0], [1, 1, 1, 0]]
                self.shape2Mask = [[1, 0, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0]]
                self.shape3Mask = [[1, 1, 1, 0], [0, 1, 0, 0]]
                self.shape4Mask = [[0, 1, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0]]
        self.blank = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
               
class Screen:
    def __init__(self):
        self.size = [10,20]
        self.output = [
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],

        ]
    def display(self):
        for i in self.output:
            for j in i:
                if j == 1:
                    print("[]", end="")
                elif j == 0:
                    print("  ", end="")
                elif j == 2:
                    print("[", end="")
                elif j == 3:
                    print("]")
    def place(self, blockMask, x, y):
        for row, i in enumerate(blockMask):
            for col, j in enumerate(i):
                screenY = row + y
                screenX = col + 1 + x

                if (0 <= screenY < len(self.output) and
                    0 <= screenX < len(self.output[screenY]) - 1):
                    self.output[screenY][screenX] = j
    def moveBlockDown(self, blockMask, blank, y):
        i = 0

        while i <= len(self.output) - len(blockMask):
            self.place(blockMask, y, i)

            clearTerminal()
            screen.display()

            time.sleep(0.2)

            self.place(blank, y, i)
            i += 1

        # Display the final position
        self.place(blockMask, y, i - 1)
        clearTerminal()
        self.display()
    def clearDatThang(self):
        countI = 0
        for i in self.output:
            countJ = 0
            for j in i:
                if j == 1:
                    self.output[countI][countJ] = 0

                countJ += 1
            countI += 1


# Main gameloop
screen = Screen()
block1 = Block(2)

for i in range(7):
    exec(f"block{i} = Block({i})")
    y = 0
    for j in range(4):
        thread1 = Threading.thread(target=keyboardListen, args=(y))
        exec(f"screen.moveBlockDown(block{i}.shape{j + 1}Mask, block{i}.blank, {})")
        
        screen.clearDatThang()









