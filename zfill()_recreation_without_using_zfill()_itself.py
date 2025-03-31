# define a function that returns the value of the string with the appropriate Zeros
def zero_fill(input_string, length):
    total_width = max(0,(length - len(input_string)))
    return (("0"*total_width)+input_string)
    
# input variables: string, and length
input_string = input("input string: ")
length = int(input("input the length for the Zero: "))

# print statement
print(zero_fill(input_string, length))