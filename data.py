ron = {"welcome message": "Ron: Hello. This is my table of stuff. Trade something if you want, I don't care.",
        "sale modifier" : 1,
        "items": [{"item": "axe",
                "value": 7,
                "quantity": 1},
                {"item": "mustache trimmer",
                "value": 1,
                "quantity": 2}] 
    }

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

player = User(1.2, {"item": "thumbtack", "value": 1, "quantity": 1}, "")

class Vendor:
    """
    Creates vendor
    """
    def __init__(self, welcome_message, sale_modifier, items):
        self.welcome = welcome_message
        self.sale = sale_modifier
        self.items = items

#Vendor objects
jim = Vendor("Jim: Hi there, want to trade something? Take whatever you want!", 0.7, 
            [{"item": "stapler", "value": 1.2,"quantity": 1},
            {"item": "teapot", "value": 4, "quantity": 1},
            {"item": "magic beans", "value": 6, "quantity": 1},
            {"item": "telescope","value": 12, "quantity": 1},
            {"item": "keyboard", "value": 7, "quantity": 3}])

michael = Vendor(f"Michael: Welcome to my table {player.username}! My items are big - THAT'S WHAT SHE SAID!", 0.6, 
                [{"item": "coffee mug","value": 0.8,"quantity": 1},
                {"item": "reem of paper","value": 0.5,"quantity": 10}
                {"item": "an award","value": 2,"quantity": 3}
                {"item": "cented candle","value": 3,"quantity": 2}
                {"item": "plasma tv","value": 9,"quantity": 1}
                ])

kevin = Vendor("Kevin: Hi... I'm Kevin. This is items. We trade.", 0.7, 
                [{"item": "pot of chili","value": 6,"quantity": 1},
                {"item": "drum kit","value": 13,"quantity": 1}
                {"item": "cookie","value": 0.8,"quantity":10}
                {"item": "calculator","value": 3,"quantity":2}
                {"item": "ice cream cone","value": 1,"quantity": 4}
                ])

angela = Vendor("Angela: Good afternoon. Before you I lay several quite valuble objects.", 1, 
                [{"item": "wood cross","value": 5,"quantity": 1},
                {"item": "baby jesus statue","value": 7,"quantity": 1}
                {"item": "open toe shoes","value": 3,"quantity": 3}
                {"item": "bible","value": 3,"quantity": 2}
                {"item": "used cat toy","value": 1,"quantity": 4}
                ])

phyllis = Vendor("Phyllis: Oh, hello! Please, come take a look. Have you met my husband, Bob Vance, Vance Refrigiration?", 0,8, 
                [{"item": "used mini fridge","value": 11,"quantity": 1},
                {"item": "oven mitt","value": 4,"quantity": 4}
                {"item": "santa costume","value": 10,"quantity": 1}
                {"item": "ice cream cake","value": 3,"quantity": 3}
                {"item": "luxury make up kit","value": 11,"quantity": 1}
                ])

                