import tkinter as tk
from ui.CalcUI import CalcUI

if __name__ == "__main__":
    rt = tk.Tk()
    rt.geometry("300x400")
    CalcUI(rt)
    rt.mainloop()