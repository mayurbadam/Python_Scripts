import tkinter 
m = tkinter.Tk()
'''
widgets are added here
'''
w1=tkinter.Button(m, text='+', width=10)#, .grid(row =0, column=0))
w2=tkinter.Button(m, text='-', width=10)#, .grid(row =0, column=1)) 
w3=tkinter.Button(m, text='x', width=10)#, .grid(row =1, column=0))
w4=tkinter.Button(m, text='/', width=10)#, .grid(row =1, column=1))
w1.pack()
w2.pack()
w3.pack()
w4.pack()

m.mainloop()
