
class Person:
  # constructor
  def __init__(self, first_name, last_name, age):
    self.first_name = first_name
    self.last_name = last_name
    self.age = int(age)
    self.full_name = first_name + ' ' + last_name

  @classmethod
  def from_string(cls, str):
    first_name, last_name, age = str.split(",")
    return cls(first_name, last_name, age)

  def is_above_18(self):
    return self.age>18

p = Person('Jiana', 'Patel', 3)
print(p.full_name)

# Calling class method and return constructor
user = Person.from_string("Maimit,Patel,30")
print("User full name: ", user.full_name)
print("Is above 18: ", user.is_above_18())