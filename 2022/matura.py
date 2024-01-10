import random
# s = 'baabbaaab' #aababb
a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
k = 1
def myFn(s: str):
    k = 1
    for x in range(len(s)):
        if s[x] == 'a':
            a[x] = a[x - 1] + 1
        else:
            a[x] = a[x - 1]

    for x in range(len(s) - 1, 0, -1):
        if s[x] == 'b':
            b[x] = b[x+1] + 1
        else: 
            b[x] = b[x+1]

    for x in range(len(s)):
        if a[x] + b[x+1] > k:
            k = a[x] + b[x+1]
    
    if k == 10:
        print(k)
        print(s)
        return True
    else: return False


# check = False
# while check == False:
#     s = ''
#     for x in range(10):
#         res = random.randint(0,1)
#         if res == 0: s += 'a'
#         else: s += 'b'
#     print(s)
#     if myFn(s):
#         check = True
    
def algo(n: int):
    s = 0
    for x in range(1, n):
        for x in range(1, n):
            s = s + 1
    print(s)

print(int('132', 4) + int('3111', 4))
print(int('1111011', 2))
print(int('362', 8))
print(15*16+3)
print(int('3303', 4))
    

