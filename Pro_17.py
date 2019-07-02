n,m = map(int,raw_input().split())
array = map(int,raw_input().split())
ans = 'no'
for i in range(0,n):
    for j in range(i,n):
        su = array[i] + array[j]
        if su == m:
            ans = 'yes'
print ans
