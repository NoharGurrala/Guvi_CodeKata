n = input()
array = map(int,raw_input().split())
arr = []
for i in range(0,2):
    ans = 0
    for i in range(0,n,2):
        ans = ans + array[i]
    arr.append(ans)
arr.sort()
print arr[-1]
