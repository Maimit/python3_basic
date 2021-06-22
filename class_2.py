
# CLASS 2
class Laptop:
  # class variable
  discount = 10
  instances_count = 0

  # constructor
  def __init__(self, brand, model, price):
    Laptop.instances_count += 1
    self.brand = brand
    self.model = model
    self.price = price

  # Class method
  @classmethod
  def count_instances(cls):
    return f" You have created {cls.instances_count} instances of class {cls.__name__} "

  # Instance method
  def discount_price(self):
    # first check object has discount than use OW use class variable discount
    return self.price - (self.discount/100)*self.price

# This will use class variable discount first priority if object not include discount
l1 = Laptop('Mac', 'A4', 200000)
print(l1.discount_price())

# This will use discount 20%
l2 = Laptop('Dell', 'D15', 35000)
l2.discount = 20
print(l2.__dict__)
print(l2.discount_price())

# Call class method
print(Laptop.count_instances())