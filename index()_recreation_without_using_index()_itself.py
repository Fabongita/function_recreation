# add variables for: list, string counter,  and the string itself that is to be counted
string_list =  ["apple", "hippo", "spam", "hippo" ]
string_to_count = "hippo"
# use a for loop that iterates through the list which counts the specified string
for index, item in enumerate(string_list):
    if item == string_to_count:
        found_index = index
        break
else:
    raise ValueError(f"{string_to_count} not found in the list")
# add a print statement that show the results 
print(found_index)