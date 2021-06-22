name = input('Enter name: ')
age = int(input('Enter age: '))
fav_movies = input("Enter favorite movies comma separated: ").split(',')
fav_songs = input("Enter favorite songs comma separated: ").split(',')

d = dict(name = name, age = age, fav_movies = fav_movies, fav_songs = fav_songs)

for key, value in d.items():
  print(f'{key}: {value}')
