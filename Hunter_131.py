n = input()
m = n/2+1
so = map(int,raw_input().split())
ar = so
ar.sort()
fi = ar[m:]
fi = fi[::-1]
li = ar[:m]
final = ''
for i in range(m):
    final = final + str(fi[i]) + ' ' + str(li[i]) + ' '
if(n%2 != 0):
    final = final + str(fi[-1])
print final
