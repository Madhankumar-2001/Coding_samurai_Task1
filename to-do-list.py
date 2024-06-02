from tkinter import * 
import tkinter.messagebox
import os


"""I used TASKS_FILE line to save the contents which are all entered in the to-do-list gets stored in the text file.
later it can be viewed """

TASKS_FILE = "tasks.txt"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox_task.insert(END, task.strip())


def save_tasks():
    tasks = listbox_task.get(0, END)
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def entertask():
    
    input_text = ""
    def add():
        input_text = entry_task.get(1.0, "end-1c")
        if input_text == "":
            tkinter.messagebox.showwarning(title="Warning!", message="Please Enter some Text")
        else:
            num_tasks = listbox_task.size() + 1
            listbox_task.insert(END, f"{num_tasks}. {input_text}")
            save_tasks()
            root1.destroy()
    root1 = Tk()
    root1.title("Add task")
    entry_task = Text(root1, width=40, height=4)
    entry_task.pack()
    button_temp = Button(root1, text="Add task", command=add)
    button_temp.pack()
    root1.mainloop()

def deletetask():
    selected = listbox_task.curselection()
    if selected:
        listbox_task.delete(selected[0])
        renumber_tasks()
        save_tasks()

def renumber_tasks():
    tasks = listbox_task.get(0, END)
    listbox_task.delete(0, END)
    for i, task in enumerate(tasks):
        task_text = task.split(". ", 1)[1]  
        listbox_task.insert(END, f"{i + 1}. {task_text}")

def markcompleted():
    marked = listbox_task.curselection()
    if marked:
        temp = marked[0]
        temp_marked = listbox_task.get(marked)
        if " ✔" in temp_marked:
            temp_marked = temp_marked.replace(" ✔", "")
        else:
            temp_marked = temp_marked + " ✔"
        listbox_task.delete(temp)
        listbox_task.insert(temp, temp_marked)
        save_tasks()

window = Tk()
window.title("To_Do_APP")

frame_task = Frame(window)
frame_task.pack()

listbox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=50, font="Helvetica")
listbox_task.pack(side=LEFT)

scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=RIGHT, fill=Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

load_tasks()
 
entry_button = Button(window, text="Add task", width=50, command=entertask)
entry_button.pack(pady=3)

delete_button = Button(window, text="Delete selected task", width=50, command=deletetask)
delete_button.pack(pady=3)

mark_button = Button(window, text="Mark as completed", width=50, command=markcompleted)
mark_button.pack(pady=3)

window.protocol("WM_DELETE_WINDOW", lambda: (save_tasks(), window.destroy()))

window.mainloop()
