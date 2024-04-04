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
jim = Vendor("Jim: Hi there, want to trade something? Take whatever you want!", 0.8, 
            [{"item": "stapler", "value": 1.2,"quantity": 1},
            {"item": "teapot", "value": 4, "quantity": 1},
            {"item": "magic beans", "value": 6, "quantity": 1},
            {"item": "telescope","value": 12, "quantity": 1},
            {"item": "keyboard", "value": 7, "quantity": 3}])
"""
michael = Vendor("welcome message", sale_m, 
                [{"item": " ","value": ,"quantity":},
                {"item": " ","value": ,"quantity":}
                {"item": " ","value": ,"quantity":}
                {"item": " ","value": ,"quantity":}
                {"item": " ","value": ,"quantity":}
                ])

kevin = Vendor("welcome message", sale_m, 
                [{"item": " ","value": ,"quantity":},
                {"item": " ","value": ,"quantity":}
                {"item": " ","value": ,"quantity":}
                {"item": " ","value": ,"quantity":}
                {"item": " ","value": ,"quantity":}
                ])

angela = 

phyllis = 
"""
                