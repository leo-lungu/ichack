import tkinter as tk
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.count = 0

    def create_widgets(self):
        self.welcome = tk.Label(self)
        self.welcome["text"] = "Welcome to Hand Hero\nCommunication made easy."
        self.welcome.pack(side="top")

        self.startBtn = tk.Button(self)
        self.startBtn["text"] = "Start"
        #self.startBtn["command"] = 
        self.startBtn.pack(side="top")


        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")


root = tk.Tk()
root.geometry("600x400+100+100")
app = Application(master=root)
app.mainloop()
