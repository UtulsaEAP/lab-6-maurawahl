'''
Name: Maura Wahl
Time: Thursdays at 2pm
'''
def process_and_print(input_string):
      # Split into separate strings DONE BOI
  strings = input_string.split(" ")
    # Convert strings to integers and filter out negative values DONE BOI
  for x in range(0,len(strings)):
     strings[x] = int(strings[x])
  negative = []
  for x in range(0,len(strings)):
     if strings[x] < 0:
        negative.append(strings[x])
  negative.sort()
  negative = negative[::-1]
  for x in range(0,len(negative)):
     print(str(negative[x]) + " ", end = "")
     

    # Sort integers in reverse order DONE BOI SIKE
  
    # Print sorted integers
    
    

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)
