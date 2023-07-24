from tkinter import *
import settings
import utils
from cell import Cell
from board import Board

root = Tk()

# Window settings
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper")
root.resizable(False, False)

# Title block
top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utils.height_percent(20)
)
top_frame.place(x=0, y=0)

# Side block
left_frame = Frame(
    root,
    bg='black',
    width=utils.width_percentage(20),
    height=utils.height_percent(80)
)
left_frame.place(x=0, y=utils.height_percent(20))

# Main game place
center_frame = Frame(
    root,
    bg='black',
    width=utils.width_percentage(80),
    height=utils.height_percent(80)

)
center_frame.place(x=utils.width_percentage(20), y=utils.height_percent(20))


#Board
board = Board(settings.GRID_SIZE, settings.GRID_SIZE, center_frame)
board.randomize_mines()


#Control Functions
def flag():
    board.flag_selected_cell()
    print("Flagged")
    

def uncover():
    board.uncover_selected_cell()
    print("Uncovered")


#Control Buttons
flagButton = Button(left_frame, text="Flag Button", command=flag)
flagButton.pack()
flagButton.place(x=40, y=30)

uncoverButton = Button(left_frame, text="Uncover Button", command=uncover)
uncoverButton.pack()
uncoverButton.place(x=40, y=60)



#Run Window
root.mainloop()


