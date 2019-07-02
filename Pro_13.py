n,itera = map(int,raw_input().split())
array = map(int,raw_input().split())
add=[]
for i in range(0,itera):
    s = []
    limit = map(int,raw_input().split())
    ll = limit[0]-1
    for i in range(ll,limit[1]):
        s.append(array[i])
    add.append(min(s))
for i in add:
    print i
