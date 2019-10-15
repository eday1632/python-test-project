

class Rover(object):

    def __init__(self):
        self.x = None
        self.y = None
        self.bearing = None
        self.width_limit = None
        self.height_limit = None

    def land_rover(self, init, limits):
        # sets the initial position and bearing
        init = init.split()
        limits = limits.split()

        self.x = int(init[0])
        self.y = int(init[1])
        self.bearing = init[2]
        self.width_limit = int(limits[0])
        self.height_limit = int(limits[1])

    def move(self):
        # todo finish testing paths
        if self.bearing == 'N':
            if self.y < self.height_limit:
                self.y += 1
        elif self.bearing == 'E':
            if self.x < self.width_limit:
                self.x += 1
        elif self.bearing == 'S':
            if self.y > 0:
                self.y -= 1
        elif self.bearing == 'W':
            if self.x > 0:
                self.x -= 1

    def left(self):
        if self.bearing == 'N':
            self.bearing = 'W'
        elif self.bearing == 'E':
            self.bearing = 'N'
        elif self.bearing == 'S':
            self.bearing = 'E'
        elif self.bearing == 'W':
            self.bearing = 'S'

    def right(self):
        if self.bearing == 'N':
            self.bearing = 'E'
        elif self.bearing == 'E':
            self.bearing = 'S'
        elif self.bearing == 'S':
            self.bearing = 'W'
        elif self.bearing == 'W':
            self.bearing = 'N'

    def current_location(self):
        return self.x, self.y, self.bearing

    def conduct_mission(self, moves):
        for move in moves:
            if move == 'L':
                self.left()
            elif move == 'R':
                self.right()
            elif move == 'M':
                self.move()



