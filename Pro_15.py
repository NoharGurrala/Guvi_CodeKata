n = input()
array = map(int,raw_input().split())
array.sort()
for i in range(0,n):
    print array[(n-1)-i]
