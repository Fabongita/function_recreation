# initialize a variable for the input, prefix that is to be removed, and a counter
string_input = input("input anything: ")
prefix = input("add a prefix to be removed: ")
new_string_input = ""

#use an if statement to see if the string input starts with the prefix to be removed
if string_input.startswith(prefix):
    new_string_input = string_input[len(prefix):]  
else:
    new_string_input = string_input  

print(string_input)


