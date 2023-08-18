from Star import * 
from tkinter import *
import tkinter as tk
    
count = True
class Starfield(tk.Tk):
    def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)
            self.stars = self.first_take()
            self.speed = 1
            self.geometry('800x600')
            self.canvas = Canvas(self, width=800, height=600, bg='black', highlightthickness=0)
            self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
            self.canvas.pack()
            self.wm_attributes('-transparentcolor','purple')
            self.label = Label(self.canvas, text='Speed : '+ str(self.speed), font=("Arial", 25), bg='black', fg ='white')
            self.label.pack()
            self.canvas.create_window(0, 0, window=self.label, anchor='nw')
            self.update_canvas()
            
    def _on_mousewheel(self, event):
        if event.delta == -120:
            self.speed -= 1
        if event.delta == 120:
            self.speed += 1
        self.label.configure(text = 'Speed : ' + str(self.speed))
            
    def first_take(self):
        stars = []
        for i in range(500):
            stars.append(Star())
        return stars
        
    def make_stars(self):
        for i in range(500):
            self.stars.pop()
            self.stars.append(Star())
            self.stars[i].update(self.canvas, self.speed)
            

    def update_canvas(self):
        self.canvas.delete('delete')
        while count:
            self.make_stars()
            break
        self.after(2,self.update_canvas)
        
if __name__== "__main__":
    app = Starfield()
    app.mainloop()
