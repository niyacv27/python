list=["Niya","priya","mariyam"]
longest_length = 0
for word in list:
    current_length = len(word)
    if current_length > longest_length:
        longest_length = current_length

print("Length of the longest word is:",longest_length)   
