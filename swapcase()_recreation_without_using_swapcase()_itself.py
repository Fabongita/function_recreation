# add string input, and the new string
string_input = input("input a string with alternating capitalizations: ")
new_string = ""
# for loop that checks if an string is a capital or small letter. Then changes to its opposite.

for char in string_input:
    if char.isupper():
        new_string += chr((ord(char)+32))
    elif char.islower():
        new_string += chr((ord(char)-32))
    else:
        new_string += char

# add print statement
print(new_string)

