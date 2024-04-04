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
    username = input("Enter username here: ")
    print("It is time to start the game. Let the great experiment begin!\n")
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
        selected_answer = input("\nChoose an option:\n")
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
    print("This is my inventory: \n")
    items_list = vendor["items"]
    for item in items_list:
        print(f"{(items_list.index(item)+1)}: {item["item"].capitalize()}")
    
    answer = input("\nWould you like to make a trade? (Y/N): ") #this need some error handling
    if answer.lower() == "n":
        print("Let us go back to the menu then.")
        game_menu()
    elif answer.lower() == "y":
        chosen_item = input("What would you like to trade? ").lower()
    else:
        print("Please answer Y or N")

    return chosen_item, chosen_qnt
    
    print("What now?")

def trade(item, quantity):
    """
    Users trade offer is tested
    If accepted - user and vendors inventory updated
    """


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
    chosen_tuple = visit_vendor(chosen_vendor)
    print(f"I want to trade {chosen_tuple[1]} {chosen_tuple[0]}")

if __name__ == "__main__": 
    main()


