from tkinter import *
import settings
import utils
from cell import Cell
from board import Board
import time

from tkinter.font import Font

# custom_font = Font(family='Helvetica', size=your_font_size)

root = Tk()

# Window settings
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper")
root.resizable(False, False)

# Custom Font
title_font = Font(family='Arial', size=24, weight='bold')
button_font = Font( family = "Arial", 
                                 size = 20, 
                                 weight = "bold")

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
    bg='#d9d9d9',  # Light gray color
    width=utils.width_percentage(80),
    height=utils.height_percent(80),
    bd=5,  # Add border
    relief='sunken'  # Add sunken effect
)
center_frame.place(x=utils.width_percentage(20), y=utils.height_percent(20))


# Function to handle difficulty selection
def on_difficulty_selected(event):
    difficulty = selected_difficulty.get()
    board.remove_all_mines()
    board.randomize_mines(difficulty)
    
    
# Dropdown menu for difficulty selection

selected_difficulty = StringVar(root, value="easy")

difficulty_options = ["easy", "medium", "hard", "very_hard"]
difficulty_dropdown = OptionMenu(left_frame, selected_difficulty, *difficulty_options, command=on_difficulty_selected)
difficulty_dropdown.pack()
difficulty_dropdown.place(x=40, y=200)


#Board
board = Board(settings.GRID_SIZE, settings.GRID_SIZE, center_frame)
# board.randomize_mines()
board.randomize_mines("easy")  # Set the difficulty to easy

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
    # board.reset_board()
    board.remove_all_mines()
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

# Mines Label
mine_count_label = Label(top_frame, text="Mines: {}".format(board.total_mines), font=title_font, fg="white", bg="black")
mine_count_label.pack(pady=10)

# Start stopwatch
update_stopwatch()

# Start New Game Button
newGameButton = Button(top_frame, text="Start New Game", font=button_font, command=start_new_game)
newGameButton.pack(pady=10)


#Run Window
root.mainloop()

