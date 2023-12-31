import tkinter
import customtkinter as ctk

        
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry('500x500')
        self.title('TestApp')
        
        self.frame = Frame1(self)

class Frame1(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        #if you remove this, the "red block" will stick to the upper left corner
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        
        self.frame_rot = ctk.CTkFrame(master=master, fg_color='red')
        self.frame_rot.grid(row=0, column=0)

        #sticky "ns" will centralize the label vertically
        self.label = ctk.CTkLabel(master=self.frame_rot, text='hallo', height=130)
        self.label.grid(row=0, column=0, sticky="ns")
        

if __name__ == "__main__":
    app = App()
    app.mainloop()