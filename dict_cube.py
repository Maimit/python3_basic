def cube_finder(n):
  d = dict()
  for i in range(1, n+1):
    d[i] = i**3
  return d

print(cube_finder(5))