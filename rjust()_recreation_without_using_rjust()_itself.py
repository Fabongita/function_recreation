# define function that returns the value of the string input with the appropriate spaces
def right_just(string_input, length, character_type):
    total_width = max(0, (length - len(string_input)))
    return((total_width*character_type)+string_input)
# add input variables, the type of character, and the length of the characters
string_input = input("input a string: ")
length = int(input("input the length for the characters: "))
character_type = input("input the type of character to use, (blank for space and only one digit)")

# if and else that checks the type of character
if not character_type:
    character_type = " "
elif len(character_type) > 1:
    character_type = character_type[0]

# print statement
print(right_just(string_input, length, character_type), "HAHAAHAH")