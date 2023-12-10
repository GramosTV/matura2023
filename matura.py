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

    for x in file:
        formatted = x.split('\t')
        obj = {
            "date": formatted[0],
            "raspberries": formatted[1],
            "strawberries": formatted[2],
            "currants": formatted[3].split('\n')[0]
        }
        arr.append(obj)

    
    print(arr)
jam()