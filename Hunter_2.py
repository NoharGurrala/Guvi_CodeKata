n = input()
ar = map(int,raw_input().split())
ar.sort()
ar.reverse()
print( ''.join(map(str,ar)))
