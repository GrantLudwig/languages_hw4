#hw4.py v1.0
#Grant Ludwig
#5/8/19

import sys
from functools import reduce

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

#Computes the greatest common denominator
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

#Simplifies a fraction
def simplify(fraction):
    num, den = fraction
    if num == 0:
        den = 1
    elif abs(num) == den:
        num = int(abs(num)/num)
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
target = (int(sys.argv[2]), int(sys.argv[3]))
try:
    fractionList = createFractionList(fileName)
except FileNotFoundError:
    print('File could not be found')
    sys.exit()
except InvalidFile:
    print('Invalid file')
    sys.exit()
print(fractionList)
#Simplify fractions
simFractions = [simplify(fraction) for fraction in fractionList]
print(simFractions)
##TODO Generator
#for output in genDifferences(fractionList, target):
    #print(output)
#Decimal Fractions
decimalValues = list(map((lambda x: x[0] / x[1]), fractionList))
print(decimalValues)
#Double Fractions
doubledFractions = list(map((lambda x: simplify((x[0]*2, x[1]))), fractionList))
print(doubledFractions)
#Fractions greater than target
filterList = list(filter((lambda x: x[0]/x[1] > target[0]/target[1]), fractionList))
print(filterList)
#Minimum Fraction
print(reduce(lambda x, y: x if x[0]/x[1] < y[0]/y[1] else y, fractionList))
#Sum of fractions (in simpliest form)
print(reduce(lambda x, y: simplify((x[0]*y[1] + y[0]*x[1],x[1]*y[1])), fractionList))