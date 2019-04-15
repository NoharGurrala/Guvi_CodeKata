n = 2
ar = map(str,raw_input().split())
fi = ''
ar.sort()
sm = len(ar[0])
ma = len(ar[1])
for i in range(0,n):
    if len(ar[i]) < sm:
        sm = len(ar[i])
#print sm
for i in range(0,sm):
    r = 1
    wo = ar[0][i]
 #   print wo
    for j in range(1,n):
        if wo == ar[j][i]:
            r = r + 1
        else:
            break
   # print r    
    if r == n:
      fi = fi + wo
siz = len(fi)
print(ma-siz)
