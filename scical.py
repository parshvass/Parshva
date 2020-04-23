from tkinter import *
import math
import tkinter.messagebox

root = Tk()

root.configure(background="black") 
root.title('Scientific Calculator by Parshva')
root.geometry("320x150")

equation =""
equation1 =""
tkinter.messagebox.showinfo("DISCLAIMER","Please use Brackets Correctly")
eq = StringVar()
express_field = Entry(root,textvariable = eq)
express_field.grid(columnspan=5, ipadx=80)

eq.set('Please Enter Your Expression')

def click(num):
    global equation,equation1
    a = equation = equation + str(num)
    eq.set(equation)
	equation1 = a

def clear():
	global equation
	equation=""
	eq.set("")

def evaluate():
	global equation
	ans = eval(equation)
	equation= str(ans)
	eq.set(f'{ans}')

'''
def popstr():
    global equation
	equation = equation[:-1]
    eq.set(equation)
'''
button1 = Button(root, text='1', bg='black', fg='red', command=lambda: click(1), height=1, width=7) 
button1.grid(row=2, column=0)

button2 = Button(root, text='2', bg='black', fg='red', command=lambda: click(2), height=1, width=7) 
button2.grid(row=2, column=1)

button3 = Button(root, text='3', bg='black', fg='red', command=lambda: click(3), height=1, width=7) 
button3.grid(row=2, column=2)

button4 = Button(root, text='4', bg='black', fg='red', command=lambda: click(4), height=1, width=7) 
button4.grid(row=3, column=0)

button5 = Button(root, text='5', bg='black', fg='red', command=lambda: click(5), height=1, width=7) 
button5.grid(row=3, column=1)

button6 = Button(root, text='6', bg='black', fg='red', command=lambda: click(6), height=1, width=7) 
button6.grid(row=3, column=2)

button7 = Button(root, text='7', bg='black', fg='red', command=lambda: click(7), height=1, width=7) 
button7.grid(row=4, column=0)

button8 = Button(root, text='8', bg='black', fg='red', command=lambda: click(8), height=1, width=7) 
button8.grid(row=4, column=1)

button9 = Button(root, text='9', bg='black', fg='red', command=lambda: click(9), height=1, width=7) 
button9.grid(row=4, column=2)

button0 = Button(root, text='0', bg='black', fg='red', command=lambda: click(0), height=1, width=7) 
button0.grid(row=5, column=1)

buttonlp = Button(root, text='(', bg='black', fg='red', command=lambda: click('('), height=1, width=7) 
buttonlp.grid(row=5, column=0)

buttonrp = Button(root, text=')', bg='black', fg='red', command=lambda: click(')'), height=1, width=7) 
buttonrp.grid(row=5, column=2)

buttonplus = Button(root, text='+', bg='black', fg='red', command=lambda: click('+'), height=1, width=7) 
buttonplus.grid(row=2, column=3)

buttonmin = Button(root, text='-', bg='black', fg='red', command=lambda: click('-'), height=1, width=7) 
buttonmin.grid(row=3, column=3)

buttondiv = Button(root, text='/', bg='black', fg='red', command=lambda: click('/'), height=1, width=7) 
buttondiv.grid(row=4, column=3)

buttonmul = Button(root, text='*', bg='black', fg='red', command=lambda: click('*'), height=1, width=7) 
buttonmul.grid(row=5, column=3)

buttoneq = Button(root, text='=', bg='black', fg='red', command=evaluate, height=1, width=7) 
buttoneq.grid(row=6, columnspan=3)

buttonsin = Button(root,text='sin',width=6, bg='black', fg='red',command=lambda : click('math.sin('))
buttonsin.grid(row=2, column=4)

buttoncos = Button(root,text='cos',width=6, bg='black', fg='red',command=lambda : click('math.cos('))
buttoncos.grid(row=3, column=4)

buttontan = Button(root,text='tan',width=6, bg='black', fg='red',command=lambda : click('math.tan('))
buttontan.grid(row=4, column=4)

buttonlog = Button(root,text='ln',width=6, bg='black', fg='red',command=lambda : click('math.log('))
buttonlog.grid(row=5, column=4)

buttonpwr = Button(root,text='^',width=6, bg='black', fg='red',command=lambda : click('**'))
buttonpwr.grid(row=6, column=4)

buttonsqrt = Button(root,text='√',width=7, bg='black', fg='red',command=lambda : click('math.sqrt('))
buttonsqrt.grid(row=6, column=3)

buttonclr = Button(root,text='CLEAR',width=7, bg='black', fg='red',command= clear)
buttonclr.grid(row=6, column=2)

buttondt = Button(root,text='.',width=7, bg='black', fg='red',command=lambda : click('.'))
buttondt.grid(row=6, column=0)

buttonpie = Button(root, text='π', bg='black', fg='red', command=lambda: click(3.1415926535), height=1, width=7) 
buttonpie.grid(row=4, column=5)

buttone = Button(root, text='e', bg='black', fg='red', command=lambda: click(2.71828182845), height=1, width=7) 
buttone.grid(row=3, column=5)

''''
buttone = Button(root, text='Back', bg='black', fg='red', command= popstr(), height=1, width=7) 
buttone.grid(row=2, column=5)
'''

root.mainloop()
