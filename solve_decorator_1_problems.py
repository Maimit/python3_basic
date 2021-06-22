from functools import wraps # Solve Problem 1

def decorator(function):
  @wraps(function) # Solve Problem 1
  def wrapper(*args, **kwargs):
    '''This is wrapper function'''
    print("This is awesome function")
    return function(*args, **kwargs) # return function to solve the problem 2
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