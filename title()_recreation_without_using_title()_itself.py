# initialize a variable for the string input, and an empty string that will be used as the result, added a flag variable
string_input = "HELLO WORLD!"
string_results = ""
new_word = True

# use a for to check each characters and see if it it's a first letter, non alpha numeric, and a succeeding letter that is capitalized
for char in string_input:
    if char.isalpha() and new_word:
        string_results += char.upper()
        new_word = False
    elif char.isalpha() and not new_word:
        string_results += char.lower()
    else:
        string_results += char
        new_word = True

#add a print statement that shows the results
print(string_results)
