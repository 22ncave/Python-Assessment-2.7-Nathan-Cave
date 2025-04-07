"""This file allows users to order pizza.

The user can add pizza,sides and drinks to their order.
remove items, cancel their order and check out.
"""
order = []
order_details = []
saved_orders = []
pizza_list = [["Ham & Cheese", 13.99], ["Pepperoni", 12.49], ["Vegetarian", 14.99], ["Cheese", 11.99], ["Meat Lovers", 13.99], ["Sausage", 13.99], ["Chicken", 13.99], ["Anchovy", 14.99]]
side_list = [["Garlic Bread", 5.67], ["Fries", 4.32], ["Chicken Wings", 7.59], ["Salad", 4.5]]
drink_list = [["Coke", 6], ["Pepsi", 6], ["Orange juice", 4.5], ["Fanta", 5.5]]


def pizza_menu():
    """Allow the user to add a pizza to order.

    This function presents the user with the pizza options. It then allows the user to input which they would
    like to add to their order and how many of that pizza they would like to add.
    Once the user has inputed thier desired pizza and amount it is added to the order list.
    """
    print("1)Ham & Cheese $13.99\n2)Pepperoni $12.49\n3)Vegetarian $14.99\n4)Cheese 11.99\n5)Meat Lovers $13.99\n6)Sausage $13.99\n7)Chicken $13.99\n8)Anchovy $14.99")
    user_pizza = item_input_checker("pizza", 8)
    print("Max of 10")
    pizza_count = item_input_checker("amount", 10)
    for i in range(pizza_count):
        order.append(pizza_list[user_pizza-1])


def side_menu():
    """Allow the user to add a side to order.

    This function presents the user with the sides that they can add to their order. It allows them to input which
    they would like to add tp their order and how many of that item.
    Once the user has inputed thier chosen side and amount it is added to the order list.
    """
    print("1)Garlic Bread $5.67\n2)Fries $4.32\n3)Chicken Wings $7.59\n4)Salad $4.5")
    user_side = item_input_checker("side", 4)
    print("Max of 10")
    side_count = item_input_checker("amount", 10)
    for i in range(side_count):
        order.append(side_list[user_side-1])


def drink_menu():
    """Allow the user to add a drink to order.

    This function presents the user with the drink options.
    It allows them to input which item they would like to add and how many.
    Once the user has inputed their chosen drink and amount it is added to the order list.
    """
    print("1)Coke $6\n2)Pepsi $6\n3)Orange juice $4.5\n4)Fanta $5.5")
    user_drink = item_input_checker("drink", 4)
    print("Max of 10")
    drink_count = item_input_checker("amount", 10)
    for i in range(drink_count):
        order.append(drink_list[user_drink-1])


def item_input_checker(option, amount):
    """Check that the user has inputed correctly.

    This function checks to see if the input from the user in the pizza, side and drink functions is valid.
    If their input is a string the function tells them what they did wrong and lets them reinput.
    If the input is an invalid amount the function corrects them and lets them re enter.
    """
    while True:
        try:
            choice = int(input("Enter chosen " + option + "\n>"))
            if choice < 1:
                print("Please enter a valid input")
            elif choice > amount:
                print("Please enter a valid input")
            else:
                return choice
        except ValueError:
            print("Invalid input\nPlease only enter numbers")


def remove_item():
    """Allow the user to remove an item from order.

    This function allows the user to remove and item from their order.
    It prints all the current items in their order and then lets them chose which they would like to remove.
    If the user has no items in their order the fucntion will let them no and return them to the menu.
    """
    if len(order) < 1:
        print("There is no items in your order")
    else:
        while True:
            try:
                number = 1
                for item in order:
                    print(str(number) + ") " + item[0] + " $" + str(item[1]))
                    number += 1
                remove = int(input("What would you like to remove?\n>"))
                if remove > number-1:
                    print("Invalid input")
                elif remove < 1:
                    print("Invalid input")
                else:
                    order.remove(order[remove-1])
                    print("Item removed")
                    break
            except ValueError:
                print("Invalid input\nPlease only enter numbers")


def welcome():
    """Print welcome mesage.

    This function is used to display a welcome message when first opening the program.
    """
    print("Welcome to The Great Pie in the Sky\nYou're gonna love our pizza")
    input("Press enter to start your order")


def view_order():
    """Allow the user to view their order.

    This function allows the user to view the items that are in their order.
    it gives the user an option to either check out or continue.
    If they continue then it will return to the menu.
    If they check out then it calls the check out function.
    If the user has no items in their order the function informs them then returns them to the menu.
    """
    if len(order) < 1:
        print("No items in your order")
    else:
        for item in order:
            print(item[0] + " $" + str(item[1]))
        while True:
            finnish = input("Would you like to check out\ny/n\n>")
            if finnish == "y":
                check_out()
                break
            elif finnish == "n":
                print("Returning")
                break
            else:
                print("Invalid input")


def check_out():
    """Allow the user to check out.

    This function allows the user to check out with their order.
    It gives them the option to chose between delivery or not.
    It prints out all their order information.
    It allows the user to end or continue and start another order.
    """
    while True:
        delivery = input("Would you like your order to be delivered?\ny/n\n>")
        if delivery == "y":
            name = input("Please enter the name for the order\n>")
            phone_number = input("Please enter your phone number\n")
            address = input("Please enter your adress\n>")
            order_details.append(name)
            order_details.append(phone_number)
            order_details.append(address)
            break
        elif delivery == "n":
            name = input("Please enter the name for the order\n>")
            order_details.append(name)
            break
        else:
            print("Invalid input")
    total_cost = 0
    for item in order:
        print(item[0] + " $" + str(item[1]))
        total_cost = total_cost + item[1]
    print("Total cost of your order $" + str(total_cost))
    if delivery == "y":
        print(order_details[0] + "\n" + order_details[1] + "\n" + order_details[2])
    else:
        print(order_details[0])
    print("Your order will be ready soon")
    while True:
        new_order = input("Start another order?\ny/n\n>")
        if new_order == "y":
            saved_orders = order + order_details
            order.clear()
            order_details.clear()
            menu()
        elif new_order == "n":
            exit()
        else:
            print("Invalid input")


def cancel_order():
    """Allow the user to cancel their order.

    This function allows the user to cancel their order.
    If the user choses to cancel the order the information stored in the order list is removed and the code ends.
    """
    while True:
        confirmation = input("Are you sure you would like to cancel your order?\ny/n\n>")
        if confirmation == "y":
            order.clear()
            print("Your order has been canceled")
            exit()
        elif confirmation == "n":
            print("Returning")
            break
        else:
            print("Invalid input")


def menu():
    """Print main menu.

    This function works as the main menu and allows the user to navigate to the different functions of the program.
    """
    while True:
        user_choice = input("What would you like to do?\na) add a pizza\nb) add a side\nc) add a drink\nd)Remove an item\ne)View order\nf)Cancel order\n>")
        if user_choice == "a":
            pizza_menu()
        elif user_choice == "b":
            side_menu()
        elif user_choice == "c":
            drink_menu()
        elif user_choice == "d":
            remove_item()
        elif user_choice == "e":
            view_order()
        elif user_choice == "f":
            cancel_order()
        else:
            print("Invalid input")
            print("Only enter the visible options")


welcome()

menu()
