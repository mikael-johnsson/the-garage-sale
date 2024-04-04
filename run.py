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
    player.username = input("Enter username here: ")
    print("It is time to start the game. Let the great experiment begin!\n")
    
def game_menu():
    """
    Displays a menu to allow the user to choose what to do in the game
    """
    choice = ""
    choice_not_made = True
    while(choice_not_made):
        print("1: Trade with Ron\n"
        "2: Show your inventory\n" 
        "3: Show score and exit game\n"
        "4: Learn more about the vendors")
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
    visit_vendor(choice)

def visit_vendor(vendor):
    """
    Displays the chosen vendors inventory
    """
    this_vendor = vendor
    print("This is my inventory: \n")
    items_list = vendor["items"]
    for item in items_list:
        print(f"{(items_list.index(item)+1)}: {item["item"].capitalize()}, {item["quantity"]} pcs")
    
    answer = input("\nWould you like to make a trade? (Y/N): ") #this need some error handling
    if answer.lower() == "n":
        print("Let us go back to the menu then.")
        game_menu()

    elif answer.lower() == "y":
        chosen_number = int(input(f"What would you like to trade? (1-{len(items_list)}): "))
        i = chosen_number - 1
        chosen_item = items_list[(i)]
        print("I have that item!")
        print(f"I have this amount of that: {items_list[(i)]["quantity"]}\n")

        chosen_qnt = int(input("How many do you want? ")) #this need some error handling
        if chosen_qnt <= items_list[(i)]["quantity"]:
                print("I can make that trade")
                trade(chosen_item, chosen_qnt, this_vendor)
        else: 
            print("I dont have that many")
            game_menu()

    else:
        print("Please answer Y or N")

def trade(item, quantity, vendor):
    """
    Users trade offer is tested
    If accepted - user and vendor inventory updated
    """
    player_value = player.items["value"] * player.items["quantity"] * player.luck
    vendor_value = item["value"] * quantity * vendor["sale modifier"] 
    if player_value >= vendor_value:
        new_user_item = item
        new_vendor_item = player.items
        print("Trade went through!")
        player.items = new_user_item
        player.items["quantity"] = quantity
        vendor["items"].append(new_vendor_item)
        vendor["items"].remove(item)
    
        
    else:
        print("That's a bad trade for me")
    game_menu()
    

def show_inventory():
    """
    Displays the users inventory
    """
    print(f"You have: {user["items"]["quantity"]} {user["items"]["item"]}")

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
    print(f"Your inventory sold for ${user["items"]["value"]}, good job!")

    exit_answer = True
    while (exit_answer):
        answer = input("Are you ready to exit game? (Y/N):").lower()
        if answer == "y":
            print("You pressed y")
            exit()
            exit_answer = False
        elif answer == "n":
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
    input_username()
    game_menu()
   

if __name__ == "__main__": 
    player = User(1.2, {"item": "thumbtack", "value": 1, "quantity": 1}, "")
    main()




