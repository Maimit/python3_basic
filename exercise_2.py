num1, num2, num3 = input("Enter number1, number2, number3 by comma separated: ").split(",")
average = (int(num1) + int(num2) + int(num3)) / 3
print(f"Average of {num1},{num2},{num3} is: {average}")

name = input("Enter name: ")
print("Reverse name: ", name[-1::-1])