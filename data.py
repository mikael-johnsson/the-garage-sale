class User:
    """
    Creates user
    """
    def __init__(self, luck, items, username):
        self.luck = luck
        self.items = items
        self.username = username

    def inventory(self):
        print(self.items["item"].capitalize())

player = User(1.2, {"item": "thumbtack", "value": 1}, "")

class Vendor:
    """
    Creates vendor
    """
    def __init__(self, name, welcome_message, sale_modifier, items):
        self.name = name
        self.welcome = welcome_message
        self.sale = sale_modifier
        self.items = items

#Vendor objects
jim = Vendor("Jim", "Jim: Hi there, want to trade something? Take whatever you want!", 0.7, 
            [{"item": "stapler", "value": 1.2},
            {"item": "teapot", "value": 4},
            {"item": "magic beans", "value": 6},
            {"item": "telescope","value": 12},
            {"item": "keyboard", "value": 7}])

michael = Vendor("Michael", f"Michael: Welcome to my table{player.username}! My items are big - THAT'S WHAT SHE SAID!", 0.6, 
                [{"item": "coffee mug","value": 0.8},
                {"item": "reem of paper", "value": 0.5},
                {"item": "award","value": 2},
                {"item": "cented candle","value": 3},
                {"item": "plasma tv","value": 9}
                ])

kevin = Vendor("Kevin", "Kevin: Hi... I'm Kevin. This is items. We trade.", 0.7, 
                [{"item": "pot of chili","value": 6},
                {"item": "drum kit","value": 13},
                {"item": "cookie","value": 0.8},
                {"item": "calculator","value": 3},
                {"item": "ice cream cone","value": 1}
                ])

angela = Vendor("Angela", "Angela: Good afternoon. Before you I lay several quite valuble objects.", 1, 
                [{"item": "wood cross","value": 5},
                {"item": "baby jesus statue","value": 7},
                {"item": "open toe shoes","value": 3},
                {"item": "bible","value": 3},
                {"item": "used cat toy","value": 1}
                ])

phyllis = Vendor("Phyllis", "Phyllis: Oh, hello! Please, come take a look. Have you met my husband, Bob Vance, Vance Refrigiration?", 0.8,
                [{"item": "used mini fridge","value": 11},
                {"item": "oven mitt","value": 4},
                {"item": "santa costume","value": 10},
                {"item": "ice cream cake","value": 3},
                {"item": "luxury make up kit","value": 11}
                ])

                