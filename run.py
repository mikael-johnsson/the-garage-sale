def display_instructions():
    print("WELCOME TO THE TRADE GAME\n")
    print("The game is simple: trade your thumbtack with higher valued items at one of the five vendors. \nIn ten rounds, your aim is to trade your inventory up as high as you can!")
    print("Your score is the amount of cash you receive when selling your items when leaving the market.")
    input_username()

def input_username():
    username = Input(Enter username here:)
    return username
    
display_instructions()