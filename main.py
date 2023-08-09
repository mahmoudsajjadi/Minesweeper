from tkinter import *
from tkinter import ttk
import settings
import utils
from cell import Cell
from board import Board
import time
import emoji


from tkinter.font import Font

# custom_font = Font(family='Helvetica', size=your_font_size)

root = Tk()
root.iconbitmap("mine.ico")

# Window settings
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper")
root.resizable(False, False)

# Custom Font
title_font = Font(family='Helvetica', size=35, weight='bold')
button_font = Font(family='Helvetica', size=12)

# Title block
top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utils.height_percent(20)
)
top_frame.place(x=0, y=0)

# Bar above main game
control_frame = Frame(
    top_frame,
    bg='grey',
    width=utils.width_percentage(58.6),
    height=utils.height_percent(5),
    bd=1,
    borderwidth=2

)
control_frame.place(x=utils.width_percentage(20), y=utils.height_percent(15))

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
    width=utils.width_percentage(20),
    height=utils.height_percent(80),
    bd=5,  # Add border
    relief='sunken',  # Add sunken effect
)
center_frame.place(x=utils.width_percentage(20), y=utils.height_percent(20))


# Function to handle difficulty selection
def on_difficulty_selected(event):
    difficulty = selected_difficulty.get()
    board.remove_all_mines()
    board.randomize_mines(difficulty)


# Dropdown menu for difficulty selection

selected_difficulty = StringVar()
selected_difficulty.set("")

# Styling the dropdown
dropdown_font_style = ("Helvetica", 12)
style = ttk.Style()
style.theme_use('clam')
style.configure('TMenubutton',
                font=dropdown_font_style)


difficulty_options = ["Easy", "Easy", "Medium", "Hard", "Expert"]
difficulty_dropdown = ttk.OptionMenu(
    control_frame, selected_difficulty, *difficulty_options, command=on_difficulty_selected)
difficulty_dropdown.pack()
difficulty_dropdown.place(x=0,
                          y=0)


# timer visuals..
label = Label(control_frame,
              text=f'{emoji.emojize(":alarm_clock:")}', font=("Helvetica", 19), fg="red", bg="grey")
label.pack()
label.place(x=utils.width_percentage(22), y=0)

stopwatch_label = Label(control_frame, text="00", font=("Helvetica", 15))
stopwatch_label.pack()
stopwatch_label.place(x=utils.width_percentage(26), y=0)

elapsed_time = 0  # Initialize elapsed_time


def update_stopwatch():
    global start_time, elapsed_time

    if start_time > 0:  # Only update if the stopwatch has started
        # Calculate the elapsed time since the stopwatch started
        current_time = time.time()
        elapsed_time = current_time - start_time

    # Format the elapsed time as hours, minutes, and seconds
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)

    # Update the stopwatch label text
    stopwatch_label.config(
        text=f"{hours:02d}:{minutes:02d}:{seconds:02d}", bg="grey")

    # Schedule the update_stopwatch function to run again after 100 milliseconds
    stopwatch_label.after(100, update_stopwatch)


def start_stopwatch(event):
    global start_time

    # Start the stopwatch if it hasn't been started yet
    if start_time == 0:
        start_time = time.time()


start_time = 0


# Bind the start_stopwatch function to all buttons
root.bind_all("<Button-1>", start_stopwatch)

# Board
board = Board(settings.GRID_SIZE,
              settings.GRID_SIZE, center_frame)

# board.randomize_mines()
board.randomize_mines("Easy")  # Set the difficulty to easy


# Control Functions


def flag():
    board.flag_selected_cell()
    print("Flagged")


def uncover():
    board.uncover_selected_cell()
    print("Uncovered")


def start_new_game():
    global start_time, elapsed_time
    start_time = time.time()
    elapsed_time = 0  # Reset elapsed_time
    board.remove_all_mines()
    board.randomize_mines()  # Randomize mines again
    update_stopwatch()  # Start updating immediately after starting a new game


# Control Buttons
flagButton = Button(
    left_frame, text=f'{emoji.emojize(":triangular_flag:")}', command=flag)
flagButton.pack()
flagButton.place(x=40, y=30)

uncoverButton = Button(left_frame, text="Uncover Button", command=uncover)
uncoverButton.pack()
uncoverButton.place(x=40, y=60)

# Start New Game Button
newGameButton = Button(control_frame,
                       text=f'{emoji.emojize(":grinning_face:")}', font=("Helvetica", 13), fg="yellow", bg="#807E75", command=start_new_game)
newGameButton.pack()
newGameButton.place(x=utils.width_percentage(17), y=0)


if __name__ == "__main__":
    # Initialize the start_time variable
    start_time = 0
    elapsed_time = 0

    # Start the update_stopwatch function to update the stopwatch display
    update_stopwatch()

    # Run the tkinter main event loop
    # root.mainloop()

# Run Window
root.mainloop()
