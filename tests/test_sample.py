from unittest import TestCase
from context import src
from src import my_module

class MyTest(TestCase):
    # todo: setup initial test variables / objects

    def test_current_location(self):
        rover = my_module.Rover()
        rover.land_rover('1 2 N', '5 5')
        self.assertEqual(rover.current_location(), (1, 2, 'N'))

    def test_move(self):
        rover = my_module.Rover()
        rover.land_rover('1 2 N', '5 5')

        rover.move()
        self.assertEqual(rover.current_location(), (1, 3, 'N'))

        rover.move()
        rover.move()
        self.assertEqual(rover.current_location(), (1, 5, 'N'))

        rover.move()
        self.assertEqual(rover.current_location(), (1, 5, 'N'))

    def test_left(self):
        rover = my_module.Rover()
        rover.land_rover('1 2 N', '5 5')

        rover.left()
        self.assertEqual(rover.current_location(), (1, 2, 'W'))

        rover.left()
        self.assertEqual(rover.current_location(), (1, 2, 'S'))

        rover.left()
        self.assertEqual(rover.current_location(), (1, 2, 'E'))

        rover.left()
        self.assertEqual(rover.current_location(), (1, 2, 'N'))

    def test_right(self):
        rover = my_module.Rover()
        rover.land_rover('1 2 N', '5 5')

        rover.right()
        self.assertEqual(rover.current_location(), (1, 2, 'E'))

        rover.right()
        self.assertEqual(rover.current_location(), (1, 2, 'S'))

        rover.right()
        self.assertEqual(rover.current_location(), (1, 2, 'W'))

        rover.right()
        self.assertEqual(rover.current_location(), (1, 2, 'N'))

    def test_conduct_mission(self):
        rover = my_module.Rover()
        rover.land_rover('1 2 N', '5 5')

        rover.conduct_mission('LMLMLMLMM')
        self.assertEqual(rover.current_location(), (1, 3, 'N'))

        rover = my_module.Rover()
        rover.land_rover('3 3 E', '5 5')

        rover.conduct_mission('MMRMMRMRRM')
        self.assertEqual(rover.current_location(), (5, 1, 'E'))


