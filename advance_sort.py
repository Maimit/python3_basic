users = [
  {'name': 'Maimit', 'age': 30, 'score': 70},
  {'name': 'Divya', 'age': 25, 'score': 100},
  {'name': 'Jiana', 'age': 3, 'score': 99},
]

print("Sorting by age ascending order: ", sorted(users, key = lambda user: user.get('age')))
print("Sorting by age descending order: ", sorted(users, key = lambda user: user.get('age'), reverse = True))