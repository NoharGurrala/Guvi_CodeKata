k = input()
array = []
for i in range(0,k):
    arr = map(int,raw_input().split())
    array = array + arr
array.sort()
for i in array:
    print i,
