m,n = map(int,raw_input().split())
for i in range(m,n):
  t = i
  fi = 0
  while t!=0:
    l = t%10
    f = l**3
    fi = fi + f
    t = t / 10
  if fi == i:
    print fi,
