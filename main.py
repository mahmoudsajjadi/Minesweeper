from tkinter import *
import settings
import utils
from cell import Cell

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

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell()
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )
root.mainloop()
