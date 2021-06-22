name, char = input("Enter comma separated user\'s name & charactor: ").split(',')

print(f"length of string: {len(name.strip())}")
print(f"total {char} in the name is {name.strip().lower().count(char.strip().lower())}")