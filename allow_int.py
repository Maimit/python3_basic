from functools import wraps

def decorator(function):
  @wraps(function)
  def wrapper(*args, **kwargs):
    if all([type(i) == int for i in args]):
      return function(*args, **kwargs)
    return print("Invalid arguments")
  return wrapper

@decorator
def add(*args):
  total = 0
  for n in args:
    total += n
  return total

print(add(1,2,3,4,5))