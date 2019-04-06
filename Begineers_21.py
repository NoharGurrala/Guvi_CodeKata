n,a,d = map(int,raw_input().split())
su = []
su.append(a)
#print  n,a,d
for i in range(1,n):
    su.append(a + i*d)
add = 0
for i in su:
    add = add + i
print add
