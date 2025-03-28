# Add input variable, variable for the lowered words
string_input = input("input sentences that has capital letters: ")
lowered_words = ""

# for loop logic that iterates through the input variable and checks if it is a small letter or not
for char in string_input:
    if char.isupper():
        swapper = char.swapcase()
        lowered_words += swapper
    else:
        lowered_words += char
        
print(lowered_words)
