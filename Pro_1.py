n = input()
ar = []
sm = 10000
fi = ''
for i in range(0,n):
    st = raw_input()
    ar.append(st)
    if len(st) < sm:
        sm = len(st)
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
print fi
