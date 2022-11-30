# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
string = input("Alphabetized string")

string_array = sorted([*user_string])

alpha_string = ""
for letter in string_array:
    alpha_string += letter

print("Alphabetized: ", alpha_string)