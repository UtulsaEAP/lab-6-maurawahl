'''
Name: Maura Wahl
Time: Thursdays at 2pm
'''

def food_input():
    user_input = input()
    tokens = user_input.split()

    #type you while  loop here
    while tokens[1] != "0" and tokens[0] != "quit":
        print("Eating " + tokens[1] + " " + tokens[0] + " a day keeps you happy and healthy.")
        new_input = input()
        tokens = new_input.split()

if __name__ == "__main__":
    food_input()
