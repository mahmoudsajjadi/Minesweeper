from tkinter import *
import settings
import utils
from cell import Cell
from board import Board
import time

root = Tk()

# Window settings
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper")
root.resizable(False, False)

# Custom Font
title_font = ("Helvetica", 24, "bold")
button_font = ("Helvetica", 14)

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

# Stopwatch
start_time = time.time()


def update_stopwatch():
    elapsed_time = time.time() - start_time
    stopwatch_label.config(text="Time: {:.1f} seconds".format(elapsed_time))
    stopwatch_label.after(100, update_stopwatch)

#Control Functions
def flag():
    board.flag_selected_cell()
    print("Flagged")
    

def uncover():
    board.uncover_selected_cell()
    print("Uncovered")


def start_new_game():
    global start_time
    start_time = time.time()
    board.reset_board()
    board.randomize_mines()  # Randomize mines again
    update_stopwatch()
    
    
#Control Buttons
flagButton = Button(left_frame, text="Flag Button", command=flag)
flagButton.pack()
flagButton.place(x=40, y=30)

uncoverButton = Button(left_frame, text="Uncover Button", command=uncover)
uncoverButton.pack()
uncoverButton.place(x=40, y=60)

# Stopwatch Label
stopwatch_label = Label(top_frame, text="Time: 0 seconds", font=title_font, fg="white", bg="black")
stopwatch_label.pack(pady=10)

# Start stopwatch
update_stopwatch()

# Start New Game Button
newGameButton = Button(top_frame, text="Start New Game", font=button_font, command=start_new_game)
newGameButton.pack(pady=10)


#Run Window
root.mainloop()

