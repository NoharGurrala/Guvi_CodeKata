n = raw_input().split()
ans = []
for i in range(len(n)):
    ans.append(n[i][::-1])
ansstr = ' '.join(map(str,ans))
print ansstr
