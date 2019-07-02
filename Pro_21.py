def check(a,nu,t):
    b = a[:nu]
    c = a[nu:]
    ba = sum(b)/len(b)
    ca = sum(c)/len(c)
    if ba == ca:
        return 1
    return 0
n = input()
ans = 'no'
array = map(int,raw_input().split())
for i in range(1,n-1):
    a = check(array,i,n)
    if a == 1:
        ans = 'yes'
        break
print ans
