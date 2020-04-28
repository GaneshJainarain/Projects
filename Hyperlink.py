#Ganesh Jainarainsa
#December 20, 2019
#Defang Class NYPD UI



from tkinter import *
from tkinter import Tk
import tkinter as tk


def main():
    program = ConvertProgram()


class ConvertProgram:
    
    def __init__(self):
        self.window = Tk()
        self.my_display = None
        self.my_displayString = ''
        self.create_widgets()
        

    def create_widgets(self):

        self.my_display=Label(self.window, text=self.my_displayString, padx =140, pady =50)
        self.my_display.grid(row=0,column=0, columnspan = 4 ,rowspan = 4)
        

        label1 = Label(self.window, text = "Enter Defanged URL(s) Here:", font = "-weight bold")
        label1.grid(row = 0, column = 0)
        label1.config(font =("Calibra", 20))
        

        self.buttonClear = Button(self.window, text="Clear",font = "-weight bold", command = self.clear,padx =20)
        self.buttonClear.grid(row=3,column=1, columnspan = 1)
        self.buttonClear.config(font =("Calibra", 20))
        

        label2 = Label(self.window, text = "Hyperlink(s) ------> ", font = "-weight bold")
        label2.grid(row = 1, column = 0)
        label2.config(font =("Calibra", 20))
        

        self.entry = Entry(self.window, width = "40")
        self.entry.grid(row = 0, column = 1)
        

        convert_button = Button(self.window, text = "Convert To HYPERLINK",font = "-weight bold", command = self.Hyperlink)
        convert_button.grid(row=3, column=0)
        convert_button.config(font =("Calibra", 20))


        label5 = Label(self.window, text = "*This program auto-copies for you", font = "-weight bold")
        label5.grid(row = 4, column = 0)
        label5.config(font =("Calibra", 12))
        

        label6 = Label(self.window, text = "after Convert button is pressed*", font = "-weight bold")
        label6.grid(row = 5, column = 0)
        label6.config(font =("Calibra", 11))
        

        self.display_Hyperlink = Label(self.window)
        self.display_Hyperlink.grid(row = 1, column = 1)


        label34 = Label(self.window, text = "            ", font = "Helvetica")
        label34.grid(row = 5, column = 0, columnspan = 3)
        label34.config(font =("Calibra", 12))


        label4 = Label(self.window, text = " # Powered by Ganesh Jainarain of InfoSec #", padx= 20, pady =20 ,font = "Helvetica")
        label4.grid(row = 7, column = 0, columnspan = 3)
        label4.config(font =("Calibra", 12))


        quit_button = Button(self.window,text="Quit", font ="-weight bold", command=self.window.destroy,padx =30)
        quit_button.grid(row=4,column= 1,columnspan = 2)
        quit_button.config(font =("Calibra", 20))



    def Hyperlink(self):

        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        
        URL = str(self.entry.get())
        X = URL.replace("hxxp", "http").replace("[dot]", ".").replace("{", "").replace("}", "").replace("hxxps", "https").replace("[.]", ".").replace("HXXPS", "https").replace("HXXP", "http")


        r.clipboard_append(X)
        r.update()
        self.display_Hyperlink['text'] = X
  

    def clear(self):
        self.entry.delete(0, 'end')
        self.display_Hyperlink['text']=''
        


main()
