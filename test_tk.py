#!/usr/bin/env python3
#antuor:Alan

from tkinter import *

root = Tk()
label = Label(root,bg = 'blue',text="alan saxasxaxasxasxasis a pythoner",wraplength = 10,width = 10,height=3,anchor = 'nw',justify = 'left')
label.pack()
# for a in ['n','s','e','w','ne','nw','se','sw']:
#     Button(root,
#     text = 'anchor', anchor = a,
#     width = 10, height = 4).pack()

for b in [0,1,2,3,4]:
    Button(root, text = str(b), bd = b).pack()

def statePrint():
    print('ok')
for r in ['normal','active','disabled']:

    Button(root,
    text = r,
    state = r,
    width = 30,
    command = statePrint).pack()

# for r in ['raised','sunken','groove','ridge']:
#     Button(root,
#     text = r,
#     relief = r,
#     width = 30).pack()

##########################################
def psw():
    password = e.get()
    print("your psw:",password)

b = Button(root,text="submmit",command = psw)   #把变量赋值给textvariable
b.pack()
e = StringVar()
entry = Entry(root,textvariable = e)
e.set('input your text here')   #输入框初始值
entry['show'] = "*"
entry.pack()
def callCheckbutton():
#改变 v 的值,即改变 Checkbutton 的显示值 v.set('check Tkinter')

    v = StringVar()
    v.set('check python')
#绑定 v 到 Checkbutton 的属性 textvariable Checkbutton(root,
v = StringVar()
v.set('uuu python')
Checkbutton(root,
            text = 'chec python',
            textvariable = v,
            command = callCheckbutton ).pack()

lb = Listbox(root)



root.mainloop()

