n = input()
ar = map(int,raw_input().split())
an = []
for i in range(0,n):
    if i%2==0:
        if ar[i]%2 == 1:
            an.append(ar[i])
    else:
        if ar[i]%2 == 0:
            an.append(ar[i])
print (' '.join(map(str,an)))
