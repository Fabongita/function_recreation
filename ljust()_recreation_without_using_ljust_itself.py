#create a function for left justify that takes in the string input and spaces
def left_just(string_input, width, character):
    total_width = max(width - len(string_input), 0) 
    return((string_input)+(character*total_width)) 

#create a variable for string input, and width
string_input = input("input a string: ")
width = int(input("input how many spaces for the left justification: "))
character = input("input the character to be used, use only 1 digit and a blank is a space: ")
if not character:
    character = " "
elif len(character) > 1:
    character = character[0]

#add a print statement 
print(left_just(string_input, width, character), "Hello, have a good day")