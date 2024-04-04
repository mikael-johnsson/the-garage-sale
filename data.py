"""user = {"luck modifier": 1.2,
        "items" : {"item": "thumbtack",
                    "value": 1,
                    "quantity": 1}
    }"""

ron = {"welcome message": "Hello. This is my table of stuff. Trade something if you want, I don't care.",
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