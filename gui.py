import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image  
import json

with open("data.json") as f:
    data = json.load(f)

page_1 = data["pages"][0]
page_2 = data["pages"][1]
indexVal1 = (f"{page_1['key_1']}")
middleVal1 = (f"{page_1['key_2']}")
ringVal1 = (f"{page_1['key_3']}")
pinkyVal1 = (f"{page_1['key_4']}")

indexVal2 = (f"{page_2['key_1']}")
middleVal2 = (f"{page_2['key_2']}")
ringVal2 = (f"{page_2['key_3']}")
pinkyVal2 = (f"{page_2['key_4']}")

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
        self.tfont = tk.font.Font(size=14)

        self.back = tk.Button(self)
        self.back["text"] = "Go back."
        self.back["command"] = self.master.switch_to_menu
        self.back.grid(row=0, column=2)

        self.save = tk.Button(self)
        self.save["text"] = "Save."
        # self.save["command"] = write to file
        self.save.grid(row=2, column=2)

        self.page1_label = tk.Label(self)
        self.page1_label["text"] = "Page one"
        self.page1_label.grid(row=0, column=1)

        self.page2_label = tk.Label(self)
        self.page2_label["text"] = "Page two"
        self.page2_label.grid(row=0, column=3)


        self.one_label = tk.Label(self)
        self.one_label["text"] = "1"
        self.one_label.grid(row=1, column=0)

        self.two_label = tk.Label(self)
        self.two_label["text"] = "2"
        self.two_label.grid(row=2, column=0)

        self.three_label = tk.Label(self)
        self.three_label["text"] = "3"
        self.three_label.grid(row=3, column=0)

        self.fourth_label = tk.Label(self)
        self.fourth_label["text"] = "4"
        self.fourth_label.grid(row=4, column=0)


        self.index_entry = tk.Text(self, width = 20, height = 3, font=self.tfont)
        self.index_entry.insert("end", indexVal1)
        self.index_entry.grid(row=1, column=1, padx=20, pady=5)

        self.middle_entry = tk.Text(self, width = 20, height = 3, font=self.tfont)
        self.middle_entry.insert("end", middleVal1)
        self.middle_entry.grid(row=2, column=1, padx=20, pady=5)

        self.ring_entry = tk.Text(self, width = 20, height = 3, font=self.tfont)
        self.ring_entry.insert("end", ringVal1)
        self.ring_entry.grid(row=3, column=1, padx=20, pady=5)

        self.pinky_entry = tk.Text(self, width = 20, height = 3, font=self.tfont)
        self.pinky_entry.insert("end", pinkyVal1)
        self.pinky_entry.grid(row=4, column=1, padx=20, pady=5)
        
        self.index_entry2 = tk.Text(self, width = 20, height = 3, font=self.tfont)
        self.index_entry2.insert("end", indexVal2)
        self.index_entry2.grid(row=1, column=3, padx=20, pady=5)

        self.middle_entry2 = tk.Text(self, width = 20, height = 3, font=self.tfont)
        self.middle_entry2.insert("end", middleVal2)
        self.middle_entry2.grid(row=2, column=3, padx=20, pady=5)

        self.ring_entry2 = tk.Text(self, width = 20, height = 3, font=self.tfont)
        self.ring_entry2.insert("end", ringVal2)
        self.ring_entry2.grid(row=3, column=3, padx=20, pady=5)

        self.pinky_entry2 = tk.Text(self, width = 20, height = 3, font=self.tfont)
        self.pinky_entry2.insert("end", pinkyVal2)
        self.pinky_entry2.grid(row=4, column=3, padx=20, pady=5)



    def remove_image(self):
        self.image_label.destroy()





if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x720")
    root.title("Hand Hero")
    root.resizable(False, False)
    app = Application(master=root)
    app.mainloop()
