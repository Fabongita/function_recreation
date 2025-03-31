# add variables for: list, string counter,  and the string itself that is to be counted
string_list =  ["hippo", "apple", "spam", "hajime", "hippo", "no", "ippo", "hippo", "hippo"]
string_to_count = "hippo"
string_counter = 0

# use a for loop that iterates through the list which counts the specified string
for item in string_list:
    if item == string_to_count:
        string_counter += 1
    else:
        continue
# add a print statement that show the results 
print(string_counter)