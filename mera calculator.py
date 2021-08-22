#!/usr/bin/env python
# coding: utf-8

# In[57]:


from tkinter import *
from tkinter.font import Font


# In[58]:


root = Tk()
root.title("mera first calculator")


# In[59]:


e = Entry(root,width=20,borderwidth=10,font=("Georgia",14))
e.grid(row=0,column=0,columnspan=3,padx=20,pady=20)


# In[60]:


def button_click(number):
    first=e.get()
    e.delete(0, END)
    e.insert(0, str(first)+str(number))
    
def button_clear():
    e.delete(0, END)
    
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    
    if maths == "addition":
        e.insert(0, f_num+int(second_number))
    if maths == "subtraction":
        e.insert(0, f_num-int(second_number))
    if maths == "multiplication":
        e.insert(0, f_num*int(second_number))
    if maths == "division":
        e.insert(0, f_num/int(second_number))

def button_add():
    first_number = e.get()
    global f_num
    global maths
    maths = "addition"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_sub():
    first_number = e.get()
    global f_num
    global maths
    maths = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_mul():
    first_number = e.get()
    global f_num
    global maths
    maths = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

    
def button_div():
    first_number = e.get()
    global f_num
    global maths
    maths = "division"
    f_num = int(first_number)
    e.delete(0, END)


# In[61]:


button1 = Button(root,text="1",width=5,height=1,bg="#8181FD",font=("Comic Sans MS",17),command= lambda:button_click(1))
button2 = Button(root,text="2",width=5,height=1,bg="#8181FD",font=("Comic Sans MS",17),command= lambda:button_click(2))
button3 = Button(root,text="3",width=5,height=1,bg="#8181FD",font=("Comic Sans MS",17),command= lambda:button_click(3))
button4 = Button(root,text="4",width=5,height=1,bg="#8181FD",font=("Comic Sans MS",17),command= lambda:button_click(4))
button5 = Button(root,text="5",width=5,height=1,bg="#8181FD",font=("Comic Sans MS",17),command= lambda:button_click(5))
button6 = Button(root,text="6",width=5,height=1,bg="#8181FD",font=("Comic Sans MS",17),command= lambda:button_click(6))
button7 = Button(root,text="7",width=5,height=1,bg="#8181FD",font=("Comic Sans MS",17),command= lambda:button_click(7))
button8 = Button(root,text="8",width=5,height=1,bg="#8181FD",font=("Comic Sans MS",17),command= lambda:button_click(8))
button9 = Button(root,text="9",width=5,height=1,bg="#8181FD",font=("Comic Sans MS",17),command= lambda:button_click(9))
button0 = Button(root,text="0",width=5,height=1,bg="#8181FD",font=("Comic Sans MS",17),command= lambda:button_click(0))
buttonADD = Button(root,text="+",width=5,height=1,bg="#BCFF00",font=("Comic Sans MS",17),command=button_add)
buttonEQ = Button(root,text="=",width=5,height=1,bg="#BCFF00",font=("Comic Sans MS",17),command=button_equal)
buttonCLR = Button(root,text="clear",padx=30,pady=5,fg="yellow",bg="red",font=("Comic Sans MS",13),command=button_clear)
buttonSUB = Button(root,text="-",width=5,height=1,bg="#BCFF00",font=("Comic Sans MS",17),command=button_sub)
buttonMUL = Button(root,text="X",width=5,height=1,bg="#BCFF00",font=("Comic Sans MS",17),command=button_mul)
buttonDIV = Button(root,text="/",width=5,height=1,bg="#BCFF00",font=("Comic Sans MS",17),command=button_div)


# In[62]:


button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
button0.grid(row=4,column=1)
buttonADD.grid(row=4,column=2)
buttonSUB.grid(row=4,column=0)
buttonMUL.grid(row=5,column=0)
buttonDIV.grid(row=5,column=1)
buttonEQ.grid(row=5,column=2)
buttonCLR.grid(row=6,column=1)


# In[63]:


root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




