#initialize an input variable for strings, a flag variable to 
# track if there are spaces, and variable for the new string 
string_input = input("input anything: ")
leading_spaces = True
new_string = ""
#use a for loop that loops through the input which checks the whitespace and returns the index if there is no whitespace
for i in string_input:
    if leading_spaces and i.isspace():
        continue
    else:
        leading_spaces = False
        new_string += i
print(new_string)