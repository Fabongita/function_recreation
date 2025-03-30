# Add a string input, flag, and a new string variable
string_input = input("input a sentence with leading or trailing spaces: ")
trailing_spaces = True
new_string = ""
# add a for loop that checks if there are spaces on the right side and removes it
for char in string_input[::-1]:
    if char.isspace() and trailing_spaces:
        continue
    else:
        trailing_spaces = False
        new_string += char
# add a print statement for the result
new_string = new_string[::-1]
print(new_string,"HAHAHAH")