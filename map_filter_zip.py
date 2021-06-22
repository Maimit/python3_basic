# map => return iterator object
def square(n):
  return n**2

numbers = range(1,11)
print(list(map(square, numbers)))

# lambda + map
print(list(map(lambda n: n**2, numbers)))

# Filter => return iterator object
def is_even(n):
  return n%2 == 0

print(list(filter(is_even, numbers)))

# lambda + Filter
print(list(filter(lambda n: n%2 == 0, numbers)))

# zip => return iterator object
l1 = [1,2,3,4]
l2 = [5,6,7,8]

# Make tuple
print(list(zip(l1, l2)))