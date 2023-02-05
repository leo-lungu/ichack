import tkinter as tk
from tkinter import font

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.menu_page = MenuPage(self)
        self.main_page = MainPage(self)
        self.master.configure(background='#57C4E5')
        self.menu_page.pack()
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family="Arial",
                                   size=19,
                                   weight=font.BOLD)
        
    def switch_to_main(self):
        self.menu_page.pack_forget()
        self.main_page.pack()

    def switch_to_menu(self):
        self.main_page.pack_forget()
        self.menu_page.pack()

class MenuPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(background='#57C4E5')
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        self.welcome = tk.Label(self, bg="#57C4E5")
        self.welcome["text"] = "Welcome to Hand Hero!\nCommunication made easy."
        self.welcome.grid(row=0, column=0, columnspan=2, pady=50)

        self.selectBtn = tk.Button(self, bg='#011627', fg='#FFFFFF')
        self.selectBtn["text"] = "Select"
        #self.startBtn["command"] = 
        self.selectBtn.grid(row=1, column=0)

        self.startBtn = tk.Button(self, bg='#011627', fg='#FFFFFF')
        self.startBtn["text"] = "Start"
        self.startBtn["command"] = self.master.switch_to_main
        self.startBtn.grid(row=1, column=1)


        self.quit = tk.Button(self, text="QUIT", fg="red", bg='#011627', 
                              command=root.destroy)
        self.quit.grid(row=2, column=0, columnspan=2, pady=50)


class MainPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.back = tk.Button(self)
        self.back["text"] = "Go back."
        self.back["command"] = self.master.switch_to_menu
        self.back.grid(row=0, column=0)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x720")
    root.title("Hand Hero")
    app = Application(master=root)
    app.mainloop()
