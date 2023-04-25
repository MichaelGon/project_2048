import unittest
from init import Globals
from func import make_turn, is_any


class Test_2048(unittest.TestCase):
    def test_1(self):
        arr = [
            [2, 2, 4, 0],
            [2, 0, 4, 2],
            [2, 4, 0, 8],
            [0, 0, 0, 0]
        ]

        rez = [
            [4, 4, 0, 0],
            [2, 4, 2, 0],
            [2, 4, 8, 0],
            [0, 0, 0, 0]
        ]

        example = Globals()
        example.board_values = arr
        example.direction = 'LEFT'

        self.assertEqual(make_turn(example), rez)

    def test_2(self):
        arr = [
            [2, 2, 4, 0],
            [4, 2, 8, 0],
            [2, 0, 0, 8],
            [2, 2, 8, 0]
        ]

        rez = [
            [0, 0, 4, 4],
            [0, 4, 2, 8],
            [0, 0, 2, 8],
            [0, 0, 4, 8]
        ]

        example = Globals()
        example.board_values = arr
        example.direction = 'RIGHT'

        self.assertEqual(make_turn(example), rez)

    def test_3(self):
        arr = [
            [2, 2, 0, 0],
            [4, 2, 8, 0],
            [2, 4, 4, 8],
            [0, 0, 2, 0]
        ]

        rez = [
            [2, 4, 8, 8],
            [4, 4, 4, 0],
            [2, 0, 2, 0],
            [0, 0, 0, 0]
        ]

        example = Globals()
        example.board_values = arr
        example.direction = 'UP'

        self.assertEqual(make_turn(example), rez)

    def test_4(self):
        arr = [
            [2, 2, 0, 0],
            [4, 2, 0, 0],
            [2, 4, 0, 8],
            [0, 0, 0, 0]
        ]

        rez = [
            [0, 0, 0, 0],
            [2, 0, 0, 0],
            [4, 4, 0, 0],
            [2, 4, 0, 8]
        ]

        example = Globals()
        example.board_values = arr
        example.direction = 'DOWN'

        self.assertEqual(make_turn(example), rez)

    def test_5(self):
        arr = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        rez = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        example = Globals()
        example.board_values = arr
        example.direction = 'UP'
        self.assertEqual(make_turn(example), rez)

        example.direction = 'DOWN'
        self.assertEqual(make_turn(example), rez)

        example.direction = 'RIGHT'
        self.assertEqual(make_turn(example), rez)

        example.direction = 'LEFT'
        self.assertEqual(make_turn(example), rez)

    def test_6(self):
        arr = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        example = Globals()
        example.board_values = arr

        self.assertEqual(is_any(example), True)

    def test_7(self):
        arr = [
            [2, 4, 8, 2],
            [16, 8, 4, 2],
            [2, 4, 8, 16],
            [8, 16, 2, 4]
        ]

        example = Globals()
        example.board_values = arr

        self.assertEqual(is_any(example), True)

    def test_8(self):
        arr = [
            [2, 4, 8, 16],
            [16, 8, 4, 2],
            [2, 4, 8, 16],
            [16, 78, 4, 2]
        ]

        example = Globals()
        example.board_values = arr

        self.assertEqual(is_any(example), False)


if __name__ == 'main':
    unittest.main()
