# python3 run.py
from data import *
from colorama import Fore, Back, Style

def display_instructions():
    """
    Displays title and instructions to the game
    """
    print(Fore.GREEN + "WELCOME TO THE GARAGE SALE") 
    print(Style.RESET_ALL)
    print("The game is simple: trade your thumbtack with higher valued items"
    "at one of the five vendors.\n"
    "Your score is the amount of cash your inventory is worth when leaving"
    "the market.\n"
    "Remember: the trade deal needs to be good for both you and the vendor -"
    "or they will deny the deal.\n")
    
    
    
def input_username():
    """
    Lets the user insert a username
    """
    player.username = input("Enter username here:\n")
    print(Fore.GREEN + "\nIt is time to start the game."
    "Let the great experiment begin!")
    print(Style.RESET_ALL)
    
def game_menu():
    """
    Displays a menu to allow the user to choose what to do in the game
    """
    choice = ""
    choice_not_made = True
    while(choice_not_made):
        print("1: Go to the garage sale\n"
        "2: Show your inventory\n" 
        "3: Show score and exit game\n"
        "4: Learn more about the vendors")
        selected_answer = input("\nChoose an option:\n")
        match selected_answer:
            case "1":
                go_to_market()
                choice_not_made = False
            case "2":
                show_inventory()
            case "3":
                choice_not_made = False
                display_score_and_exit()
            case "4":
                show_vendor_info()
            case _:
                print(Fore.RED + "Something went wrong, select a number"
                "between 1-4")
                print(Style.RESET_ALL)
    

def go_to_market():
    """
    Allows user to choose which vendor to meet
    """
    choice = ""
    choice_not_made = True
    while(choice_not_made):
        print(Fore.GREEN + "\nWelcome to the garage sale! Choose a"
        "table to visit.")
        print(Style.RESET_ALL)
        print("1: Jim\n"
        "2: Michael\n" 
        "3: Angela\n"
        "4: Kevin\n"
        "5: Phyllis")
        selected_answer = input("\nChoose an option:\n")
        match selected_answer:
            case "1":
                choice = jim
                choice_not_made = False
            case "2":
                choice = michael
                choice_not_made = False
            case "3":
                choice = angela
                choice_not_made = False
            case "4":
                choice = kevin
                choice_not_made = False
            case "5":
                choice = phyllis
                choice_not_made = False
            case _:
                print(Fore.RED + "Something went wrong, select a number"
                "between 1-5")
                print(Style.RESET_ALL)
    visit_vendor(choice)

def visit_vendor(vendor):
    """
    Displays the chosen vendors inventory
    """
    print(Fore.GREEN + f"\n{vendor.welcome}")
    print(Style.RESET_ALL)
    items_list = vendor.items
    for item in items_list:
        print(f"{(items_list.index(item)+1)}: {item["item"].capitalize()}")
    
    item_input = True
    while(item_input):
        try:
            chosen_number = int(input("What would you like to trade?"
            f"(1-{len(items_list)}):\n"))
            if chosen_number > 0 and chosen_number <= len(items_list):
                item_input = False
                i = chosen_number - 1
                chosen_item = items_list[i]
                trade(chosen_item, vendor)
            else: 
                print(f"Something went wrong, select a number between"
                f"1-{len(items_list)}")
        except ValueError:
            print(f"Something went wrong, select a number between"
                f"1-{len(items_list)}")

            

def trade(item, vendor):
    """
    Users trade offer is tested
    If accepted - user and vendor inventory updated
    """
    player_value = player.items["value"] * player.luck
    vendor_value = item["value"] * vendor.sale
    if player_value >= vendor_value:
        new_user_item = item
        new_vendor_item = player.items
        print(Fore.GREEN + f"\n{vendor.name}: I will accept that deal."
         "Here you go.")
        print(Style.RESET_ALL)
        print("-- Trade went through, inventory updated --\n")
        player.items = new_user_item
        vendor.items.append(new_vendor_item)
        vendor.items.remove(item)   
    else:
        print(Fore.CYAN + f"\n{vendor.name}: That's not a good trade for me."
        f"Your {player.items["item"]} is not worth enough.")
        print(Style.RESET_ALL)
        print("-- Trade failed --\n")
    game_menu()
    

def show_inventory():
    """
    Displays the users inventory
    """
    print(f"\nYou have: {player.items["item"].capitalize()}\n")

def show_vendor_info():
    """
    Display info about the vendors
    """
    print("There are five vendors at the garage sale:\n"
        "Jim - A tall, skinny guy who is always happy."
        "Would love to trade with you!\n"
        "Michael - A man in a ill fitting suit. Not the best negotiator.\n"
        "Angela - A tiny, tiny woman with a stylish cross around her neck."
        "Doesn't seem to care for you. \n"
        "Kevin - A big, bald guy. His items seem to consist of mostly"
        "food and music related stuff.\n"
        "Phyllis - Kind of looks like your grandma. Her husband seems"
        "to be with her aswell.\n")

def display_score_and_exit():
    """
    Displays score and exits game
    """
    print(f"Your inventory is worth ${player.items["value"]},"
    f"good job {player.username}!")

    exit_answer = True
    while (exit_answer):
        answer = input("Are you ready to exit game? (Y/N):\n").lower()
        if answer == "y":
            print(Fore.GREEN + "Thank you for playing!")
            print(Style.RESET_ALL)
            exit()
            exit_answer = False
        elif answer == "n":
            print(Fore.GREEN + "Let's go back to the menu"
            "and trade some more!")
            print(Style.RESET_ALL)
            game_menu()
            exit_answer = False
        else:
            print(Fore.RED + "Something went wrong, please input"
            "the letter 'Y' or 'N'")
            print(Style.RESET_ALL)

def main():
    """
    Runs the game
    """
    display_instructions()
    input_username()
    game_menu()
   

if __name__ == "__main__": 
    main()





