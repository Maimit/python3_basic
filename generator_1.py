# Generator are Iterator
def even_generator(n):
  for i in range(2, n+1, 2): # range(start_arg, stop_arg, step)
    if i%2 == 0:
      yield i

numbers = even_generator(10) # Generate sequence

for num in numbers:
  print(num)

# after generating sequence you can only iterate only once
for num in numbers:
  print(num)