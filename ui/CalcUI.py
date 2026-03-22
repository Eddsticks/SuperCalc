import tkinter as tk
from tkinter import ttk
from styles.themes import apply_styles
from logic.CalcLogic import CalcLogic

class CalcUI:
    def __init__(self, window):
        self.window = window
        self.window.title("SuperCalculator by Eddy")
        self.logic = CalcLogic()
        apply_styles(self.window)

        # == PANEL ==
        self.pant = ttk.Entry(window, font=('Arial', 20), justify='right')
        self.pant.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)

        # == BUTTONS ==
        buttons = [
            ('E', 0, 3, "Delete.TButton"),
            ('7', 1, 0, None), ('8', 1, 1, None), ('9', 1, 2, None), ('/', 1, 3, "Operation.TButton"),
            ('4', 2, 0, None), ('5', 2, 1, None), ('6', 2, 2, None), ('*', 2, 3, "Operation.TButton"),
            ('1', 3, 0, None), ('2', 3, 1, None), ('3', 3, 2, None), ('-', 3, 3, "Operation.TButton"),
            ('C', 4, 0, "Delete.TButton"), ('0', 4, 1, None), ('=', 4, 2, "Operation.TButton"),
            ('+', 4, 3, "Operation.TButton")
        ]

        for (text, panel, col, sty) in buttons:
            com = lambda t=text: self.on_press(t)
            ttk.Button(window, text=text, command=com, style=sty if sty else "TButton").grid(row=panel, column=col,
                                                                                             sticky="nsew", ipady=10)

        for i in range(4):
            window.grid_columnconfigure(i, weight=1)
        for i in range(5):
            window.grid_rowconfigure(i, weight=1)

    def on_press(self, key):
        if key == "=":
            res = self.logic.calculate(self.pant.get())
            self.pant.delete(0, tk.END)
            self.pant.insert(tk.END, res)
        elif key == "C":
            self.pant.delete(0, tk.END)
        elif key == "E":
            ntext = self.logic.backspace(self.pant.get())
            self.pant.delete(0, tk.END)
            self.pant.insert(tk.END, ntext)
        else:
            self.pant.insert(tk.END, key)
