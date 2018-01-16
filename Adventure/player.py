class Player:

    def __init__(self, x, y):
        '''
        Creates a new Player.
        param x: x-coordinate of position on map, non-negative integer
        param y: y-coordinate of position on map, non-negative integer

        This is a suggested starter class for Player.
        You may add new parameters / attributes / methods to this class as you
        see fit. Consider every method in this Player class as a
        "suggested method":
        -- Suggested Method (You may remove/modify/rename these as you like) --
        '''
        self.x = x
        self.y = y
        self.inventory = []
        self.victory = False
        self._score = 0
        self._move = 0

    def move(self, dx, dy):
        '''
        Given integers dx and dy, move player to
        new location (self.x + dx, self.y + dy)
        param dx: integer
        param dy: integer
        '''
        self.x += dx
        self.y += dy

    def move_north(self):
        '''These integer directions are based on how the map must be stored
        in our nested list World.map'''
        self.move(0, -1)

    def move_south(self):
        self.move(0, 1)

    def move_east(self):
        self.move(1, 0)

    def move_west(self):
        self.move(-1, 0)

    def add_item(self, item):
        '''
        Add item to inventory.
        '''
        self.inventory.append(item)

    def remove_item(self, item):
        '''
        Remove item from inventory.
        '''
        self.inventory.remove(item)

    def get_inventory(self):
        '''
        Return inventory.
        '''
        return self.inventory

    def count_move(self):
        '''
        Count the movement
        '''
        self._move += 1

    def get_score(self):
        '''
        Return the score
        '''
        return self._score

    def get_move(self):
        '''
        Reture the movement
        '''
        return self._move

    def is_too_much_items(self):
        '''
        Determine whether items are too much
        '''
        return len(self.inventory) > 3

    def add_score(self, points):
        '''
        Add the score into player
        '''
        self._score += points
