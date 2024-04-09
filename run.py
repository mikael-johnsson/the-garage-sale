from data import *
from colorama import Fore, Back, Style, init
init(autoreset = True)

def display_instructions():
    """
    Displays title and instructions to the game
    """
    print(Fore.GREEN + "WELCOME TO THE GARAGE SALE\n") 
    print("The game is simple: trade your thumbtack with higher valued items"
    " at one of the five vendors.\n"
    "Your score is the amount of cash your inventory is worth when leaving"
    " the market. If you are really good you reach the most valuble item - the telescope.\n"
    "Remember: the trade deal needs to be good for both you and the vendor -"
    " or they will deny the deal.\n")
    
def input_username():
    """
    Lets the user input a username
    """
    while(True):
        player.username = input("Enter username here:\n")
        if not player.username.strip():
            print(Fore.RED + "\nPlease enter a username")
        else:
            print(Fore.GREEN + "\nIt is time to start the game."
            " Let the great experiment begin!\n")
            break
    
def game_menu():
    """
    Displays a menu to allow the user to choose what to do in the game
    """
    choice = ""
    while(True):
        print(Fore.MAGENTA + "GAME MENU\n")
        print("1: Go to the garage sale\n"
        "2: Show your inventory\n" 
        "3: Show score and exit game\n"
        "4: Learn more about the vendors")
        selected_answer = input("\nChoose an option:\n")
        match selected_answer:
            case "1":
                go_to_market()
            case "2":
                player.inventory()
            case "3":
                display_score_and_exit()
            case "4":
                show_vendor_info()
            case _:
                print(Fore.RED + "Something went wrong, select a number"
                "between 1-4\n")
    
def go_to_market():
    """
    Allows user to choose which vendor to meet
    """
    choice = ""
    while(True):
        print(Fore.GREEN + "\nWelcome to the garage sale! Choose a"
        " table to visit.\n")
        print("1: Jim\n"
        "2: Michael\n" 
        "3: Angela\n"
        "4: Kevin\n"
        "5: Phyllis")
        selected_answer = input("\nChoose an option:\n")
        match selected_answer:
            case "1":
                choice = jim
                break
            case "2":
                choice = michael
                break
            case "3":
                choice = angela
                break
            case "4":
                choice = kevin
                break
            case "5":
                choice = phyllis
                break
            case _:
                print(Fore.RED + "Something went wrong, select a number "
                "between 1-5\n")
    visit_vendor(choice)

def visit_vendor(vendor):
    """
    Displays the chosen vendors inventory
    """
    print(Fore.GREEN + f"\n{vendor.welcome}\n")
    items_list = vendor.items
    for item in items_list:
        print(f"{(items_list.index(item)+1)}: {item["item"].capitalize()}")
    while(True):
        try:
            chosen_number = int(input("What would you like to trade? "
            f"(1-{len(items_list)}):\n"))
            if chosen_number > 0 and chosen_number <= len(items_list):
                i = chosen_number - 1
                chosen_item = items_list[i]
                trade(chosen_item, vendor)
                break
            else: 
                raise ValueError
        except ValueError:
            print(Fore.RED + f"Something went wrong, select a number between "
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
         " Here you go.\n")
        print("-- Trade went through, inventory updated --\n")
        player.items = new_user_item
        player.trades += 1
        vendor.items.append(new_vendor_item)
        vendor.items.remove(item)   
    else:
        print(Fore.CYAN + f"\n{vendor.name}: That's not a good trade for me. "
        f"Your {player.items["item"]} is not worth enough.\n")
        print("-- Trade failed --\n")
    game_menu()


def show_vendor_info():
    """
    Display info about the vendors
    """
    print(Fore.GREEN + "\nThere are five vendors at the garage sale:\n")
    print(
        "Jim - A tall, skinny guy who is always happy."
        " Would love to trade with you! Most valuble item is the telescope.\n"
        "Michael - A man in a ill fitting suit. Not the best negotiator. Most valuble item is the plasma tv.\n"
        "Angela - A tiny, tiny woman with a stylish cross around her neck."
        " Doesn't seem to care for you. Most valuble item is the baby jesus statue \n"
        "Kevin - A big, bald guy. His items seem to consist of mostly"
        " food and music related stuff. Most valuble item is the drum kit.\n"
        "Phyllis - Kind of looks like your grandma. Her husband seems"
        " to be with her aswell. Most valuble item is the used mini fridge.\n")

def display_score_and_exit():
    """
    Displays score and exits game
    """
    print(Fore.GREEN + "\nSCORE\n")
    print(f"In {player.trades} trades you have reached a value of ${player.items["value"]},"
    f" good job {player.username}!")
    while (True):
        answer = input("Are you ready to exit game? (Y/N):\n").lower()
        if answer == "y":
            print(Fore.GREEN + "\nThank you for playing!\n")
            exit()
            break
        elif answer == "n":
            print(Fore.GREEN + "Let's go back to the menu"
            " and trade some more!\n")
            game_menu()
            break
        else:
            print(Fore.RED + "Something went wrong, please input"
            " the letter 'Y' or 'N'\n")

def main():
    """
    Runs the game
    """
    display_instructions()
    input_username()
    game_menu()

if __name__ == "__main__": 
    main()





