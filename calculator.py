from tkinter import *
import tkinter.font

cal=Tk()
cal.title('계산기')
cal.geometry('300x500')

def calculate(num):
    if display_label['text'] == '0' or display_label['text'] == 0:
        display_label.config(text = num)
    else :
        display_label.config(text=str(display_label['text'])+str(num))
def dot():
    display_label.config(text=str(display_label['text']) + '.')

def angle():
    btext = before_label['text']
    if display_label['text']==0:
            display_label.config(text='(')
    elif btext.count('(') == btext.count(')'):
       before_label.config(text=str(btext)+'(')
    elif btext.count('(') == btext.count(')') + 1:
        before_label.config(text=str(before_label['text'])+str(display_label['text'])+')')
        display_label.config(text='')

def delete():
    dtext = str(display_label['text'])
    btext = str(before_label['text'])
    if display_label['text']=='0' or display_label['text']=='':
        if len(btext) == 1:
            before_label.config(text = '')
        else:   before_label.config(text=btext[:-1])
    else:
        if len(dtext) == 1:
            display_label.config(text = '0')
        else :  display_label.config(text = dtext[:-1])
def percent():
    display_label.config(text = int(display_label['text']) / 100)
def alldel():
    before_label.config(text = '')
    display_label.config(text = '0')
def before(opr):
    btext = str(before_label['text'])
    if btext[-1:] in ['+', '-', '*', '/'] and display_label['text']=='':
        before_label.config(text = btext[:-1] + opr)
    else:
        before_label['text'] += str(display_label['text']) + str(opr)
        display_label['text'] = ''
def result():
    try:
        cal_result = before_label['text'] + str(display_label['text'])
        display_label['text'] = eval(cal_result)
        before_label['text'] = ''
    except ZeroDivisionError:
        before_label['text'] = ''
        display_label['text'] = 0
    except SyntaxError:
        before_label['text'] = ''
        display_label['text'] = 0

font=tkinter.font.Font(family='맑은 고딕', size=13, weight='bold')

main_frame = Frame(cal)
display_frame = Frame(main_frame)
before_label = Label(display_frame, text='', font=font, height=1, anchor='e', padx=5, pady=5, bg='white')
display_label = Label(display_frame, text='0', font=font, height =3, anchor = 'e', padx = 5, pady = 5, bg = 'white')
input_frame = Frame(main_frame)
calc_frame = Frame(input_frame)
num_frame = Frame(input_frame)

calline = Frame(num_frame)
numline1 = Frame(num_frame)
numline2 = Frame(num_frame)
numline3 = Frame(num_frame)
numline4 = Frame(num_frame)

num_btn7 = Button(numline1, text='7', font=font, height=2, width=6, command=(lambda x=7: calculate(x)))
num_btn8 = Button(numline1, text='8', font=font, height=2, width=6, command=(lambda x=8: calculate(x)))
num_btn9 = Button(numline1, text='9', font=font, height=2, width=6, command=(lambda x=9: calculate(x)))
num_btn4 = Button(numline2, text='4', font=font, height=2, width=6, command=(lambda x=4: calculate(x)))
num_btn5 = Button(numline2, text='5', font=font, height=2, width=6, command=(lambda x=5: calculate(x)))
num_btn6 = Button(numline2, text='6', font=font, height=2, width=6, command=(lambda x=6: calculate(x)))
num_btn1 = Button(numline3, text='1', font=font, height=2, width=6, command=(lambda x=1: calculate(x)))
num_btn2 = Button(numline3, text='2', font=font, height=2, width=6, command=(lambda x=2: calculate(x)))
num_btn3 = Button(numline3, text='3', font=font, height=2, width=6, command=(lambda x=3: calculate(x)))
num_btn_dot = Button(numline4, text = '.', font=font, height=2, width=6, command=dot)
num_btn0 = Button(numline4, text = '0', font=font, height=2, width=6, command=(lambda x=0: calculate(x)))
c_btn = Button(numline4, text = 'c', font=font, height=2, width=6, command=alldel)

ang_btn = Button(calline, text = '(  )', font=font, height=2, width=6, bg='gray70', command=angle)
per_btn = Button(calline, text = '%', font=font, height=2, width=6, bg='gray70', command=percent)
del_btn = Button(calline, text = '←', font=font, height=2, width=6, bg='gray70', command=delete)
add_btn = Button(calc_frame, text = '+', font=font, height=2, width=6, bg='gray70', command=(lambda x='+': before(x)))
sub_btn = Button(calc_frame, text = '-', font=font, height=2, width=6, bg='gray70', command=(lambda x='-': before(x)))
mul_btn = Button(calc_frame, text = '*', font=font, height=2, width=6, bg='gray70', command=(lambda x='*': before(x)))
div_btn = Button(calc_frame, text = '/', font=font, height=2, width=6, bg='gray70', command=(lambda x='/': before(x)))
result_btn = Button(calc_frame, text = '=', font=font, height=2, width=6, bg='RosyBrown1', command=result)

#pack
main_frame.pack(expand=YES, fill=BOTH)
display_frame.pack(expand=YES, fill=BOTH)
input_frame.pack(expand=YES, fill=BOTH)
before_label.pack(expand=YES, fill=BOTH)
display_label.pack(expand=YES, fill=BOTH)
num_frame.pack(side=LEFT)
calc_frame.pack(side=LEFT)
calline.pack()
numline1.pack()
numline2.pack()
numline3.pack()
numline4.pack()

space = 3
ang_btn.pack(side=LEFT, padx = space, pady = space)
per_btn.pack(side=LEFT, padx = space, pady = space)
del_btn.pack(side=LEFT, padx = space, pady = space)

num_btn7.pack(side=LEFT, padx=space, pady=space)
num_btn8.pack(side=LEFT, padx=space, pady=space)
num_btn9.pack(side=LEFT, padx=space, pady=space)
num_btn4.pack(side=LEFT, padx=space, pady=space)
num_btn5.pack(side=LEFT, padx=space, pady=space)
num_btn6.pack(side=LEFT, padx=space, pady=space)
num_btn1.pack(side=LEFT, padx=space, pady=space)
num_btn2.pack(side=LEFT, padx=space, pady=space)
num_btn3.pack(side=LEFT, padx=space, pady=space)
num_btn_dot.pack(side=LEFT, padx=space, pady=space)
num_btn0.pack(side=LEFT, padx=space, pady=space)
c_btn.pack(side=LEFT, padx=space, pady=space)

add_btn.pack(pady=space)
sub_btn.pack(pady=space)
mul_btn.pack(pady=space)
div_btn.pack(pady=space)
result_btn.pack(pady=space)

cal.mainloop()
