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
        self.is_game_over = False

        #populate the board with cells
        for x in range(rows):
            for y in range(cols):
                c = self.cells[x][y]
                c.create_btn_object(center_frame)
                c.cell_btn_object.config(command=lambda row=x, col=y: self.on_cell_click(row, col))
                c.cell_btn_object.grid(column=x, row=y)
    
    def remove_all_mines(self):
        for row in self.cells:
            for cell in row:
                cell.is_mine = False
                cell.update_btn_text(" ")
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
            self.selected_cell = None

    def flag_selected_cell(self):
        if self.selected_cell:
            self.selected_cell.set_flagged()
            self.selected_cell.update_btn_text("F")
        self.is_game_over = self.check_for_win()
    
    def uncover_selected_cell(self):
        if self.selected_cell:
            self.selected_cell.is_uncovered = True

            # Update the button text based on the cell contents (e.g., bomb count)
            if self.selected_cell.is_mine:
                self.selected_cell.show_mine()
                self.is_game_over = True
                self.game_over()
                
            else:
                #get num of surrounding mines
                surrounding_mine_count = self.count_surrounding_mines(self.selected_cell)
                #update the button text to match the num of mines
                self.selected_cell.update_btn_text(surrounding_mine_count)

                #if there are no surrounding mines, uncover the surrounding cells and display their mine count
                if surrounding_mine_count == 0:
                    self.uncover_surrounding_cells(self.selected_cell)      
                
                self.is_game_over = self.check_for_win()

    def get_surrounding_cells(self, cell):
        x, y = cell.x, cell.y
        surrounding_cells = []
        #append the surrounding cells (3x3 grid) to the list
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i >= 0 and i < self.rows and j >= 0 and j < self.cols:
                    if i != x or j != y:
                        surrounding_cells.append(self.cells[i][j])

        print(f"Surrounding cells for ({x}, {y}):")
        print([(cell.x, cell.y) for cell in surrounding_cells])

        return surrounding_cells
    
    def count_surrounding_mines(self, cell):
        #counts the number of mines surrounding the cell
        surrounding_cells = self.get_surrounding_cells(cell)
        count = 0
        for cell in surrounding_cells:
            if cell.is_mine:
                count += 1
        print(f"Found {count} mines")
        return count
    
    def uncover_surrounding_cells(self, cell):
        #uncover the surrounding cells
        surrounding_cells = self.get_surrounding_cells(cell)
        for cell in surrounding_cells:
            cell.is_uncovered = True
            surrounding_mine_count = self.count_surrounding_mines(cell)
            cell.update_btn_text(surrounding_mine_count)
        
    
    #Randomly places mines on the board
    def randomize_mines(self, difficulty):
        if difficulty == "easy":
            self.total_mines = int(self.rows * self.cols * 0.1)  # 10% of the board is mines
        elif difficulty == "medium":
            self.total_mines = int(self.rows * self.cols * 0.30)  # 15% of the board is mines
        elif difficulty == "hard":
            self.total_mines = int(self.rows * self.cols * 0.50)  # 20% of the board is mines
        elif difficulty == "very_hard":
            self.total_mines = int(self.rows * self.cols * 0.75)  # 25% of the board is mines
        else:
            raise ValueError("Invalid difficulty level")

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

    def check_for_win(self):
        for row in self.cells:
            for cell in row:
                if cell.is_mine and not cell.is_flagged:
                    print("mines not all flagged")
                    return False
                if not cell.is_mine and not cell.is_uncovered:
                    print("not all cells uncovered")
                    return False
        print("You win!")
        return True   
    
    def game_over(self):
        print("Game over!")