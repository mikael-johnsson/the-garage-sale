# python3 run.py

def display_instructions():
    print("WELCOME TO THE TRADE GAME\n")
    print("The game is simple: trade your thumbtack with higher valued items at one of the five vendors. \nIn ten rounds, your aim is to trade your inventory up as high as you can!")
    print("Your score is the amount of cash you receive when selling your items when leaving the market.")
    

def input_username():
    username = input("Enter username here:")
    return username
    
def game_menu():
    print("1: Trade with Ron\n"
        "2: Show your inventory\n" 
        "3: Show score and exit game")
    choice = ""
    choice_not_made = True
    while(choice_not_made):
        selected_answer = input("Choose a path:")
        match selected_answer:
            case "1":
                choice = "1"
                choice_not_made = False
            case "2":
                choice = "2"
                choice_not_made = False
            case "3":
                choice = "3"
                choice_not_made = False
            case _:
                print("Something went wrong, select a number between 1-3")
    return choice

def main():
    display_instructions()
    username = input_username()
    print(game_menu())
    

main()