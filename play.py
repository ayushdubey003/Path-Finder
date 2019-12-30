import sys
sys.path.append('gui/api')
sys.path.append('gui/res')

from maze import Maze
from utils import draw_maze
from window import Window
from colors import color_list


def play(dim=20):
    display_window_width = 1050
    display_window_height = 710
    maze_size = 580
    partition = 720
    cell_size = maze_size // dim
    maze_offset_x = (partition - cell_size * dim) // 2
    maze_offset_y = (display_window_height - cell_size * dim) // 2
    border_width = int(20 / dim + 1.7)
    
    display_window = Window(display_window_width, display_window_height, 
            caption='Maze')
    
    maze = Maze(dim)
    maze.build()

    draw_maze(display_window, maze, maze_offset_x,maze_offset_y, cell_size, border_width, precision=False if dim > 35 else True)

    solution_rect = display_window.draw_textbox((partition + display_window_width) / 2.1
        , display_window_height / 2 - 30, 'See solution', color=color_list['dark_gray']  
            , size=52, action=None, fontstyle='rasa', underline=True)

    save_rect = display_window.draw_textbox((partition + display_window_width) / 2.1
        , display_window_height / 2 + 30, 'Export Maze', color=color_list['dark_gray']
            , size=32, action=None, fontstyle='rasa', underline=True, italic=False)

    display_window.show()


def main():
    if len(sys.argv) == 1:
        play(30)
    else:
        DIM = int(sys.argv[1][1:])
        if DIM > 50 or DIM < 1:
            print("Please enter a dimension between 1 and 50")
        else:
            play(DIM)


if __name__ == '__main__':
    main()
