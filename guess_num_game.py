import random

winning_num = random.randint(1,100)
guessing_num = int(input("Enter number between 1 and 100: "))
game_over = False
guess_count = 1

while not game_over:
  if guessing_num == winning_num:
    input(f"You are win in {guess_count} guess")
    game_over = True
  else:
    if guessing_num < winning_num:
      print("Number is to low")
    else:
      print("Number is to high")

    guess_count += 1
    guessing_num = int(input("Enter again: "))
