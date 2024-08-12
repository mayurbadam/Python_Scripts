from tkinter import *

# globally declaring the expression variable
expression = "0b"
  
# Function to update numbers expression in the text entry box
def press(num):
    # point out the global expression variable
    global expression
 
    # concatenation of string
    expression = expression + str(num)
 
    # update the expression by using set method
    equation.set(expression)


# Function to update characters expression in the text entry box
def cpress(char):
    # point out the global expression variable
    global expression
 
    # concatenation of string
    expression = expression + char + "0b"
 
    # update the expression by using set method
    equation.set(expression)
 

# Function to convert to decimal
def radpress(rad):
    try:

        global expression
        if(rad == "Dec"):
           total = int(expression,2)
        elif(rad == "Hex"):
           total = int(expression,2)
           total = hex(total)
        elif(rad == "Oct"):
           total = int(expression,2)
           total = format(total,'o')
        
        equation.set(total)

        expression = ""

    # if error is generate then handle
    # by the except block

    except:

        equation.set(" error ")
        expression = ""

# Function to evaluate the final expression
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
 
    # Put that code inside the try block
    # which may generate the error
    try:
 
        global expression
 
        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(bin(round(eval(expression),3)))
 
        equation.set(total)
 
        # initialize the expression variable
        # by empty string
        expression = ""
 
    # if error is generate then handle
    # by the except block
    except:
 
        equation.set(" error ")
        expression = ""
 
 
# Function to clear the contents
# of text entry box
def clear():
    global expression
    expression = "0b"
    equation.set("0b")
 
 
# Driver code
if __name__ == "__main__":
    #GUI window using tkinter
    gui = Tk()
 
    # setting the background colour of GUI window
    gui.configure(background="grey")
 
    # setting the title of GUI window
    gui.title("Simple Calculator")
 
    # setting the configuration of GUI window
    gui.geometry("330x170")
 
    # Instance of StringVar(). It is the variable class.
    equation = StringVar()
 
    # creating the text entry box for showing the expression .
    expression_field = Entry(gui, textvariable=equation)
 
    # grid method is used for placing the widgets at respective positions in table like structure .
    expression_field.grid(columnspan=4, ipadx=70)
 
    # creating Buttons and place at a particular location inside the root window. 
    # when user presses the button, the command or function affiliated to that button is executed .
    button0 = Button(gui, text=' 0 ', fg='black', bg='white',
                    command=lambda: press(0), height=1, width=6)
    button0.grid(row=1, column=0)

    Float= Button(gui, text='.', fg='black', bg='white',
                    command=lambda: press('.'), height=1, width=6)
    Float.grid(row=1, column=1)

    clear = Button(gui, text='Clear', fg='black', bg='white',
                command=clear, height=1, width=6)
    clear.grid(row=1, column=2)

    button1 = Button(gui, text=' 1 ', fg='black', bg='white',
                    command=lambda: press(1), height=1, width=6)
    button1.grid(row=2, column=0)

    equal = Button(gui, text=' = ', fg='black', bg='white',
                command=equalpress, height=1, width=6)
    equal.grid(row=2, column=1)
 
    divide = Button(gui, text=' / ', fg='black', bg='white',
                    command=lambda: cpress("/"), height=1, width=6)
    divide.grid(row=2, column=2)

    plus = Button(gui, text=' + ', fg='black', bg='white',
                command=lambda: cpress("+"), height=1, width=6)
    plus.grid(row=3, column=0)
 
    minus = Button(gui, text=' - ', fg='black', bg='white',
                command=lambda: cpress("-"), height=1, width=6)
    minus.grid(row=3, column=1)
 
    multiply = Button(gui, text=' * ', fg='black', bg='white',
                    command=lambda: cpress("*"), height=1, width=6)
    multiply.grid(row=3, column=2)
 
    Decimal= Button(gui, text='Dec', fg='black', bg='white',
                    command=lambda: radpress('Dec'), height=1, width=6)
    Decimal.grid(row=6, column=0)
    Hexadecimal= Button(gui, text='Hex', fg='black', bg='white',
                    command=lambda: radpress('Hex'), height=1, width=6)
    Hexadecimal.grid(row=6, column=1)
    Octal= Button(gui, text='Oct', fg='black', bg='white',
                    command=lambda: radpress('Oct'), height=1, width=6)
    Octal.grid(row=6, column=2)
    
    # starting the GUI
    gui.mainloop()



    #button2 = Button(gui, text=' 2 ', fg='black', bg='white',
    #                command=lambda: press(2), height=1, width=6)
    #button2.grid(row=2, column=1)
 
    #button3 = Button(gui, text=' 3 ', fg='black', bg='white',
    #                command=lambda: press(3), height=1, width=6)
    #button3.grid(row=2, column=2)
 
    #button4 = Button(gui, text=' 4 ', fg='black', bg='white',
    #                command=lambda: press(4), height=1, width=6)
    #button4.grid(row=3, column=0)
 
    #button5 = Button(gui, text=' 5 ', fg='black', bg='white',
    #                command=lambda: press(5), height=1, width=6)
    #button5.grid(row=3, column=1)
 
    #button6 = Button(gui, text=' 6 ', fg='black', bg='white',
    #                command=lambda: press(6), height=1, width=6)
    #button6.grid(row=3, column=2)
 
    #button7 = Button(gui, text=' 7 ', fg='black', bg='white',
    #                command=lambda: press(7), height=1, width=6)
    #button7.grid(row=4, column=0)
 
    #button8 = Button(gui, text=' 8 ', fg='black', bg='white',
    #                command=lambda: press(8), height=1, width=6)
    #button8.grid(row=4, column=1)
 
    #button9 = Button(gui, text=' 9 ', fg='black', bg='white',
    #                command=lambda: press(9), height=1, width=6)
    #button9.grid(row=4, column=2)
