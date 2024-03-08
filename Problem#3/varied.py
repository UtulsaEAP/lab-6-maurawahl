'''
Name: Maura Wahl
Time: Thursdays at 2pm
'''
def process_input(user_input):
    numbers = user_input.split()
    for x in range(0,len(numbers)):
        numbers[x] = float(numbers[x])
      # Split into separate strings

    # Convert strings to floats
    

    # Get max and average
    max_value = max(numbers)
    average_value = sum(numbers)/len(numbers)
    return max_value, average_value

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = (input())

    # Call the function and get the results
    max_value, average_value = process_input(user_input)

    print(f'Max Value: {max_value:.2f}')
    print(f'Average Value: {average_value:.2f}')
