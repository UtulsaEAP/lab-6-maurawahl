'''
Name: Maura Wahl
Time: Thursdays at 2pm
'''
def process_user_contacts(user_input):
    user_contacts = user_input.split(" ")
    dictionary = {}
    for x in range(0,len(user_contacts)):
        new_contact = user_contacts[x].split(",")
        dictionary[new_contact[0]] = new_contact[1]

       # user_contacts.remove(user_contacts[x])

 
    #user_input = 
    #tokens = 

    # Put word pairs into a dictionary
    
    # Get contact name from input, output contact's phone number
    contact_name = input("Enter the contact name: ")
    print(dictionary[contact_name])
   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)
