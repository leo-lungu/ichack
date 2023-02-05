import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image  

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.menu_page = MenuPage(self)
        self.master.configure(background='#57C4E5')
        self.menu_page.pack()
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family="Arial",
                                   size=19,
                                   weight=font.BOLD)
        
    def switch_to_main(self):
        self.menu_page.pack_forget()
        self.main_page = MainPage(self)
        self.main_page.pack()

    def switch_to_menu(self):
        self.main_page.pack_forget()
        self.main_page.remove_image()
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
        #self.startBtn["command"] = DOES THIS EXIST?!?!?!
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
        self.lf = Image.open("lefthand.png")
        self.left_hand = ImageTk.PhotoImage(self.lf)
        self.image_label = tk.Label(image=self.left_hand, bg="#57C4E5")
        self.image_label.image = self.left_hand
        self.image_label.pack(side="bottom")

    def create_widgets(self):
        self.tfont = tk.font.Font(size=24)

        self.back = tk.Button(self)
        self.back["text"] = "Go back."
        self.back["command"] = self.master.switch_to_menu
        self.back.pack()

        self.index_entry = tk.Text(self, width = 20, height = 3, font=self.tfont)
        self.index_entry.insert("end", "THIS IS MY INDEX")
        self.index_entry.pack()

        self.middle_entry = tk.Text(self, width = 20, height = 3, font=self.tfont)
        self.middle_entry.insert("end", "THIS IS MY MIDDLE")
        self.middle_entry.pack()

        self.ring_entry = tk.Text(self, width = 20, height = 3, font=self.tfont)
        self.ring_entry.insert("end", "THIS IS MY RING")
        self.ring_entry.pack()

        self.pinky_entry = tk.Text(self, width = 20, height = 3, font=self.tfont)
        self.pinky_entry.insert("end", "THIS IS MY PINKY")
        self.pinky_entry.pack()



    def remove_image(self):
        self.image_label.destroy()





if __name__ == "__main__":
    root = tk.Tk()
    WIDTH = 1280
    HEIGHT = 720
    root.geometry("1280x720")
    root.title("Hand Hero")
    root.resizable(False, False)
    app = Application(master=root)
    app.mainloop()
