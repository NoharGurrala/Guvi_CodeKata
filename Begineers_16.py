m,n = map(int,raw_input().split())

for j in range(m+1,n):
  c = 0
  for i in range(2,j):
    if j % i == 0:
      c = c + 1
  if c == 0:
      print j,
