from functools import wraps

def data_type_allow(data_type):
  def decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
      if all([type(i) == data_type for i in args]):
        return function(*args, **kwargs)
      return print("Invalid argument")
    return wrapper
  return decorator


@data_type_allow(int)
def to_square(*args):
  return [n**2 for n in args]

@data_type_allow(str)
def join_string(*args):
  return " ".join(args)

print(to_square(1,2,3,4))
print(join_string("Maimit", "Patel"))
