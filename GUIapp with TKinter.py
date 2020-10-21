import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title('GUI')

name_label=ttk.Label(win,text='Enter your name :')
name_label.grid(row=0,column=0,sticky=tk.W)


age_label=ttk.Label(win,text='Enter your age :')
age_label.grid(row=2,column=0,sticky=tk.W)

gender_label=ttk.Label(win,text='Select your gender : ')
gender_label.grid(row=3,column=0,sticky = tk.W)

email_label=ttk.Label(win,text='Enter your Email :')
email_label.grid(row=1,column=0,sticky=tk.W)

name_Var = tk.StringVar()
name_entrybox = ttk.Entry(win,width=20,textvariable = name_Var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()


email_Var = tk.StringVar()
email_entrybox = ttk.Entry(win,width=20,textvariable = email_Var)
email_entrybox.grid(row=1,column=1)
email_entrybox.focus()

age_Var= tk.StringVar()
age_entrybox = ttk.Entry(win,width=20,textvariable = age_Var)
age_entrybox.grid(row=2,column=1)


gender_Var = tk.StringVar()
gender_combobox = ttk.Combobox(win,width=16,textvariable=gender_Var,state='readonly')
gender_combobox['values'] = ('Male','Female','Transgender')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)

usertype=tk.StringVar()
radiobtn1 = ttk.Radiobutton(win,text='Student',value='Student',variable=usertype)
radiobtn1.grid(row=4,column=0)

radiobtn2 = ttk.Radiobutton(win,text='Teacher',value='Teacher',variable=usertype)
radiobtn2.grid(row=4,column=1)

checkbtn_Var = tk.IntVar()
checkbtn = ttk.Checkbutton(win,text='check if you want to subscribe a newsletter',variable=checkbtn_Var)
checkbtn.grid(row=5,column=3)


def action():
     username = name_Var.get()
     userage = age_Var.get()
     user_email = email_Var.get()
     print(f'{username} is {userage} year old , {user_email}')
     user_gender=gender_Var.get()
     user_type = usertype.get()
     if checkbtn_Var.get()==0:
          subscribed = 'NO'
     else:
          subscribed = 'YES'
     print(user_gender,user_type,subscribed)

     with open('gui_file.txt','a') as f:

          f.write(f'{username},{userage},{user_email},{user_gender},{user_type},{subscribed}\n')

     name_entrybox.delete(0,tk.END)
     age_entrybox.delete(0,tk.END)
     email_entrybox.delete(0,tk.END)
     
submit_button = tk.Button(win,text='Submit',command=action)
submit_button.grid(row=6,column=3)
submit_button.configure(foreground='Blue')

win.mainloop
