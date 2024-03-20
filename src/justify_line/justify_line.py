# def justify_line(string,number):
#     listed_string = list(string)
#     # There are 16-15 =1 space
#     spaces = number - len(string)  
#     counter = 0
#     for i,letter in enumerate(listed_string):
#          while counter < spaces:
#                 if letter == " ":
#                     listed_string.insert(i+1," ")
#                     counter += 1
#                 break
#     print("".join(listed_string))
#     return "".join(listed_string)   


def justify_line(string, number):
    # Calculate the number of extra spaces needed to reach the maximum line length
    spaces = number - len(string)
    
    # Check if the string exceeds the maximum line length
    if spaces < 0:
        return "String exceeds maximum line length."
    
    # Convert the string to a list for easy manipulation
    listed_string = list(string)
    
    # Calculate the number of spaces to be inserted between words
    counter = listed_string.count(" ")
    
    # Calculate the number of additional spaces to distribute between words
    min = spaces // counter
    
    # Initialize a counter for inserted spaces
    counter = 0
    
    # Iterate through the characters of the string
    for i, letter in enumerate(listed_string):
        # Check if it's time to insert additional spaces
        while counter < min:
            if letter == " ":
                # Insert additional spaces
                listed_string.insert(i + 1, " " * (min - counter))
                counter += 1
            break  # Break out of the while loop
        
    # Convert the modified list back to a string and return
    return "".join(listed_string)
           
  
        
