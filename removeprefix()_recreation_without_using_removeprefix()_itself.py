# initialize a variable for the input, prefix that is to be removed, and a counter
string_input = input("input anything: ")
prefix = input("add a prefix to be removed: ")
new_string_input = ""
counter = 0
mismatch = False

#use a for loop that iterates through the input which if the input and the prefix are equal then it will continue
for char in string_input:
    if counter < len(prefix):
       if char == prefix[counter]:
        counter += 1
        continue
       else:
            mismatch = True
            break
# checks if the mismatch and
if not mismatch and counter == len(prefix):
    new_string_input = string_input[counter:]
    print(new_string_input)
else:
    print(string_input)


