from tkinter import Button


class Cell:
    def __init__(self, is_mine=False) -> None:
        self.is_mine = is_mine
        self.cell_btn_object = None

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=5,
            height=2,
            text=' '
        )
        btn.bind()
        self.cell_btn_object = btn
