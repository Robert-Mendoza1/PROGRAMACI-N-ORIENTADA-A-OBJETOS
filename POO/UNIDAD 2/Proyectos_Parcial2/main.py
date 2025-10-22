from tkinter import Tk
from login_view import LoginApp

def main():
    root = Tk()
    app = LoginApp(root)
    root.mainloop()
    
    
if __name__ == "__main__":
    main()