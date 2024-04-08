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
jim = Vendor("Jim", "Jim: Hi there, want to trade something?"
            "Take whatever you want!", 
            0.7, 
            [{"item": "stapler", "value": 1.3},
            {"item": "teapot", "value": 3},
            {"item": "magic beans", "value": 4.9},
            {"item": "telescope","value": 10},
            {"item": "keyboard", "value": 5.4}])

michael = Vendor("Michael", "Michael: Welcome to my table!"
                "My items are so big- THAT'S WHAT SHE SAID!", 
                0.6, 
                [{"item": "coffee mug","value": 0.8},
                {"item": "reem of paper", "value": 0.5},
                {"item": "award","value": 1.5},
                {"item": "cented candle","value": 2.2},
                {"item": "plasma tv","value": 7.1}
                ])

kevin = Vendor("Kevin", "Kevin: Hi... I'm Kevin. This is items. We trade.", 
                0.7, 
                [{"item": "pot of chili","value": 4.1},
                {"item": "drum kit","value": 9},
                {"item": "cookie","value": 0.9},
                {"item": "calculator","value": 2.3},
                {"item": "ice cream cone","value": 1.1}
                ])

angela = Vendor("Angela", "Angela: Good afternoon. Before you I lay"
                "several quite valuble objects.", 
                1, 
                [{"item": "wood cross","value": 3.7},
                {"item": "baby jesus statue","value": 5.9},
                {"item": "open toe shoes","value": 2.9},
                {"item": "bible","value": 3.4},
                {"item": "used cat toy","value": 1}
                ])

phyllis = Vendor("Phyllis", "Phyllis: Oh, hello! Please, come take a look."
                "Have you met my husband, Bob Vance, Vance Refrigiration?", 
                0.8,
                [{"item": "used mini fridge","value": 8.2},
                {"item": "oven mitt","value": 2.5},
                {"item": "santa costume","value": 7.8},
                {"item": "ice cream cake","value": 1.9},
                {"item": "luxury make up kit","value": 6.5}
                ])

                