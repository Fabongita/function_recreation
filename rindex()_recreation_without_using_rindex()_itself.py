# add string and string to find for testing (change to input statement if finished)
new_string = input("input a string: ")
index_string = input("input the number of index to find on the string: ")

#reverse an index using index () to find the last occurence
reversed_index = new_string[::-1].index(index_string[::-1])
reverse_result = len(new_string) - reversed_index - len(index_string)

# print the result 
print(reverse_result)


