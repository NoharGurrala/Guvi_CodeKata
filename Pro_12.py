n,itera = map(int,raw_input().split())
array = map(int,raw_input().split())
add=[]
for i in range(0,itera):
    s = 0
    limit = map(int,raw_input().split())
    ll = limit[0]-1
    for i in range(ll,limit[1]):
        s = s + array[i]
    add.append(s)
for i in add:
    print i
