class Location:

    def __init__(self, num, points, position, bdescrip,
                 ldescrip, directions=[], items=[]):
        '''Creates a new location.

        Data that could be associated with each Location object:
        a position in the world map,
        a brief description,
        a long description,
        a list of available commands/directions to move,
        items that are available in the location,
        and whether or not the location has been visited before.
        Store these as you see fit.
        '''
        self.num = num
        self.target_points = points
        self.position = position
        self.bdescrip = bdescrip
        self.ldescrip = ldescrip
        self.items = items[:]
        self.directions = directions
        self.has_visit = False

    def get_brief_description(self):
        '''Return str brief description of location.'''

        return self.bdescrip

    def get_full_description(self):
        '''Return str long description of location.'''

        return self.ldescrip

    def available_actions(self):
        '''
        -- Suggested Method (You may remove/modify/rename this as you like) --
        Return list of the available actions in this location.
        The list of actions should depend on the items
        available in the location
        and the x,y position of this location on the world map.'''

        actions = ['Go ' + direction for direction in self.directions]
        for item in self.items:
            actions.append('Check ' + item.name)
        return actions

    def refresh_points(self):
        '''
        The method will refresh the points that exist in current
        location.'''

        self.target_points = 0
        for item in self.items:
            self.target_points += item.get_target_points()


class Item:

    def __init__(self, name, start, target, target_points):
        '''Create item referred to by string name, with integer "start"
        being the integer identifying the item's starting location,
        the integer "target" being the item's target location, and
        integer target_points which is the number of points player gets
        if item is deposited in target location.

        This is just a suggested starter class for Item.
        You may change these parameters and the data available for each
        Item class as you see fit.
        Consider every method in this Item class as a "suggested method":
        -- Suggested Method (You may remove/modify/rename these as you like) --

        The only thing you must NOT change is the name of this class: Item.
        All item objects in your game MUST be represented as an instance
        of this class.
        '''

        self.name = name
        self.start = start
        self.target = target
        self.target_points = target_points

    def get_starting_location(self):
        '''Return int location where item started.'''

        return self.start

    def get_name(self):
        '''Return the str name of the item.'''

        return self.name

    def get_target_location(self):
        '''Return item's int target location.'''

        return self.target

    def get_target_points(self):
        '''Return int points awarded for depositing the item in
        its target location.'''

        return self.target_points


class World:

    def __init__(self, mapdata, locdata, itemdata):
        '''
        Creates a new World object, with a map, and data about every
        location and item in this game world.

        You may add parameters/attributes/methods to this class as you see fit.
        BUT DO NOT RENAME OR REMOVE ANY EXISTING METHODS/ATTRIBUTES.

        :param mapdata: name of text file containing map data in grid format
        (integers represent each location, separated by space)
              map text file MUST be in this format.
              E.g.
              1 -1 3
              4 5 6
        Where each number represents a different location,
        and -1 represents an invalid, inaccessible space.
        param locdata: name of text file containing location data
        (format left up to you)
        param itemdata: name of text file containing item data
        (format left up to you)
        '''

        # The map MUST be stored in a nested list
        self.map = self.load_map(mapdata)
        # self.locations ... You may choose how to store location and item data
        # This data must be stored somewhere. Up to you how you choose to do it
        self.load_locations(locdata)
        # This data must be stored somewhere. Up to you how you choose to do it
        self.load_items(itemdata)

    def load_map(self, filename):
        '''
        THIS FUNCTION MUST NOT BE RENAMED OR REMOVED.
        Store map from filename (map.txt) in the variable "self.map"
        as a nested list of integers like so:
            1 2 5
            3 -1 4
        becomes [[1,2,5], [3,-1,4]]
        RETURN THIS NEW NESTED LIST.
        param filename: string that gives name of text file in which map data
        is located
        return: return nested list of integers representing map of
        game world as specified above
        '''
        # initializa nest list map
        map = []
        # read the file, and close it
        map_file = open(filename, 'r')
        lines = map_file.readlines()
        map_file.close()

        # loop through each line
        for line in lines:
            # clear the line
            line = line.strip('\n').split(' ')
            # loop through each num in line
            index = 0
            while index < len(line):
                # convert num into int
                line[index] = int(line[index])
                index += 1
            # add the line into map
            map.append(line)
        return map

    def load_locations(self, filename):
        '''
        Store all locations from filename (locations.txt) into the variable
        "self.locations"
        Remember to keep track of the integer number representing each location
        Make sure the Location class is used to represent each location.
        Change this docstring as needed.
        param filename:
           LOCATION location_number
           Short description
           Long description
           END
        becomes to {str: Location}
        '''
        # initialize locations as dict
        self.locations = {}
        # read lines, and close the file
        loca_file = open(filename, 'r')
        lines = loca_file.readlines()
        loca_file.close()

        # initialzie index, start, end for loop
        index = 0
        start = 0
        end = 0
        # loop through each line
        while index < len(lines):
            # if begins with location, get the index for start
            if lines[index].startswith('LOCATION'):
                start = index
            # if begins as END, get the index for end
            elif lines[index].startswith('END'):
                end = index
            index += 1
            # if end is not 0
            if end != 0:
                # get the location num, points, two descriptions
                loca_num = int(lines[start][9:].strip('\n'))
                points = int(lines[start+1].strip('\n'))
                bdescrip = lines[start+2].strip('\n')
                ldescrip_list = lines[start+3:end]
                # since long description is a list,
                # we need to invert it into a str
                ldescrip = ''
                # loop through each item and add together as a str
                for descrip in ldescrip_list:
                    ldescrip += descrip
                ldescrip = ldescrip[:-1]
                # add location object into dict
                self.locations[loca_num] = Location(loca_num, points,
                                                    [], bdescrip, ldescrip)
                # delete these part and initialize index, start, and end
                lines = lines[end+1:]
                index = 0
                start = 0
                end = 0

        # initialzie a and y for loop
        y = 0
        while y < len(self.map):
            x = 0
            while x < len(self.map[y]):
                # initialzie possible directions as list
                directions = []
                # use four statement to determine if
                # the player can go east, south, west, and north
                # if the next area is -1, which means
                # we can not go there
                if x != len(self.map[y]) - 1 and self.map[y][x+1] != -1:
                    directions.append('east')
                if y != len(self.map) - 1 and self.map[y+1][x] != -1:
                    directions.append('south')
                if x != 0 and self.map[y][x-1] != -1:
                    directions.append('west')
                if y != 0 and self.map[y-1][x] != -1:
                    directions.append('north')
                # add all the position and direction into location dict
                if self.map[y][x] in self.locations:
                    self.locations[self.map[y][x]].position.append((x, y))
                    self.locations[self.map[y][x]].directions = directions[:]
                x += 1
            y += 1

    def load_items(self, filename):
        '''
        Store all items from filename (items.txt) into self.items
        whatever you think is best.
        Make sure the Item class is used to represent each item.
        Change this docstring accordingly.
        param filename:
           num num num str ...
           start target target_points item's name
        becomes [Item]
        '''
        # read lines, and close the file
        items_file = open(filename, 'r')
        lines = items_file.readlines()
        items_file.close()
        self.items = {}

        # loop through each line
        for line in lines:
            # clear the line
            line = line.strip('\n').split(' ')
            # convert first three vavariable into int
            line[0] = int(line[0])
            line[1] = int(line[1])
            line[2] = int(line[2])
            # get the name list and clear line list
            name = line[3:]
            line = line[:3]
            line.append('')
            # loop through each word in name list and add it into line[3]
            for word in name:
                line[3] = line[3] + word + ' '
            line[3] = line[3][:-1]
            # create the object of Item
            item = Item(line[3], line[0], line[1], line[2])
            # add item into both items and locations.items
            self.items[line[3]] = item
            self.locations[line[0]].items.append(item)
            # add the target_points into locations
            self.locations[line[0]].target_points += line[2]

    def get_location(self, x, y):
        '''Check if location exists at location (x,y) in world map.
        Return Location object associated with this location if it does.
        Else, return None.
        Remember, locations represented by the number -1 on the map
        should return None.
        :param x: integer x representing x-coordinate of world map
        :param y: integer y representing y-coordinate of world map
        :return: Return Location object associated with this location
        if it does. Else, return None.
        '''

        # try to get the location
        try:
            loca_num = self.map[y][x]
            if loca_num == -1:
                return None
            location = self.locations[loca_num]
        # any error means location does not exist
        except:
            return None
        return location
