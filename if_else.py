import random;

winning_num = random.randint(1,100)
print(winning_num)

guessed_num = int(input("Enter any number from 1 to 100: "))
if winning_num == guessed_num:
  print("YOU ARE WIN!!!!!")
else:
  if guessed_num < guessed_num:
    print("too low!!")
  else:
    print("too high!!")