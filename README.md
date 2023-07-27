# Minesweeper

## Documentation:

### main.py:
- Sets up the initial window for the game
- Initializes the board object and places mines
- Defines button control function
- Initializes two buttons: flag and uncover
- Runs the window

### board.py:
Properties:
- Rows: number of rows
- Cols: number of cols
- Cells: array of cell objects
- Selected cell: cell object that is marked as selected
- Center frame
- Total mines: number of mines to be placed on board


Within initialization:
- Populates the board with cells
- Sets the cell button’s command to return the x and y of the cell (lamba)

on_cell_click:
- If the clicked on cell is already selected: nothing happens
- If a cell was previously selected, it is deselected
- Once deselection is finished, the new cell is set as the selected cell

deselect_selected_cell:
- Sets the previously selected cell to not be selected

flag_selected_cell:
- If the cell is selected: sets flagged to true and put ‘F’ on button

uncover_selected_cell
- Sets uncovered to true
- If cell is mine: calls show_mine, else set cell text to the number of surrounding mines
- Updates the button's text with the number of surrounding mines
- If surrounding mine count is zero: uncovers the surrounding cells

get_surrounding_cells
- creates a list of the cells around the selected cell in 3x3 grid
- prints the list of coords to terminal

count_surrounding_mines
- uses the surrounding cells list to determine how many mines are around the cell

uncover_surrounding_cells
- uncovers the cells around the selected cell in 3x3 grid

randomize_mines
- Sets the total number of mines to 20% of the board
- While the mines placed is less that total number of mines: random x and y coordinates are chosen
- If those coordinates are not already a mine, is_mine is set to true and the mine count is updated

### cell.py:
Properties:
- Is_mine: set when cell is a mine
- cell_btn_object
- x and y: integer attributes representing the row and column indices of the cell on the game board.
- is_selected: a boolean attribute indicating whether the cell is currently selected by the player (default is False).
- is_flagged: a boolean attribute indicating whether the cell is flagged by the player as a possible mine (default is False).
- is_uncovered: a boolean attribute indicating whether the cell is uncovered (revealed) by the player (default is False).

create_btn_object:
- Creates and configures button widget
- Button is bound to right and left mouse clicks

update_btn_text:
- Updates the text on the button

set_selected:
- When the cell is selected, its background color is changed to "lightblue"; when deselected, it's restored to "lightgray".

set_flagged method:
- Sets the cell as flagged or unflagged based on the given flagged boolean parameter.

show_mine method:
- Changes the background color of the cell's graphical button to "red" to indicate that it contains a mine.


## UI Features:
- [ ] mine counter
- [ ] stopwatch
- [ ] flags
- [ ] mines
- [ ] game over message
- [ ] flag and uncover buttons
- [ ] start new game


## Functionality To Do:
- game over functions: all spaces are cleared OR mine is uncovered



