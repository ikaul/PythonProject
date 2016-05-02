#!/usr/bin/python
def metroCard(lastNumberOfDays):
    numDaysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
    numPossibilities = []
    for i in range(12):
        if lastNumberOfDays == numDaysInMonth[i]:
            x = i + 1
            x = x % 12
            numPossibilities.append(numDaysInMonth[x])
    numPossibilities = set(numPossibilities)
    return list(numPossibilities)

print metroCard(30)
print metroCard(31)
print metroCard(28)
