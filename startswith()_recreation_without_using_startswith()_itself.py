# add input string, and starts with variable
string_input = input("input a string: ")
starts_with = input("input a start string: ")
# add if and else that checks if the input starts with the starts variable
if string_input[:len(starts_with)] == starts_with:
    print("True")
else:
    print("False")