n = input()
arr = map(int,raw_input().split())
arr.sort()
st = [55]
for i in range(0,n-1):
    if arr[i] == arr[i+1]:
        p = st.pop()
        #print p,arr[i]
        if arr[i] == p:
          st.append(p)
        else:
          st.append(p)
          st.append(arr[i])
st.pop(0)
if st == []:
    print 'unique'
else:
    print (' '.join(map(str,st)))
