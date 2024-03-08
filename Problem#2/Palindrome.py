'''
Name: Maura Wahl
Time: Thursdays at 2pm
'''
def check_palindrome(user_input):
 #type your code here
    solution_flag = False
    new_user_input = user_input.lower().replace(" " , "")
    #print(new_user_input)
    backwards = "".join(reversed(new_user_input))      #"".join changes list into string
    if backwards == new_user_input:
        solution_flag = True
    else:
        exit
    if solution_flag:
        print("palindrome: " + user_input)
    else: 
        print("not a palindrome: " + user_input)


if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
