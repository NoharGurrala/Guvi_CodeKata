n = input()
su = 0
while n != 0:
    nu = n%10
    su = su + (nu ** 2)
    n = n/10
print su
