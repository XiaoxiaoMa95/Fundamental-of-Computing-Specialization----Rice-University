"""
Clone of 2048 game.
"""
# http://www.codeskulptor.org/#user47_UgHQEH8mnoWDYwp_1.py

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    non_zero = []
    is_zero = []

    for item in line:
        if item == 0:
            is_zero.append(item)
        else:
            non_zero.append(item)

    new_line = list(non_zero + is_zero)

    for index in range(len(new_line) - 1):
        if new_line[index] == new_line[index + 1] and new_line[index] != 0:
            new_line[index] += new_line[index + 1]
            new_line[index + 1] = 0
            new_line.append(new_line[index + 1])
            new_line.pop(index + 1)

    return new_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        '''
        Take the height and width of the grid and creates the initial 2048 board
        '''
        self._height = grid_height
        self._width = grid_width
        self.reset()

        up_lst = [(0, col) for col in range(self._width)]
        down_lst = [(self._height - 1, col) for col in range(self._width)]
        left_lst = [(row, 0) for row in range(self._height)]
        right_lst = [(row, self._width - 1) for row in range(self._height)]
        self._move_dict = {UP: up_lst, DOWN: down_lst, LEFT: left_lst, RIGHT: right_lst}      

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in range(self._width)]
                     for dummy_row in range(self._height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return str(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        offset = list(OFFSETS[direction])
        initial_tile = self._move_dict[direction]

        if direction == 1 or direction == 2:
            counts = self._height
        elif direction == 3 or direction == 4:
            counts = self._width

        for dummy_tile in initial_tile:
            # merges and refresh a single row or column in 2048
            temp_lst = []
            tile = list(dummy_tile)
            temp_lst.append(self.get_tile(tile[0], tile[1]))
            for dummy_i in range(counts - 1):
                tile[0] += offset[0]
                tile[1] += offset[1]
                temp_lst.append(self.get_tile(tile[0], tile[1]))
            result = merge(temp_lst)

            tile = list(dummy_tile)
            self.set_tile(tile[0], tile[1], result[0])
            for dummy_j in range(1, counts):
                tile[0] += offset[0]
                tile[1] += offset[1]
                self.set_tile(tile[0], tile[1], result[dummy_j])

        self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        zero_tiles = []
        random_zero_tile = ()
        choices = [2] * 9 + [4]
        for row in range(self._height):
            for col in range(self._width):
                #print row,col,self.get_grid_height(),self.get_grid_width()
                #print self._grid
                if self._grid[row][col] == 0:
                    zero_tiles.append((row,col))
                    
        if len(zero_tiles):
            random_zero_tile = random.choice(zero_tiles)            
            value = random.choice(choices)
            self.set_tile(random_zero_tile[0], random_zero_tile[1],value)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 5))


