# add variables
string_input = input("input a sentence that is either fully capital or not fully capital or both: ")
checker = True
# use for loop
for char in string_input:
    if char.islower():
        checker = False
        print(checker)
        checker = ""
        break
    else:
        continue
print(checker)