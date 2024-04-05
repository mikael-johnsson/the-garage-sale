# python3 run.py
from data import *
from tabulate import tabulate

def display_instructions():
    """
    Displays title and instructions to the game
    """
    print("WELCOME TO THE GARAGE SALE\n")
    print("The game is simple: trade your thumbtack with higher valued items at one of the five vendors.\n"
    "Your score is the amount of cash your inventory is worth when leaving the market.\n"
    "Remember: the trade deal needs to be good for both you and the vendor - or they will deny the deal.\n")
    
    
def input_username():
    """
    Lets the user insert a username
    """
    player.username = input("Enter username here: ")
    print("\nIt is time to start the game. Let the great experiment begin!\n")
    
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
        selected_answer = input("\nChoose an option: ")
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
                print("Something went wrong, select a number between 1-3")
    

def go_to_market():
    """
    Allows user to choose which vendor to meet
    """
    choice = ""
    choice_not_made = True
    while(choice_not_made):
        print("\nWelcome to the garage sale! Choose a table to visit:\n"
        "1: Jim\n"
        "2: Michael\n" 
        "3: Angela\n"
        "4: Kevin\n"
        "5: Phyllis")
        selected_answer = input("\nChoose an option: ")
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
                print("Something went wrong, select a number between 1-5")
    visit_vendor(choice)

def visit_vendor(vendor):
    """
    Displays the chosen vendors inventory
    """
    
    print(f"\n{vendor.welcome} \n")
    items_list = vendor.items
    for item in items_list:
        print(f"{(items_list.index(item)+1)}: {item["item"].capitalize()}, {item["quantity"]} pcs")
    
    trade_input = True
    while (trade_input):
        answer = input("\nWould you like to make a trade? (Y/N): ")
        if answer.lower() == "n":
            trade_input = False
            print("\nLet us go back to the menu then.")
            game_menu()

        elif answer.lower() == "y":
            trade_input = False
            item_input = True
            while(item_input):
                try:
                    chosen_number = int(input(f"What would you like to trade? (1-{len(items_list)}): "))
                    item_input = False
                    i = chosen_number - 1
                    chosen_item = items_list[i]
                    print(f"\nSure thing, I have this amount of {items_list[i]["item"]}: {items_list[i]["quantity"]}\n")
                except ValueError:
                    print(f"Something went wrong, select a number between 1-{len(items_list)}")

            quantity_input = True
            while(quantity_input):
                try:
                    chosen_qnt = int(input("How many do you want? ")) 
                    if chosen_qnt == 0:
                            print("You cannot trade for zero of my item.")
                    elif chosen_qnt <= items_list[i]["quantity"]:
                        trade(chosen_item, chosen_qnt, vendor)
                    else: 
                        print("I don't have that many")
                        game_menu()
                except ValueError:
                    print(f"Something went wrong, select a number")

        else:
            print("Please answer Y or N")

def trade(item, quantity, vendor):
    """
    Users trade offer is tested
    If accepted - user and vendor inventory updated
    """
    player_value = player.items["value"] * player.items["quantity"] * player.luck
    vendor_value = item["value"] * quantity * vendor.sale
    if player_value >= vendor_value:
        new_user_item = item
        new_vendor_item = player.items
        print(f"\n{vendor.name}: I will accept that deal. Here you go.\n"
        "-- Trade went through, inventory updated --\n")
        player.items = new_user_item
        player.items["quantity"] = quantity
        vendor.items.append(new_vendor_item)
        vendor.items.remove(item)   
    else:
        print(f"\n{vendor.name}: That's not a good trade for me.\n"
        "-- Trade failed --\n")
    game_menu()
    

def show_inventory():
    """
    Displays the users inventory
    """
    print(f"\nYou have: {player.items["quantity"]} {player.items["item"].capitalize()}\n")

def show_vendor_info():
    """
    Display info about the vendors
    """
    print("There are five vendors at the garage sale:\n"
        "Jim - A tall, skinny guy who is always happy. Would love to trade with you!\n"
        "Michael - A man in a ill fitting suit. Not the best negotiator.\n"
        "Angela - A tiny, tiny woman with a stylish cross around her neck. Doesn't seem to care for you. \n"
        "Kevin - A big, bald guy. His items seem to consist of mostly food and music related stuff.\n"
        "Phyllis - Kind of looks like your grandma. Her husband seems to be with her aswell.\n")

def display_score_and_exit():
    """
    Displays score and exits game
    """
    print(f"Your inventory is worth ${player.items["value"]}, good job {player.username}!")

    exit_answer = True
    while (exit_answer):
        answer = input("Are you ready to exit game? (Y/N):").lower()
        if answer == "y":
            print("Thank you for playing!")
            exit()
            exit_answer = False
        elif answer == "n":
            print("Let's go back to the menu and trade some more!")
            game_menu()
            exit_answer = False
        else:
            print("Something went wrong, please input the letter 'Y' or 'N'")

def main():
    """
    Runs the game
    """
    display_instructions()
    input_username()
    game_menu()
   

if __name__ == "__main__": 
    main()





