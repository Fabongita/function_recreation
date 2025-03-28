#add input variables for the strings and the end string, and a counter variable
string_input = input("input a string: ")
end_string = input("input an end string: ")
counter = 0

#add a for loop that loops through the input variables in reverse and checks if it is the same with the end string
for char in string_input[::-1]:
    # Compare the current character with the corresponding character from the end of end_string
    if counter < len(end_string) and char == end_string[-(counter+1)]:
        counter += 1
    else: 
        break
    
# checks if the characters match
if counter == len(end_string):
    print(True)
else: 
    print(False)