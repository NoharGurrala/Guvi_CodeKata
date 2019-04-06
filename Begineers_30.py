h1,m1 = map(int,raw_input().split())
h2,m2 = map(int,raw_input().split())
h11 = h1*60+m1
h22 = h2*60+m2
ans = abs(h11-h22)
h = ans/60
m = ans%60
print h,m
