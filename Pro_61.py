str1 = raw_input()
str2 = raw_input()
val1 = []
val2 = []
for i in range(0,len(str1)):
    ap1 = ord(str1[i])
    ap2 = ord(str2[i])
    val1.append(ap1-96)
    val2.append(ap2-96)
addval = [val1[i] + val2[i] for i in range(len(val1))]
addval = [addval[i]-26 if addval[i] > 26 else addval[i] for i in range(len(addval))]
'''for i in range(addval):
    if addval[i] > 26:
        addval[i] -= 26'''
stri = [chr(addval[i]+96) for i in range(len(addval))]
finastr = ''.join(map(str,stri))
print finastr
