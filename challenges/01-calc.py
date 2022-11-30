# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
calc_method = input("What calculation would you like to do? (add, sub, mult, div)\n")
num1 = int(input("What is the first number?\n"))
num2 = int(input("What is the second number?\n"))


if calc_method == "add":
    print(f"Your result is {num1 + num2}")

elif calc_method == "sub":
    print(f"Your result is {num1 - num2}")

elif calc_method == "mult":
    print(f"Your result is {num1 * num2}")

elif calc_method == "div":
    print(f"Your result is {num1 // num2}")

    print("Congratulations, you finished!")