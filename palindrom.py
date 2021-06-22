def is_palindrom(str):
  return str == str[::-1]

str = input("Enter string to check palindrom or not: ")
print(is_palindrom(str))