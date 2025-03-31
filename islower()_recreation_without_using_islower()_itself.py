# add string_input
string_input = input("input a string: ")
checker = True
# add for loop and an if else statement that checks if the string input is an uppercase
for char in string_input:
    if char.isupper() or not char.isalpha():
        checker = False
        break
    else: 
        continue
#add print statement that outputs true or false
print(checker)
