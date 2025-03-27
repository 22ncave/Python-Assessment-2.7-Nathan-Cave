order = []
pizza_list = [["Ham & Cheese",13.99], ["Pepperoni",12.49], ["Vegetarian",14.99], ["Cheese",11.99],["Meat Lovers",13.99], ["Sausage",13.99], ["Chicken",13.99], ["Anchovy",14.99]]
side_list = [["Garlic Bread", 5.67], ["Fries", 4.32],["Chicken Wings", 7.59], ["Salad",4.5]]
drinl_list = []
def pizza_menu():
    """
    This function presents the user with the pizza options. It then allows the user to input which they would
    like to add to their order and how many of that pizza they would like to add.
    """
    print("1)Ham & Cheese $13.99\n2)Pepperoni $12.49\n3)Vegetarian $14.99\n4)Cheese 11.99\n5)Meat Lovers $13.99\n6)Sausage $13.99\n7)Chicken $13.99\n8)Anchovy $14.99")
    user_pizza = int(input("Which pizza would you like to add?\n>"))
    pizza_count = int(input("How many would you like to add?\n>"))
    for i in range(pizza_count):
        order.append(pizza_list[user_pizza-1]) 

def side_menu():
    print("1)Garlic Bread $5.67\n2)Fries $4.32\n3)Chicken Wings $7.59\n4)Salad $4.5")
    user_side = int(input("Which side would you like to add\n>"))
    side_count = int(input("How many would you like to add?\n>"))
    for i in range(side_count):
        order.append(side_list[user_side-1])


def input_checker():
    print() 

def welcome():
    print("Welcome to The Great Pie in the Sky\nYou're gonna love our pizza\nMax 10 items per order")
    input("Press enter to start your order")

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
welcome()

menu()
pizza_menu()
