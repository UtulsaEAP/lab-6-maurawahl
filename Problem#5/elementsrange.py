'''
Name: Maura Wahl
Time: Thursdays at 2pm
'''
def filter_and_print_range(integer_list, min_val, max_val):
    #write your code here
    newlist=[]
    for x in range(0,len(integer_list)):
        if min_val <= int(integer_list[x]) <= max_val:
            newlist.append(integer_list[x])
    for x in range(0, len(newlist)):
        print(str(newlist[x]) + ",", end = "")

if __name__ == '__main__':
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ").split(" ")
    integer_list = user_input

    # Get input for the range (min and max values)
    user_input = input("Enter the min and max values separated by a space: ").split(" ")
    min_val, max_val = (int(user_input[0]), int(user_input[1]))

    # Call the function to filter and print the numbers in the given range
    filter_and_print_range(integer_list, min_val, max_val)
