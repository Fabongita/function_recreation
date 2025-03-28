# define a function for the main logic of the center method
def center_alignment(string_input, padding_character, character_number):
    total_padding = max((character_number - len(string_input), 0))
    total_left_padding = total_padding // 2
    total_right_padding = total_padding - total_left_padding
    return((total_left_padding*padding_character)+string_input+(total_right_padding*padding_character))
# initialize variables for the string input, how much padding, and the number of characters
string_input = input("Input a string: ")

padding_character = input("Input the character for the padding, (input only one character, and blank for 1 space): ")
character_number = int(input("input how many characters to use: "))

# Use a print statement to for the output
print(center_alignment(string_input, padding_character, character_number))