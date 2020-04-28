#Ganesh Jainarain
#May 3, 2019
#Compound Interest Calc GUI
#28 Final Review

from tkinter import *

def main():
    program = CompoundProgram()

    program.window.mainloop()


class CompoundProgram:

    def __init__(self):
        self.window = Tk()
        self.my_display = None
        self.my_displayString = ""
        self.create_widgets()

    def create_widgets(self):
        self.my_display = Label(self.window, text=self.my_displayString, padx =40)
        self.my_display.grid(row=6,column=1, columnspan = 2)

        headerLabel = Label(self.window, text = "COMPOUND INTEREST CALCULATOR", font = ("Helvetica",13,"bold"))
        headerLabel.grid(row = 0, column = 0, columnspan = 3)

        designLabel = Label(self.window, text = "##############################################",font = ("Helvetica",13,"bold"))
        designLabel.grid(row = 1, column = 0, columnspan = 3)

        quit_button = Button(self.window,text="Quit",font = ("Helvetica",13,"bold"), command=self.window.destroy,padx =30)
        quit_button.grid(row=9,column= 0,columnspan = 2)

        InterestLabel = Label(self.window, text = "Interest = ")
        InterestLabel.grid(row = 6, column = 0,columnspan = 2)



        ###########################################################
        label1 = Label(self.window, text = "Enter Principal amt:")
        label1.grid(row = 2, column = 0)
        self.entry1 = Entry(self.window)
        self.entry1.grid(row = 2, column = 1)
        ###########################################################
        
        ###########################################################
        label2 = Label(self.window, text = "Enter yearly Rate:")
        label2.grid(row = 3, column = 0)
        self.entry2 = Entry(self.window)
        self.entry2.grid(row = 3, column = 1)
        ###########################################################

        ###########################################################
        label3 = Label(self.window, text = "Enter # of times to compound per yr:")
        label3.grid(row = 4, column = 0)
        self.entry3 = Entry(self.window)
        self.entry3.grid(row = 4, column = 1)
        ###########################################################

        ###########################################################
        label4 = Label(self.window, text = "Enter number of years to invest:")
        label4.grid(row = 5, column = 0)
        self.entry4 = Entry(self.window)
        self.entry4.grid(row = 5, column = 1)
        ###########################################################

        ###########################################################

        convert_button = Button(self.window, text = "CALCULATE", command = self.Compound)
        convert_button.grid(row=7, column=0,columnspan = 2)

        self.Compound = Label(self.window)
        self.Compound.grid(row = 6, column = 1)

        self.buttonClear2 = Button(self.window, text="C",font = ("Helvetica",13,"bold"),command = self.clear2,padx =20)
        self.buttonClear2.grid(row=8,column=0, columnspan = 2)


    def Compound(self):
        P = float(self.entry1.get())
        r = float(self.entry2.get())
        n = float(self.entry3.get())
        t = float(self.entry4.get())
        Interest = P*((1 + r/n)**(n*t))-P
        self.Compound['text'] = "$"+ str(round(Interest,2))

    def clear2(self):
        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')
        self.entry3.delete(0, 'end')
        self.entry4.delete(0, 'end')
        self.Compound['text']=''


main()
    
        
        

        

        
        

        

        

        

        
        

