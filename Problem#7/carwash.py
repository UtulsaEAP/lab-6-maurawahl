'''
Name: Maura Wahl
Time: Thursdays at 2pm
'''
def calculate_car_wash_price(service_choice1, service_choice2):
    services = {'Air freshener': 1, 'Rain repellent': 2, 'Tire shine': 2, 'Wax': 3, 'Vacuum': 5, "-": 0}
    base_wash = 10
    total = int(base_wash)
    value = services.get(service_choice1)
    total += int(value)
    value2 = services.get(service_choice2)
    total += int(value2)
   #type your code here 
    print("ZyCar Wash")
    print("Base car wash - $10")
    if service_choice1 != "-":
        print(service_choice1 + " - $" + str(services.get(service_choice1)))
    if service_choice2 != "-":
        print(service_choice2 + " - $" + str(services.get(service_choice2)))
    print("-----")
    print("Total price: $" + str(total))

    
if __name__ == '__main__':
    # Get user input for service choices
    service_choice1 = input("Enter first service choice: ")
    service_choice2 = input("Enter second service choice: ")

    # Call the function to calculate car wash price
    calculate_car_wash_price(service_choice1, service_choice2)

    
