# add variables, and a Flag variable
string_input = input("input a sentence that is either fully capital or not fully capital or both: ")
checker = True

# use for loop that breaks and turns the flag variable to false 
for char in string_input:
    if char.islower():
        checker = False
        break
    else:
        continue
print(checker)