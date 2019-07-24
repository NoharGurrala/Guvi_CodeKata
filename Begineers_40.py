n = input()
i = 1
j = 1
print i,j,
for k in range(0,n-2):
    s = i + j
    print s,
    i = j
    j = s
