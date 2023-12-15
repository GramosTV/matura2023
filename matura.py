#Pierwszy raz python xddd

# if x > 15:
#     print('maybe')
# elif x > 5:
#     print('ok')
# else:
#     print('yee')

# print('ok') if 10 > 15 else print('nah bro')

# print(type('123'))
# print(type(123))
# print(type(False))
# print(type([]))
# print(type(str))

# print(''' okay so? '''.strip())
# print('hello'.center(20, ' '))
# print(abs(-1))

# print(bin(67)[2:])
# print([*"123"])

#to lecimy

# 2023 zad 2 wszystkie oprocz 2.4
from datetime import datetime
from datetime import time
def binaryBlockSum(n: int):
    arr = [*bin(n)[2:]]
    currentValue = ''
    sum = 0
    for x in arr:
        if x != currentValue:
            sum += 1
            currentValue = x
    return sum

def binaryBlockSumStr(n: str):
    arr = [*n]
    currentValue = ''
    sum = 0
    for x in arr:
        if x != currentValue:
            sum += 1
            currentValue = x
    return sum

def countFile():
    file = open('bin_przyklad.txt', 'r').readlines()
    for index, value in enumerate(file):
        file[index] = value.split('\n')[0]
    sum = 0
    for x in file:
        if binaryBlockSumStr(x) <= 2:
            sum += 1
    print(sum)

def findBiggestNum():
    print(int('111', 2))

    file = open('bin_przyklad.txt', 'r').readlines()
    for index, value in enumerate(file):
        file[index] = value.split('\n')[0]
    biggestNum = 0
    for i, x in enumerate(file):
        if int(x, 2) > biggestNum:
            biggestNum = int(x, 2)
            winningIndex = i
    print(file[winningIndex])


def XOR (): 
    file = open('bin_przyklad.txt', 'r').readlines()
    for index, value in enumerate(file):
        file[index] = value.split('\n')[0]
    for i, x in enumerate(file):
        file[i] = bin(int(x, 2) ^ (int(int(x, 2)/2)))[2:]
    print(file)

# Matura 2023 zadanie 3

def piPairs():
    file = open('pi_przyklad.txt', 'r').readlines()
    sum = 0
    for i, x in enumerate(file):
        if (i + 1) != len(file) and int(file[i].split('\n')[0] + file[i+1].split('\n')[0]) > 90:
            sum += 1
    print(sum)

def piDictionaries():
    file = open('pi_przyklad.txt', 'r').readlines()
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    d = {}
    for i, x in enumerate(numbers):
        for element in numbers:
            d[x + element] = 0

    for i, x in enumerate(file):
        if (i + 1) != len(file):
            x = x.split('\n')[0]
            next = file[i+1].split('\n')[0]
            num = x + next
            d[num] += 1

    most = max(d.values())
    least = min(d.values())
    maxResult = None
    minResult = None
    for i, x in enumerate(d.items()):
        if x[1] == most:
            if maxResult is None or maxResult > x[0]:
                maxResult = x[0]
        elif x[1] == least:
            if minResult is None or minResult > x[0]:
                minResult = x[0]
    print(minResult)
    print(maxResult)

# piDictionaries()

def piSequences():
    file = open('pi_przyklad.txt', 'r').readlines()
    sum = 0
    for i, x in enumerate(file):
        file[i] = x.split('\n')[0]
    for i, x in enumerate(file):
        if i + 5 < len(file):
            sequence = [*x + file[i+1] + file[i+2] + file[i+3] + file[i+4] + file[i+5]]
            shouldBeBigger = True
            failed = False
            # repeated = False
            for i, x in enumerate(sequence):
                if i != len(sequence) - 1 and failed != True:
                    # if (x == sequence[i+1] and repeated): break
                    # if (x == sequence[i+1]): repeated = True
                    if shouldBeBigger:
                        if int(x) >= int(sequence[i+1]):
                            shouldBeBigger = False
                    else:
                        if int(x) > int(sequence[i+1]):
                            if i == len(sequence) - 2:
                                sum += 1
                                print(sequence)
                        else:
                            failed = True
                            
    print("Sum: %d" %sum)

#5
def baseToDecimal():
    number = input("Enter the number: ")
    from_base = int(input("Enter the source base: "))
    decimal_number = int(number, from_base)
    print(decimal_number)

#6

def jam():
    file = open('owoce.txt', 'r').readlines()[1:]
    arr = []
    dates = []
    for x in file:
        formatted = x.split('\t')
        obj = {
            "date": formatted[0],
            "raspberries": int(formatted[1]),
            "strawberries": int(formatted[2]),
            "currants": int(formatted[3].split('\n')[0])
        }
        
        arr.append(obj)
    for x in arr:
        if x['currants'] > x['strawberries'] and x['currants'] > x['raspberries']:
            dates.append(x['date'])
    print(len(dates))

def jamWithinDates():
    file = open('owoce.txt', 'r').readlines()[1:]
    arr = []
    currants = 0
    strawberries = 0
    raspberries = 0
    for x in file:
        formatted = x.split('\t')
        obj = {
            "date": datetime.strptime(formatted[0], "%d-%m-%Y"),
            "raspberries": int(formatted[1]),
            "strawberries": int(formatted[2]),
            "currants": int(formatted[3].split('\n')[0])
        }
        
        arr.append(obj)
    yesterdaysRaspberries = 0
    yesterdaysStrawberries = 0
    yesterdaysCurrants = 0
    rs = 0
    rc = 0
    sc = 0
    rsKg = 0
    rcKg = 0
    scKg = 0
    for x in arr:
        if (x['date'] >= datetime.strptime("2020-05-01", "%Y-%m-%d") and x['date'] <= datetime.strptime("2020-09-30", "%Y-%m-%d")):
            clone = x.copy()
            clone.pop('date')
            clone['raspberries'] += yesterdaysRaspberries
            clone['strawberries'] += yesterdaysStrawberries
            clone['currants'] += yesterdaysCurrants
            yesterdaysRaspberries = 0
            yesterdaysStrawberries = 0
            yesterdaysCurrants = 0
            sort = sorted(clone, key=clone.get)
            print(clone['raspberries'], clone['strawberries'], clone['currants'])
            if ((sort[2] == 'raspberries' and sort[1] == 'strawberries') or (sort[2] =='strawberries' and sort[1] == 'raspberries')):
                rs += 1
                yesterdaysCurrants += clone['currants']

                if sort[2] == 'raspberries':
                    yesterdaysRaspberries += clone['raspberries'] - clone['strawberries']
                    rsKg += clone['strawberries']
                elif sort[2] =='strawberries':
                    yesterdaysStrawberries += clone['strawberries'] - clone['raspberries']
                    rsKg += clone['raspberries']
            elif ((sort[2] == 'raspberries' and sort[1] == 'currants') or (sort[2] == 'currants' and sort[1] == 'raspberries')):
                rc += 1
                yesterdaysStrawberries += clone['strawberries']

                if sort[2] == 'raspberries':
                    yesterdaysRaspberries += clone['raspberries'] - clone['currants']
                    rcKg += clone['currants']
                elif sort[2] =='currants':
                    yesterdaysCurrants += clone['currants'] - clone['raspberries']
                    rcKg += clone['raspberries']

            elif ((sort[2] =='strawberries' and sort[1] == 'currants') or (sort[2] == 'currants' and sort[1] =='strawberries')):
                sc += 1
                yesterdaysRaspberries += clone['raspberries']

                if sort[2] == 'strawberries':
                    yesterdaysStrawberries += clone['strawberries'] - clone['currants']
                    scKg += clone['currants']
                elif sort[2] =='currants':
                    yesterdaysCurrants += clone['currants'] - clone['strawberries']
                    scKg += clone['strawberries']
    print(rsKg, rcKg, scKg)        
jamWithinDates()