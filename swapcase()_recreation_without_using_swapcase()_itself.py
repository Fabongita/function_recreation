# add string input, and the new string
string_input = input("input a string with alternating capitalizations: ")
new_string = ""
# for loop that checks if an string is a capital or small letter. Then changes to its opposite.
for char in string_input:
    if char.isupper():
        capital_converter = chr((ord(char)+32))
        new_string += capital_converter
    if char.islower():
        small_converter = chr((ord(char)-32))
        new_string += small_converter
    else:
        new_string += char
# add print statement
print(new_string)

