# List are Iterable

numbers = [1,2,3,4,5,6]

def square_list(l):
  square = []
  for i in numbers:
    square.append(i**2)
  return square

numbers = list(range(1,11))
print(square_list(numbers))