# initialize a variable for the input, prefix that is to be removed, and a counter
string_input = input("input anything: ")
prefix = input("add a prefix to be removed: ")
new_string_input = ""
counter = 0

#use a for loop that iterates through the input which if the input and the prefix are equal then it will continue
for char in string_input:
    if counter < len(prefix) and char == prefix[counter]:
        counter += 1
        continue
    else:
        new_string_input += char
# checks if 
if counter == len(prefix):
    print(new_string_input)
else:
    print(string_input)


