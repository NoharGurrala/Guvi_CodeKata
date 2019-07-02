n,m = map(int,raw_input().split())
array = []
for i in range(0,n):
    a = map(int,raw_input().split())
    a.sort()
    array.append(a)
for i in range(0,m):
    ar = []
    for j in range(0,n):
        ar.append(array[j][i])
    ar.sort()
    for j in range(0,n):
        array[j][i] = ar[j]
for i in range(0,n):
    for j in range(0,m):
        print array[i][j],
    print''
