# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.

# pseudocode

# Function to remove characters from a string
    # Set result to the substring starting from index n to the end of the string
    # Return the modified string
   

# Print a message indicating that characters are being removed from a string

# Set the input string and the number of characters to remove

# Call the remove_chars function with the input string and the number of characters to remove

# Print the original string and the string after removing the specified number of characters



# _____________________________________________________________ actual code _____________________________________________________________________
# Function to remove characters from a string
def remove_chars(input_string, n):
    # Set result to the substring starting from index n to the end of the string
    result = input_string[n:]
    # Return the modified string
    return result


# Print a message indicating that characters are being removed from a string
print("Removing characters from a string")