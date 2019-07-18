n = raw_input().split()
ans = ''
for i in range(len(n)):
    ans = ans + n[i][::-1] + ' '
print ans
