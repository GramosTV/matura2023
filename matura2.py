# f(n):
#  jeśli n<5 wykonaj dwie instrukcje:
#  f(n+1)
#  wypisz(n-1)
# 1.2 -> 1
#
def f(n):
    if n < 5:
        f(n+1)
        print(n-1)
# f(1)

# print(int('222', 3) > int('121', 6))
# print(int('222', 3) == int('10', 11))
# print(int('222', 3) > int('11', 10))
# print(int('222', 3) < int('121', 4))

# ANY BASE TO DECIMAL       
# number*base^place

# DECIMAL TO ANY BASE
# number/base = x
# x/base
# PLACE REMAINDER FROM BOTTOM TO TOP
        
def checkIfPalindron(word: str):
    reversed = list(word)
    reversed.reverse()
    return list(word) == reversed


def palindrons():
    file = open('slowa.txt', 'r').readlines()
    amount = 0
    families = []
    for i, x in enumerate(file):
        file[i] = file[i].split('\n')[0]
    for x in file:
        flag = True
        if checkIfPalindron(x):
            amount += 1
            if len(families) == 0:
                families.append({'length': len(x), 'palindrons': [x]})
                flag = False
            else:
                for i, y in enumerate(families):
                    if y['length'] == len(x):
                        flag = False
                        families[i]['palindrons'].append(x)
            if flag:
                families.append({'length': len(x), 'palindrons': [x]})
    for i, x in enumerate(families):
        families[i]['palindrons'] = sorted(families[i]['palindrons'])
    f = open("rodziny.txt", "w")
    for x in families:
        f.write('Rodzina ' + str(x['length'])+ ": ")
        for y in x['palindrons']:
            f.write(y + " ")
        f.write('\n') 
    print(families)
# palindrons()

def pesel():
    