nu = input()
na = raw_input()
sta = []
vowels = 'aeiouAEIOU'
for i in na:
    if i not in vowels:
        sta.append(i)
fin = ''
for i in range(len(sta)):
    fin = fin + sta.pop()
print fin
