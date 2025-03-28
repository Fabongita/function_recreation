# add input string input variable, and a new string variable for the result, and a flag variable
string_input = input("input a string: ")
new_string = ""
first_letter = True

# add a for loop that checks each character to see if it is an alpha numeric, and a first letter
for char in string_input:
    if char.isalpha() and first_letter:
        new_string += char.upper()
        first_letter = False
    else:
        new_string += char.lower()

print(new_string)