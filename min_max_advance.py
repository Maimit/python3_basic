users = [
  {'name': 'Maimit', 'age': 30, 'score': 70},
  {'name': 'Divya', 'age': 25, 'score': 100},
  {'name': 'Jiana', 'age': 3, 'score': 99},
]

print("max score User Name: ", max(users, key = lambda user: user.get('score')).get('name'))
print("min age user name: ", min(users, key = lambda user: user.get('age')).get('name'))


users2 = {
  'Maimit' : {'age': 30, 'score': 70},
  'Divya' : {'age': 25, 'score': 100},
  'Jiana' : {'age': 3, 'score': 99},
}

print("max age: ", max(users2, key = lambda user: users2[user].get('age')))
print("min age: ", min(users2, key = lambda user: users2[user].get('age')))