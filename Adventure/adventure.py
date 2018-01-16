from game_data import World, Item, Location
from player import Player


def do_menu_action(action, location, player, world):
    ''' (str, Location, Player, World) -> None
    The function will do all the options
    in [menu], which includes the following:
    look
    inventory
    score
    quit
    back

    Also, there is another submenu in inventory to
    let player to drop items in their inventory.
    '''
    # if action is look then print the long description
    if action == 'look':
        print('\n' + location.ldescrip)
    # if action is inventory
    elif action == 'inventory':
        print('')
        # get the inventory list
        inventory = player.get_inventory()
        # if list contains something
        if inventory != []:
            # get the items names based on object
            items_names = [inventory[i].get_name()
                           for i in range(len(inventory))]
            print("You got " + str(len(items_names)) + "/3 items:")
            # loop through each item in the list
            # and print their info
            for item in inventory:
                name = 'Name: ' + item.get_name() + '; '
                start = 'Starts: ' + str(item.get_starting_location()) + '; '
                points = 'Points: ' + str(item.get_target_points())
                print(name + start + points + '\n')

            # ask player if he/she wants to drop
            print("Do you want to drop something here?")
            choice = ''
            while choice not in ['Yes', 'No']:
                choice = input("Please Choose Yes/No: ")
            # if drop then ask drop which item
            if choice == 'Yes':
                while choice not in items_names + ['back']:
                    choice = input("Please enter the name to drop or back: ")
                # if player wants to drop one item
                if choice in items_names:
                    # del item object from inventory list
                    index = items_names.index(choice)
                    item = inventory[index]
                    del inventory[index]
                    # if drop into the correct place
                    # get the points and item disappear
                    if location.num == item.get_target_location():
                        player.add_score(item.get_target_points())
                    # otherwise, no points, and player
                    # can still pick them
                    else:
                        location.items.append(item)
                    # count the movement
                    player.count_move()
        # if list is empty
        else:
            print("You got nothing!")
    # get the score if wants to check
    elif action == 'score':
        print('\n' + str(player._score))
    # quit the game if player wants
    elif action == 'quit':
        player.victory = True


if __name__ == "__main__":
    WORLD = World("map.txt", "locations.txt", "items.txt")
    PLAYER = Player(1, 1)  # set starting location of player;
    # you may change the x, y coordinates here as appropriate
    # MOVE is the limited movements, the player has to
    # finish within this num of movements
    MOVE = 32

    menu = ["look", "inventory", "score", "quit", "back"]

    # ge the total score of all the items
    total_score = 0
    for item in WORLD.items.values():
        total_score += item.target_points

    # to start the game
    while not PLAYER.victory:
        location = WORLD.get_location(PLAYER.x, PLAYER.y)
        location.refresh_points()
        # ENTER CODE HERE TO PRINT LOCATION DESCRIPTION
        # depending on whether or not it's been visited before,
        # print either full description (first time visit) or
        # brief description (every subsequent visit)
        # if location has been visited, print short description
        if location.has_visit:
            print("Location " + str(location.num))
            print(location.bdescrip)
        # print long one if first visit
        else:
            print("Location " + str(location.num))
            print(location.ldescrip)
            location.has_visit = True

        # print all the action that player can do
        print("What to do? \n")
        print("[menu]")
        # check points in curr location
        print("[hint]")
        for action in location.available_actions():
            print(action)
        choice = input("\nEnter action: ")

        if (choice == "[menu]"):
            print("Menu Options: \n")
            for option in menu:
                print(option)
            choice = input("\nChoose action: ")

        # CALL A FUNCTION HERE TO HANDLE WHAT HAPPENS UPON USER'S CHOICE
        # REMEMBER: the location = w.get_location(p.x, p.y) at the top of
        #    this loop will update the location if the
        #    choice the user made was just a movement, so only updating
        #    player's position is enough to change
        #    the location to the next appropriate location
        # Possibilities: a helper function do_action(WORLD, PLAYER,
        #   location, choice)
        # OR A method in World class WORLD.do_action(PLAYER, location, choice)
        # OR Check what type of action it is, then modify only player
        # or location accordingly
        # OR Method in Player class for move or updating inventory
        # OR Method in Location class for updating location item info, or other
        # location data
        # etc....
            while choice not in menu:
                # if action not in the menu
                print("\nThat is not the verb I recognized.")
                choice = input("Please choose action: ")
            # call the helper function
            do_menu_action(choice, location, PLAYER, WORLD)

        elif choice == "[hint]":
            print("\nYou may get", location.target_points,
                  "points from items in current location\n")

        # if action starts with Go
        elif choice.startswith('Go'):
            # get the x and y
            direction, x, y = choice[3:], PLAYER.x, PLAYER.y
            right_direction = True
            # determine which direction the player wants to go
            if direction == 'north':
                y -= 1
            elif direction == 'south':
                y += 1
            elif direction == 'east':
                x += 1
            elif direction == 'west':
                x -= 1
            else:
                right_direction = False
            # if direction is improper
            if not right_direction:
                print("\nThat is not the direction I recognized.")
            # move to the direction
            elif WORLD.get_location(x, y) is not None:
                PLAYER.x, PLAYER.y = x, y
                # count the movement
                PLAYER.count_move()
            # if direction does not exist
            else:
                print("\nOops... You can not go there.")

        # if action starts with Check
        elif choice.startswith('Check'):
            # get all the items name
            items = [location.items[i].get_name()
                     for i in range(len(location.items))]
            # if choice exists
            if choice[6:] in items:
                # get the item index
                item = items.index(choice[6:])
                # print name, points and location of that item
                print("\nName: " + location.items[item].get_name())
                print("Target points: " +
                      str(location.items[item].get_target_points()))
                print("Starts: Location " +
                      str(location.items[item].get_starting_location()))
                # create a sub menu includes pick and back
                sub_menu = ["pick", "back"]
                while choice not in sub_menu:
                    print("Menu Options: \n")
                    # print all the action for sub menu
                    for option in sub_menu:
                        print(option)
                    # ask for next action
                    choice = input("\nPlease choose action: ")
                # if action is pick, them pick it into inventory
                # and delete it into current location
                if choice == 'pick' and not PLAYER.is_too_much_items():
                    PLAYER.add_item(location.items[item])
                    del location.items[item]
            # if item does not exist
            else:
                print("\nYou can not check it.")
            # count movement
            PLAYER.count_move()

        # if action is in a improper form
        else:
            print("\nThat is not the verb I recognized.")

        # after each action, check whether wins
        if PLAYER.get_score() == total_score:
            PLAYER.victory = True

    # After the game is finish, we will determine that
    # whether PLAYER wins or loses.
    # Since if we can end the game by quit or finish all
    # steps. We need to determine
    # whether the player finished in allowed steps
    # or he/she just quit
    # if movements are too large
    if PLAYER.get_move() > MOVE:
        print("\nYour move has exceed our allowed steps\nGame Over\n")
    # steps within the movement, then player wins
    elif PLAYER.get_score() == total_score:
        print("\nWinning\n")
    # if player quit, then game over
    else:
        print("\nGame Over\n")
