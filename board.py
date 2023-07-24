from cell import Cell
import random

class Board:

    def __init__(self, rows, cols, center_frame):
        self.rows = rows
        self.cols = cols
        self.cells = [[Cell(row, col) for col in range(cols)] for row in range(rows)]
        self.selected_cell = None
        self.center_frame = center_frame
        self.total_mines = 0

        #populate the board with cells
        for x in range(rows):
            for y in range(cols):
                c = self.cells[x][y]
                c.create_btn_object(center_frame)
                c.cell_btn_object.config(command=lambda row=x, col=y: self.on_cell_click(row, col))
                c.cell_btn_object.grid(column=x, row=y)
    
    def on_cell_click(self, row, col):
        cell = self.cells[row][col]

        if cell.is_selected:
            return  # Do nothing if the cell is already selected

        #deselect the previous cell
        self.deselect_selected_cell()

        #select the new cell
        cell.set_selected(True)
        self.selected_cell = cell

    def deselect_selected_cell(self):
        if self.selected_cell:
            self.selected_cell.set_selected(False)
            self.selected_cell.update_btn_text(" ")

            #keeps the flag on the cell
            if self.selected_cell.is_flagged:
                self.selected_cell.update_btn_text("F")

            #keeps the uncovered on the cell
            if self.selected_cell.is_uncovered and not self.selected_cell.is_mine:
                self.selected_cell.update_btn_text("U")


    def flag_selected_cell(self):
        if self.selected_cell:
            self.selected_cell.set_flagged()
            self.selected_cell.update_btn_text("F")

    def uncover_selected_cell(self):
        if self.selected_cell:
            self.selected_cell.is_uncovered = True
            # Update the button text based on the cell contents (e.g., bomb count)
            if self.selected_cell.is_mine:
                self.selected_cell.show_mine()
            else:
                self.selected_cell.update_btn_text("U")
    
    #Randomly places mines on the board
    def randomize_mines(self):
        self.total_mines = int(self.rows * self.cols * 0.2) # 20% of the board is mines
        mines_placed = 0

        while mines_placed < self.total_mines:
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.cols - 1)
            cell = self.cells[x][y]

            # Only place a mine if the cell doesn't already have one
            if not cell.is_mine:
                cell.is_mine = True
                cell.update_btn_text("M")
                mines_placed += 1
    
        print(f"Placed {mines_placed} mines")
