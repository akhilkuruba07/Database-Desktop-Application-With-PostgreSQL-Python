from tkinter import * 
import tkinter as tk
import psycopg2

def get_data(name,age,adderss):
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="Akhilsai@1234",host="localhost",port="5432")
    cur = conn.cursor()
    query=(''' insert into student(name,age,adderss) values(%s,%s,%s);''')
    cur.execute(query,(name,age,adderss))
    print("Data Inserted")
    conn.commit()
    conn.close()

def ID_Search(id):
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="Akhilsai@1234",host="localhost",port="5432")
    cur = conn.cursor()
    query=('''select * from student where id=%s;''')
    cur.execute(query,(id))
    row=cur.fetchmany()
    display_search(row)
    conn.commit()
    conn.close()
def display_search(row):
    listbox = Listbox(frame,width=20,height=1)
    listbox.grid(row=9,column=1)
    listbox.insert(END,row)
def dispaly_All():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="Akhilsai@1234",host="localhost",port="5432")
    cur = conn.cursor()
    query = '''select * from student;'''
    cur.execute(query)
    row= cur.fetchall()
    listbox = Listbox(frame,width=20,height=5)
    listbox.grid(row=10,column=1)
    for x in row:
        listbox.insert(END,x)


root = Tk()
canvas = Canvas(root,height=480,width=900)
canvas.pack()
color = colorchooser.askcolor()[1]  # Opens a color chooser dialog and returns the selected color
root.configure(bg=color)
frame = Frame()
frame.place(relx=0.3,rely=0.1,relwidth=0.8,relheight=0.8)

label =Label(frame,text="Add Data")
label.grid(row=0,column=1)
 
label =Label(frame,text="Name")
label.grid(row=1,column=0)
entry_name = Entry(frame)
entry_name.grid(row=1,column=1)

label =Label(frame,text="Age")
label.grid(row=2,column=0)
entry_age = Entry(frame)
entry_age.grid(row=2,column=1)

label =Label(frame,text="Adderss")
label.grid(row=3,column=0)

entry_Adderss = Entry(frame)
entry_Adderss.grid(row=3,column=1)

button= Button(frame,text="Add",command=lambda:get_data(entry_name.get(),entry_age.get(),entry_Adderss.get()))
button.grid(row=4,column=1)

# createing Serching fuctionalltiy
label =Label(frame,text="Search Data")
label.grid(row=5,column=1)
label =Label(frame,text="Search By ID")
label.grid(row=6,column=0)
entry_id = Entry(frame)
entry_id.grid(row=6,column=1)
button= Button(frame,text="Search",command=lambda:ID_Search(entry_id.get()))
button.grid(row=6,column=2)
dispaly_All()
root.mainloop() 
 