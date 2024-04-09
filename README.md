# The Garage Sale
The Garage Sale is a trading game - the user visits a garage sale and tries to
trade up from thumbtack to the highest valuble item - the telescope. There are no prices at
the garage sale, the user must figure out which items the vendors are 
most likely to be willing to trade.

The game is inspired by *The Office* episode *Garage Sale*.

![Screenshot of the program at the game menu](assets/images/garage_sale_site_new.png)

Find the site [**here**](https://the-garage-sale-60683b5891c9.herokuapp.com/)

## Table of Contents
* [User Experience](#user-experience)
    * [How to play](#how-to-play)
    * [User Stories](#user-stories)
        * [Project Goals](#project-goals)
        * [User Goals](#user-goals)
* [Features](#features)
    * [Flowchart](#flowchart)
    * [Existing Features](#existing-features)
    * [Future Features](#future-features)
* [Technologies](#technologies-used)
    * [Languages](#languages)
    * [Libraries & Tools](#libraries--tools)
* [Testing](#testing)
* [Deployment](#deployment)
    * [Heroku](#heroku)
    * [How to fork](#how-to-fork)
    * [How to clone](#how-to-clone)
* [Credits](#credits)
* [Acknowledgments](#acknowledgments)


## User Experience
The Garage Sale game is a quick and in some way simple game. The user chooses when to finish the game. The amounts of allowed visits to the vendors are infinite but aswell as getting a higher valued item in the trade the user can receive a lower valued item.

### How to play
The user start with an inventory of a thumbtack. They can then choose to meet a vendor to trade that item with one of the five items the vendor possesses. If the vendor find the trade acceptable, the item changes hand. Aswell does the thumbtack. Hopefully, the users new item is more valuble than the thumbtack.

Some vendors are easier to trade with than other. Information about which to favor is available from the game menu.

When the user obtains the telescope or when they feel they have obtained the highest valuble item they can - they can go to the exit of the market and find out how valuble their item is. That value is their final score. Amounts of trades are counted and displayed aswell.
### User Stories

#### Project Goals
The goals of the project are:
* Create a game with no errors or crashes
* Deply the game in a way that it's playable when access to link is given
* Have recurring users (not measurable at the moment)

#### User Goals
As a user, I want to:
* In a clear and effective way, recieve the instructions to the game
* Play a game with no errors or crashes
* Feel the game's difficulty level is balanced
* Be able to see my final score


## Features
### Flowchart
Below is the flowchart for the application:

![Flowchart for the application](assets/images/Flowchart_the_garage_sale_V2.png)

For readability purposes the vendor section of the flowchart has been taken out and specified in it's own flowchart. Not included in the flowchart are the big amounts of input error handling happening throughout the application.
### Existing Features
**Instructions**

The first thing the user meets are the instructions of the game. They explain the goal of the game, when and how to see the final score and also when and how to exit the game.

![Screenshot of the game instructions](assets/images/features_instructions.png)

**Username input**

The user is asked to input a username. The username is later used for a more personal touch to the game. If the user does not provide the application with a username or inputs only blank spaces, an error message is shown and the user gets another try.

![Screeenshot of the username input](assets/images/features_username.png)

**Game menu**

The game menu stands out with it's magenta color. It's to here the user is redirected after every feature is worked through.

From the game menu you can reach:
* the vendors
* your inventory
* your score and way to exit the game
* info about the vendors

![Screenshot of the game menu](assets/images/features_game_menu.png)

**Show inventory**

If "show inventory" option is chosen, the users inventory will displayed. Then returns the user to "Game menu".

![Screenshot of the show inventory feature](assets/images/features_inventory.png)

**Show score and exit**

If "show score and exit" option is chosen, the value of the users current inventory, i.e. the current score, is displayed. The user is thereafter given to option to exit the game or continue playing.

![Screenshot of the show score and exit function](assets/images/features_show_score.png)

**Learn more about the vendors**

If "learn more about the vendors" option is chosen, information about the five different vendors are displayed. A cunning player obtain information which of the different vendors are easy / hard to trade with. Then returns the user to "Game menu".

![Screenshot of the learn more about the vendors feature](assets/images/features_show_vendor_info.png)

**Go to the garage sale**

If "Go to garage sale" option is chosen, the user is displayed with five different vendors to trade with.

![Screenshot of the garage sale menu](assets/images/features_garage_sale.png)

**Vendors**

When meeting with the vendors, their five items are displayed and the user is asked which item they would like to trade.

![Screenshot of the vendors item menu](assets/images/features_vendors.png)

**Trading**

If the vendor find the users item to be worth equal to or more then the chosen item the trade is successful. A message is shown and the user is taken back to the game menu and can now find their new item in their inventory.

If the vendor find the users item to be worth less than the chosen item, a message is shown and the user is taken back to the game menu.

![Screenshot of a successful trade](assets/images/features_trade_success.png)

![Screenshot of an unsuccessful trade](assets/images/features_trade_unsuccess.png)

### Future Features
In the feature it would be prefferable to implement these features:
 * A quantity factor (a vendor can possess several items of the same category)
 * An online highscore, to allow the user to compare themselves to other users
 * A feature to allow the user to negotiate with or influate the vendor

## Technologies Used
### Languages
This application was created with Python version 3.12.2.
### Libraries & Tools
Colorama - to implement colors to the application

Git - for version control

Github - to save & store files during development

Lucidchart - for flowcharts

CI Linter - for validation

Heroku - for deployment

## Testing
How the application was tested can be found [**here**](TESTING.md)
## Deployment
### Heroku
This app was deployed by Heroku. These are the instructions to do that:

1. Sign in / create an account at [Heroku](https://www.heroku.com)
2. Create a new app by clicking "New" > "Create new app"
3. Choose a name and set region
4. Go to settings and click "Reveal Config Vars"
5. Add a config var of key: PORT value: 8000
6. Add buildpacks - add Python and nodejs (in that order)
7. Go to deploy section and choose a deplyoyment method. I used Github since that is were I store my code.
8. Connect the app to the repo containing your code
9. Click manual deployment. Your app is now deployed!

NOTE: If using match keyword in the code, first read Bug section in [TESTING.md](TESTING.md)
### How to fork
These are instructions how to fork the app from Github:

1. Sign in / create an account at [Github](https://www.github.com)
2. Go to the application's repository [*the-garage-sale*](https://github.com/mikael-johnsson/the-garage-sale)
3. Click "Fork" > "Create a new fork"
4. Choose an appropriate name and click "Create Fork"

### How to clone
These are instructions how to fork the app from Github:

1. Sign in / create an account at [Github](https://www.github.com)
2. Go to the application's repository [*the-garage-sale*](https://github.com/mikael-johnsson/the-garage-sale)
3. Click "Code"
4. Choose to clone via HTTPS, SSH-key or Github CLI
5. Go to IDE of choice, I chose Gitpod
6. Create workspace via chosen clone way from step 4

## Credits
* A tutorial by Code Institute were followed to create the workspace and deploy the application
* [This](https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python) Stack Overflow thread were used for learning to use the match keyword
* A reply in Slack by the user DiarmuidHenry_5p helped me with the deployment bug

## Acknowledgments
Big thank you to my Code Institute mentor Graeme Taylor for insightful tips and encouragement during the development.