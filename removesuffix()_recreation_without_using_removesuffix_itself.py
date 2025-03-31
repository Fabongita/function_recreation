#add string input variables, suffix to be removed and a new string variable
string_input = input("input a string: ")
suffix_removal = input("input the suffix to be removed: ")

#if else statement that checks if the string endswith the suffix
if string_input.endswith(suffix_removal):
   new_string = string_input[:-len(suffix_removal)]
else:
    new_string = string_input

#add print statement
print(new_string)