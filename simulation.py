import numpy as np
from time import sleep
import sys


def decToBin(n):
    # convert decimal to binary
    return bin(n).replace("0b", "").zfill(8)


ruleNumber = int(sys.argv[1])
lineSize = int(sys.argv[2])

rules = np.array(list(decToBin(ruleNumber)))[::-1]

# define the initial state
state = np.zeros(lineSize, int)
nextState = np.zeros(lineSize, int)
middleState = int(lineSize/2)
state[middleState] = 1

# # define the number of cells
cells = len(state)


states = ['⬛', '⬜']


def getNextState(l, c, r):
    index = int(str(l) + str(c) + str(r), 2)
    return int(rules[index])


while True:
    sleep(0.2)

    for i in range(cells):
        print(states[state[i]], end='')
        nextState[i] = getNextState(
            state[(i-1) % cells], state[i], state[(i+1) % cells])
    print('')
    state = nextState.copy()

