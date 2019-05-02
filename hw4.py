#hw4.py v1.0
#Grant Ludwig
#5/8/19

import sys

class InvalidFile(Exception): pass

def createFractionList(fileName):
    fracList = []
    for line in open(fileName):
        line = line.rstrip()
        fractionLine = line.split()
        if len(fractionLine) != 2:
            raise InvalidFile
        try:
            frac = (int(fractionLine[0]), int(fractionLine[1]))
        except ValueError:
            raise InvalidFile
        if frac[1] <= 0:
            raise InvalidFile
        fracList.append(frac)
    if fracList == []:
        raise InvalidFile
    return fracList

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def simplify(fraction):
    num, den = fraction
    if num == 0:
        den = 1
    elif abs(num) == den:
        num = abs(num)/num
        den = 1
    else:
        commonDiv = gcd(num,den)
        num = int(num/commonDiv)
        den = int(den/commonDiv)
    return (num, den)

#TODO
def genDifferences(fractionList, target):
    print('TODO')

#Driver code
fileName = sys.argv[1]
target = (sys.argv[2], sys.argv[3])
try:
    fractionList = createFractionList(fileName)
except FileNotFoundError:
    print('File could not be found')
    sys.exit()
except InvalidFile:
    print('Invalid file')
    sys.exit()
print(fractionList)
simFractions = [simplify(fraction) for fraction in fractionList]
print(simFractions)
#for output in genDifferences(fractionList, target):
    #print(output)
decimalValues = map((lambda x,y: x / y), fraction in fractionList)
print(decimalValues)
