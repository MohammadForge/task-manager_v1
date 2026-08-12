import tkinter as tk
Tasks = []

window = tk.Tk()
window.geometry('640x450')
window.config(bg='#0D0E14')

title_label = tk.Label(window, text='Task manager' , bg = '#0D0E14' , fg='white' , font=('segoe UI', 20 , 'bold'))
title_label.grid(row=0 , column=0 , columnspan=2 , pady=(20,10), sticky='e')


listbox1 = tk.Listbox(window,bg='#181A23' , fg='#FFFFFF',selectbackground='#7C5CFF',selectforeground= '#FFFFFF' ,font = ('segoe UI' , 12))
li_visible = False
def show_list():
    listbox1.grid(row = 2 , column = 1 , padx =10 , pady = 10)

def rem_list():
    global li_visible
    if li_visible:
        listbox1.grid_remove()
    else:
        show_list()
    li_visible = not li_visible




get_entry = tk.Entry(window, bg='#181A23',fg='#FFFFFF',insertbackground='#FFFFFF' , font = ('segoe UI', 13, 'normal'),width=20)

entry_visible = False

def rem_entry():
    global entry_visible
    if not entry_visible:
        show_entry()
        entry_visible = True
    else:
        if get_entry.get():
            add()
        get_entry.grid_remove()
        entry_visible = False


def show_entry():
    get_entry.grid(row = 2 , column = 1, padx=10 , pady = 10, sticky='ew')
    global li_visible 
    li_visible = True


def re_listbox():
    listbox1.delete(0 , tk.END)
    for task in Tasks:
        listbox1.insert(tk.END, task)

def add():
    res = get_entry.get()
    Tasks.append(res)
    label1.config(text = 'Added!', fg = '#00E676')
    get_entry.delete(0, tk.END)
    window.after(1500, lambda:label1.config(text= ''))
    re_listbox()

def delete():
    selection = listbox1.curselection()
    if not selection:
        label3.config(text = 'You are not selecting a task!' , fg='#FFC400')
        window.after(1000, lambda:label3.config(text= ''))
        return
    index = selection[0]
    Tasks.pop(index)
    label2.config(text = 'Deleted!',fg='#FF3B5C')
    window.after(1500, lambda:label2.config(text = ''))
    re_listbox()

  
button1 = tk.Button(window, width = 15, height = 2 , text = 'Add Tasks',font = ('segoe UI' , 14 , 'bold'))
button1.grid(row = 4 , column = 0 ,padx = 20 , pady= 10) 
button1.config(bg='#7C5CFF', fg='white' ,command=rem_entry)


button2 = tk.Button(window , width = 15 , height = 2 , text = 'Delete tasks',font = ('segoe UI' , 14 , 'bold'))
button2.grid(row = 4 , column= 1 , padx= 20 , pady= 10)
button2.config(bg ='#7C5CFF',fg='#FFFFFF' ,command=delete)

button3 = tk.Button(window , width = 15 , height = 2 , text = 'Your Tasks',font = ('segoe UI' , 14 , 'bold'))
button3.grid(row = 4 , column = 2 , padx = 20 , pady=10) 
button3.config(bg ='#7C5CFF',fg='#FFFFFF'  , command=rem_list)

label1 = tk.Label(window,bg='#0D0E14' , font = ('segoe UI' , 12 , 'bold'))
label1.grid(row = 1, column = 1 , padx = 5 , pady = 0 ,sticky='n')

label2 = tk.Label(window,bg='#0D0E14' , font=('segoe UI' , 12 ,'bold'))
label2.grid(row= 1 , column = 1 , padx= 5 , pady = 0 ,sticky='w' )

label3 = tk.Label(window,bg='#0D0E14', font = ('segoe UI' , 12 , 'normal'))
label3.grid(row = 1 , column = 1 , padx = 5 , pady = 0 , sticky = 'e'  )

window.mainloop()