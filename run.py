# python3 run.py
from data import *
from tabulate import tabulate

def display_instructions():
    """
    Displays title and instructions to the game
    """
    print("WELCOME TO THE TRADE GAME\n")
    print("The game is simple: trade your thumbtack with higher valued items at one of the five vendors.")
    print("Your score is the amount of cash you receive when selling your items when leaving the market.")
    
def input_username():
    """
    Lets the user insert a username
    """
    username = input("Enter username here:")
    print("It is time to start the game. Let the great trading begin!\n")
    return username
    
def game_menu():
    """
    Displays a menu to allow the user to choose what to do in the game
    """
    print("1: Trade with Ron\n"
        "2: Show your inventory\n" 
        "3: Show score and exit game\n"
        "4: Learn more about the vendors")
    choice = ""
    choice_not_made = True
    while(choice_not_made):
        selected_answer = input("Choose a path:")
        match selected_answer:
            case "1":
                choice = ron
                choice_not_made = False
            case "2":
                show_inventory()
            case "3":
                choice_not_made = False
                display_score_and_exit()
            case "4":
                show_vendor_info()
            case _:
                print("Something went wrong, select a number between 1-3")
    return choice

def visit_vendor(vendor):
    """
    Displays the chosen vendors inventory
    """
    vendors_items = []
    vendors_quantity = [] #necessary??
    for i in vendor:
        print(f"Item: {i["item"].capitalize()}\nQuantity: {i["quantity"]}\n")
        vendors_items.append(i["item"])
        vendors_quantity.append(i["quantity"])

    MyBool = True
    while(MyBool):
        chosen_item = input("What would you like to trade? ")
        if chosen_item.lower() in vendors_items:
            print("I have that item!")
            break
        else:
            print("I can't see that in my inventory. Maybe you misspelled?")
    print("What now?")

def show_inventory():
    """
    Displays the users inventory
    """
    print(f"You have: {user[0]["quantity"]} {user[0]["item"]}")

def show_vendor_info():
    """
    Display ino about the vendors
    """
    print("There are five vendors at the market:\n"
        "Ron - the grumpy man with a big mustasch. Not to keen on selling his stuff.\n"
        "Jim - A tall, skinny guy who is always happy. Would love to trade with you!")

def display_score_and_exit():
    """
    Displays score and exits game
    """
    total_score = 0
    for i in user:
        total_score += i["value"]
    print(f"Your inventory sold for ${total_score}, good job!")

    exit_answer = True
    while (exit_answer):
        answer = input("Are you ready to exit game? (Y/N):")
        if answer.lower() == "y":
            print("You pressed y")
            exit()
            exit_answer = False
        elif answer.lower() == "n":
            print("you pressed n")
            game_menu()
            exit_answer = False
        else:
            print("Something went wrong, please input the letter 'Y' or 'N'")

def main():
    """
    Runs the game
    """
    display_instructions()
    username = input_username()
    chosen_vendor = game_menu()
    visit_vendor(chosen_vendor)
    
main()


