# add string and string to find for testing (change to input statement if finished)
new_string = "Mi casa, su casa."
index_string = "k"

#reverse an index using index () to find the last occurence
reversed_index = new_string[::-1].index(index_string[::-1])
reverse_result = len(new_string) - reversed_index - len(index_string)

# print the result 
print(reverse_result)


