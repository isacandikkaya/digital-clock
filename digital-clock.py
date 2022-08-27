from tkinter import Label, Tk 
import time
pencere = Tk() 
pencere.title("Digital Clock") 
pencere.geometry("420x150") 
pencere.resizable(1,1)

text_font= ("Boulder", 68, 'bold')
background = "#cffbbbbbb"
foreground= "#cffffcc00"
border_width = 25

label = Label(pencere, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

def saat(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, saat)

saat()
pencere.mainloop()
