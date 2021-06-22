# Problem to print function name and doc 
def decorator(function):
  def wrapper(*args, **kwargs):
    '''This is wrapper function'''
    print("This is awesome function")
    function(*args, **kwargs)
  return wrapper

@decorator
def fun1():
  '''This function print string'''
  print("This is fun1")

@decorator
def add(n1, n2):
  return n1 + n2

# Problem 1
print(fun1.__name__) # wrapper
print(fun1.__doc__) # This is wrapper function


# Problem 2
print(add(2,5)) # None