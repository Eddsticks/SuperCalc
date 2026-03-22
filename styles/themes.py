from tkinter import ttk
from . import  colors


def apply_styles(rt):
    style = ttk.Style()

    style.theme_use('alt')
    style.configure("TButton",
                    font=("Arial", 11, "bold"),
                    background=colors.BEIGE,
                    foreground="black")

    style.map("TButton",
              background=[('active', colors.BEIGE), ('pressed', colors.MUTED_OLIVE)])

    style.configure("Operation.TButton",
                    background=colors.CHARCOAL,
                    foreground="white")
    style.map("Operation.TButton",
              background=[('active', colors.GREY), ('pressed', colors.MUTED_OLIVE)])

    style.configure("Delete.TButton",
                    background=colors.TEA_GREEN,
                    foreground="black")
    style.map("Delete.TButton",
              background=[('active', colors.BEIGE), ('pressed', colors.MUTED_OLIVE)])