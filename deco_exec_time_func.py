import time
from functools import wraps

def decorater(function):
  @wraps(function)
  def wrapper(*args, **kwargs):
    t1 = time.time()
    return_value = function(*args, **kwargs)
    print(f"Time to execute this function is {time.time() - t1}")
    return return_value
  return wrapper

@decorater
def print_numbers(n):
  for i in range(1, n+1):
    i

print_numbers(1000)