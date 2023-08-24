# this is the main entry point of application. It should contain the code to launch the GUI.

import tkinter as tk
from GUI import recommend_GUI
from data import file_preparation


if __name__ == "__main__":
    
    root = tk.Tk()
    app = recommend_GUI()
    root.mainloop()
