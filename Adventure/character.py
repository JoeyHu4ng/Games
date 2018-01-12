class Character:

    def __init__(self, x, y, name, hp, MAX_hp, MIN_damage, MAX_damage, speed, description = ""):
        '''
        The function will initialize the character.
        :param x: a int means curr x position
        :param y: a int means curr y position
        :param name: a str means character's name
        :param hp: a int means curr hp
        :param MAX_hp: a int means the max hp
        :param MIN_damage: a int means the highest damage
        :param MAX_damage: a int means the lowest damage
        :param speed: a int means the speed
        :param description: a str means curr character's description
        '''
        self.x = x
        self.y = y
        self.name = name
        self.description = description
        self.hp = hp
        self.MAX_hp = MAX_hp
        self.MIN_damage
        self.MAX_damage
        self.speed = speed

    def talk(self):
        '''
        The funtion will return curr character's description.
        :return:
        '''
        return self.description


class Player(Character):

    def __init__(self, x, y, name, hp, MAX_hp, MIN_damage, MAX_damage, speed, description = ""):
        Character.__init__(self, x, y, name, hp, MAX_hp, MIN_damage, MAX_damage, speed, description = "")
        self.backpack = []
        self.buff = []
        self.MAX_training_time = 10
        self.training_time = 0
        self.weapon = None
        self.MAX_item = 10

    def go_north(self):
        self.x -= 1

    def go_south(self):
        self.x += 1

    def go_east(self):
        self.y += 1

    def go_west(self):
        self.y -= 1

    def add_to_backpack(self, item):
        if len(self.backpack) <= self.MAX_item:
            self.backpack.append(item)
            return True
        else:
            return False

    def remove_from_backpack(self, item):
        display = self.get_backpack()
        if item in display:
            index = display.index(item)
            del self.backpack[index]
            return True
        else:
            return False

    def get_backpack(self):
        display = []
        for item in self.backpack:
            display.append(item.get_name)
        return display

    def use_item(self, item):
        display = self.get_backpack()
        if item in display:
            index = display.index(item)
            self.buff.append(self.backpack.pop(index))
            self.buff[-1].use()
            return True
        else:
            return False

    def equip(self, weapon):
        display = self.get_backpack()
        if weapon in display:
            if weapon is not None:
                self.backpack.append(weapon)
            index = display.index(weapon)
            self.weapon = self.backpack.pop(index)
            return True
        else:
            return False



class NonFighter(Character):
    pass


class Fighter(Character):
    pass
