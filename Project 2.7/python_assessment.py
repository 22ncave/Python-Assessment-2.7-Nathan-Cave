order = []
pizza_list = [["Ham & Cheese",13.99], ["Pepperoni",12.49], ["Vegetarian",14.99], ["Cheese",11.99],["Meat Lovers",13.99], ["Sausage",13.99], ["Chicken",13.99], ["Anchovy",14.99]]
def pizza_menu():
    """
    This function presents the user with the pizza options then allows them to add 1 to their order
    """
    print("Ham & Cheese $13.99\nPepperoni $12.49\nVegetarian $14.99\nCheese 11.99\nMeat Lovers $13.99\nSausage $13.99\nChicken $13.99\nAnchovy $14.99")
    user_pizza = input("Which pizza would you like to add?\n")
    pizza_found = False
    for pizza in pizza_list:
        if user_pizza == pizza[0]:
            pizza_count = int(input("How many would you like to add?\n"))
            for i in range(pizza_count):
                order.append(pizza)
            pizza_found = True
    if pizza_found == False:
        print("That pizza could not be found")
        

def side_menu():
    print()

def drink_menu():
    print

def check_out():
    print

def menu():
    while True:
        user_choice = input("What would you like to do?\na) add a pizza\nb) add a side\nc) add a drink\nd)check out\n>")
        if user_choice == "a":
            pizza_menu()
        elif user_choice == "b":
            side_menu()
        elif user_choice == "c":
            drink_menu()
        elif user_choice == "d":
            check_out()
start_order = input("Press enter to start your order")
menu()
pizza_menu()
