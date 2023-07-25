from tkinter import Button

class Cell:
    def __init__(self, x, y, is_mine=False) -> None:
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y
        self.is_selected = False
        self.is_flagged = False
        self.is_uncovered = False


    def create_btn_object(self, parent):
        btn = Button(
            parent,
            width=5,
            height=2,
            text=f' '
        )
        btn.bind('<Button-1>', self.locate)
        btn.bind('<Button-3>', self.locate)
    
        self.cell_btn_object = btn
    
    #Updates the cell's text
    def update_btn_text(self, text):
        if self.cell_btn_object:
            self.cell_btn_object.config(text=text)
    
    #Return the x and y of the cell
    def locate(self, event):
        print("Selected cells coords: ({x}, {y})".format(x=self.x, y=self.y))

    #Set the cell as selected
    def set_selected(self, selected=True):
        self.is_selected = selected
        if selected:
            self.cell_btn_object.config(bg="lightblue")
        else:
            self.cell_btn_object.config(bg="lightgray")  # Restore default background color

    #Set the cell as flagged  
    def set_flagged(self, flagged=True):
        self.is_flagged = flagged
    
    #logic for when the cell uncovers a mine
    def show_mine(self):
        self.cell_btn_object.config(bg="red")

        # Update the button text based on the cell contents (e.g., bomb count)


