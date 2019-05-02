#hw4.py v1.0
#Grant Ludwig
#5/8/19

import sys

def readFile(fileName):
    firstLine = True
    pointerList = []
    blockList = []
    for line in open(fileName):
        line = line.rstrip()
        if firstLine:
            for _ in range(int(line)):
                blockList.append([])
            firstLine = False
        else:
            point, pointed = line.split(',')
            #if ValueError occurs, that means that the line is a pointer to a block
            try:
                blockList[int(point)].append(int(pointed))
            except ValueError:
                pointerList.append((point, int(pointed)))
    return (pointerList, blockList)

#Driver code
fileName = sys.argv[1]