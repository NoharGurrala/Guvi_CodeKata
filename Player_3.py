n = input()
fin = 0
while n != 0:
    l = n % 10
    fin = fin * 10 + l
    n = n / 10
print fin
