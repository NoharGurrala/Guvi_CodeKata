n,k = map(int,raw_input().split())
a = map(int,raw_input().split())
d = []
for i in range(n):
    j=i+k
    if j>n:
        j=j-n
    d[j]=a[i]
print d
