#initialize an input variable for strings, a flag variable to 
# track if there are spaces, and variable for the new string 
string_input = input("input anything: ")
leading_spaces = True
new_string = ""
#use a for loop that loops through the input which checks the whitespace and returns the index if there is no whitespace
for char in string_input:
    if leading_spaces and char.isspace():
        continue
    else:
        leading_spaces = False
        new_string += char
print(new_string)