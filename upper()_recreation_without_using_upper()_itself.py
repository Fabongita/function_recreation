# add string input variables, and a new string input variable
string_input = input("input a string: ")
new_string = ""

# add a for loop that checks if each character is a lowercase which converts it into uppercase
for char in string_input:
    if char.islower():
        new_string+=chr(ord(char)-32)
    else:
        new_string += char

#add print statement for the results
print(new_string)