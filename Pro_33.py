nam = raw_input()
ansstr = []
for i in range(0,len(nam)):
    for j in range(i,len(nam)+1):
        substr = nam[i:j]
        ansstr.append(substr)
ansstr.sort()
print ansstr[-1]
