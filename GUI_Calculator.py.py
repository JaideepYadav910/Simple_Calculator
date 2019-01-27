#Calculator made using python's tkinter module

from tkinter import *

class Application(Frame):
    """ Main class for calculator """

    def __init__(self, master):
        """ Initialise the Frame. """
        super(Application, self).__init__(master)
        self.task = ""
        self.UserIn = StringVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create all the buttons for calculator. """
        # User input stored as an Entry widget.

        self.user_input = Entry(self,
                                bg = "#ccffff",
                                bd = 5,
                                insertwidth = 1,
                                width = 15,
                                font = ("Franklin Gothic ...", 15, "bold"),
                                textvariable = self.UserIn,
                                justify = RIGHT)
        self.user_input.grid(columnspan = 4)
        self.user_input.insert(0, "0")

        # Button for value 7
        self.button1 = Button(self,
                             bg = "#99ffff",
                             bd = 10,
                             text = "7",
                             padx = 4,
                             pady = 4,
                             font = ("Arial", 10),
                             command = lambda : self.buttonClick(7))
        self.button1.grid(row = 2, column = 0, sticky = W)
        
        # Button for value 8
        self.button2 = Button(self,
                             bg = "#99ffff",
                             bd = 10,
                             text = "8",
                             padx = 4,
                             pady = 4,
                             font = ("Arial", 10),
                             command = lambda : self.buttonClick(8))
        self.button2.grid(row = 2, column = 1, sticky = W)
        
        # Button for value 9
        self.button3 = Button(self,
                             bg = "#99ffff",
                             bd = 10,
                             text = "9",
                             padx = 4,
                             pady = 4,
                             font = ("Arial", 10),
                             command = lambda : self.buttonClick(9))
        self.button3.grid(row = 2, column = 2, sticky = W)
        
        # Button for value 4
        self.button4 = Button(self,
                             bg = "#99ffff",
                             bd = 10,
                             text = "4",
                             padx = 4,
                             pady = 4,
                             font = ("Arial", 10),
                             command = lambda : self.buttonClick(4))
        self.button4.grid(row = 3, column = 0, sticky = W)
        
        # Button for value 5
        self.button5 = Button(self,
                             bg = "#99ffff",
                             bd = 10,
                             text = "5",
                             padx = 4,
                             pady = 4,
                             font = ("Arial", 10),
                             command = lambda : self.buttonClick(5))
        self.button5.grid(row = 3, column = 1, sticky = W)
        
        # Button for value 6
        self.button6 = Button(self,
                             bg = "#99ffff",
                             bd = 10,
                             text = "6",
                             padx = 4,
                             pady = 4,
                             font = ("Arial", 10),
                             command = lambda : self.buttonClick(6))
        self.button6.grid(row = 3, column = 2, sticky = W)
        
        # Button for value 1
        self.button7 = Button(self,
                             bg = "#99ffff",
                             bd = 10,
                             text = "1",
                             padx = 4,
                             pady = 4,
                             font = ("Arial", 10),
                             command = lambda : self.buttonClick(1))
        self.button7.grid(row = 4, column = 0, sticky = W)
        
        # Button for value 2
        self.button8 = Button(self,
                             bg = "#99ffff",
                             bd = 10,
                             text = "2",
                             padx = 4,
                             pady = 4,
                             font = ("Arial", 10),
                             command = lambda : self.buttonClick(2))
        self.button8.grid(row = 4, column = 1, sticky = W)
        
        # Button for value 3
        self.button9 = Button(self,
                             bg = "#99ffff",
                             bd = 10,
                             text = "3",
                             padx = 4,
                             pady = 4,
                             font = ("Arial", 10),
                             command = lambda : self.buttonClick(3))
        self.button9.grid(row = 4, column = 2, sticky = W)
        
        # Button for value 0
        self.button0 = Button(self,
                             bg = "#99ffff",
                             bd = 10,
                             text = "0",
                             padx = 4,
                             pady = 4,
                             font = ("Arial", 10),
                             command = lambda : self.buttonClick(0))
        self.button0.grid(row = 5, column = 0, sticky = W)


        # Operator buttons
        # Addition button
        self.Addbutton = Button(self,
                                bg = "#99ffff",
                                bd = 10,
                                text = "+",
                                padx = 4,
                                pady = 4,
                                command = lambda : self.buttonClick("+"),
                                font = ("Arial", 10, "bold"))
        self.Addbutton.grid(row = 2, column = 3, sticky = W)

        
        # Subtraction button
        self.Subbutton = Button(self,
                                bg = "#99ffff",
                                bd = 10,
                                text = "- ",
                                padx = 4,
                                pady = 4,
                                command = lambda : self.buttonClick("-"),
                                font = ("Arial", 10, "bold"))
        self.Subbutton.grid(row = 3, column = 3, sticky = W)

            
        # Multiplication button
        self.Multbutton = Button(self,
                                bg = "#99ffff",
                                bd = 10,
                                text = "* ",
                                padx = 4,
                                pady = 4,
                                command = lambda : self.buttonClick("*"),
                                font = ("Arial", 10, "bold"))
        self.Multbutton.grid(row = 4, column = 3, sticky = W)

        
        # Division button
        self.Divbutton = Button(self,
                                bg = "#99ffff",
                                bd = 10,
                                text = "/ ",
                                padx = 4,
                                pady = 4,
                                command = lambda : self.buttonClick("/"),
                                font = ("Arial", 10, "bold"))
        self.Divbutton.grid(row = 5, column = 3, sticky = W)

        
        # Equal button
        self.Equalbutton = Button(self,
                                bg = "#99ffff",
                                bd = 10,
                                text = "      =     ",
                                padx = 4,
                                pady = 4,
                                command = self.CalculateTask,
                                font = ("Arial", 10))
        self.Equalbutton.grid(row = 5, column = 1, columnspan = 2, sticky = W)

                
        # Clear button
        self.Clearbutton = Button(self,
                                bg = "#99ffff",
                                bd = 10,
                                text = "                AC               ",
                                padx = 4,
                                pady = 4,
                                command = self.ClearDisplay,
                                font = ("Arial", 10, "bold"))
        self.Clearbutton.grid(row = 1, column = 0, columnspan = 4, sticky = W)


    def buttonClick(self, number):
        self.task = str(self.task) + str(number)
        self.UserIn.set(self.task)

    def CalculateTask(self):
        self.data = self.user_input.get()
        try:
            self.answer = eval(self.data)
            self.displayText(self.answer)
            self.task = self.answer

        except SyntaxError as e:
            self.displayText("Invalid Syntax!")
            self.task = ""

    def displayText(self, value):
        self.user_input.delete(0, END)
        self.user_input.insert(0, value)

    def ClearDisplay(self):
        self.task = ""
        self.user_input.delete(0, END)
        self.user_input.insert(0, "0")
        
    
calc = Tk()

calc.title("Calculator")
app = Application(calc)
# Make window not resizable
calc.resizable(width = False, height = False)

calc.mainloop()

        
