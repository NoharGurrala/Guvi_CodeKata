n = input()
t = n
fi = 0
while t!=0:
    l = t%10
    f = l**3
    fi = fi + f
    t = t / 10
if fi == n:
    print 'yes'
else:
    print 'no'
