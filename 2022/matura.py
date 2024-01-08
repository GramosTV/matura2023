s = 'baabbaaab'
a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
k = 1
for x in range(len(s)):
    if s[x] == 'a':
        a[x] = a[x - 1] + 1
    else:
        a[x] = a[x - 1]
print(a)

for x in range(len(s) - 1, 0, -1):
    if s[x] == 'b':
        b[x] = b[x+1] + 1
    else: 
        b[x] = b[x+1]
print(b)

for x in range(len(s)):
    if a[x] + b[x+1] > k:
        k = a[x] + b[x+1]
print(k)
