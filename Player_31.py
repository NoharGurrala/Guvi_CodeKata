strb = raw_input()
stack = []
ope = '{[('
clos = '}])'
l = len(strb)
for i in range(0,l):
  if strb[i] in ope:
    stack.append(strb[i])
  else:
    last = stack.pop()
    if (strb[i] == '}') & (last == '{'):
      continue;
    elif (strb[i] == ']') & (last == '['):
      continue
    elif (strb[i] == ')') & (last == '('):
      continue
    else:
      print "no"
if stack == []:
      print "yes"
