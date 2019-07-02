n = input()
array = map(int,raw_input().split())
array.sort()
ans=[]
for i in range(0,n):
    ans.append(bin(array[i])[2:])
ans.sort()
main = []
for i in range(0,n):
    main.append(int(ans[i],2))
for i in  range(0,n):
    print(main[(n-1)-i])
