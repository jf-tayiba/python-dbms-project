import mysql.connector

import tkinter as tk
from tkinter import ttk


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="173212",
    database="testdb"
)

cur = conn.cursor()


root = tk.Tk()
root.title("MySQL Viewer")
root.geometry("600x500")

title_label = tk.Label(root, text="MySQL Data Viewer", font=("Arial", 16, "bold"))
title_label.pack(pady=10)


#list_box = tk.Listbox(root, width=80, height=20)
#list_box.pack(pady=10)


#scroll = tk.Scrollbar(root)
#scroll.pack(side=tk.RIGHT, fill=tk.Y)

#list_box.config(yscrollcommand=scroll.set)
#scroll.config(command=list_box.yview)





"""def show_news():
    list_box.delete(0, tk.END)
    cur.execute("SELECT * FROM news")
    rows = cur.fetchall()

    list_box.insert(tk.END, "---- NEWS TABLE ----")
    for r in rows:
        list_box.insert(tk.END, str(r))"""
#id, newsid, title, body, created_at
def show_news():
    window = tk.Toplevel(root)
    window.title("All news")
    tree = ttk.Treeview(window, columns=("news_id","title","body", "date","user_id"), show="headings")
    
    tree.heading("news_id", text="news_id")
    tree.heading("title", text="title")
    tree.heading("body", text="body")
    tree.heading("date", text="date")
    tree.heading("user_id", text="user_id")

    tree.pack(fill=tk.BOTH, expand=True)
    for row in tree.get_children():
        tree.delete(row)
    cur.execute("SELECT * FROM news")
    rows = cur.fetchall()

    for r in rows:
        tree.insert("",tk.END, values=r)


#id, newsid, title, body, created_at
def add_news():
    win = tk.Toplevel(root)
    win.title("Add news")
    win.geometry("300x200")


    

    ttk.Label(win, text="news_id:").grid(row=1, column=0, padx=10, pady=5)
    entry_newsid= ttk.Entry(win, width=30)
    entry_newsid.grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(win, text="title:").grid(row=2, column=0, padx=10, pady=5)
    entry_title= ttk.Entry(win, width=30)
    entry_title.grid(row=2, column=1, padx=10, pady=5)
    
    ttk.Label(win, text="body:").grid(row=3, column=0, padx=10, pady=5)
    entry_body= ttk.Entry(win, width=30)
    entry_body.grid(row=3, column=1, padx=10, pady=5)

    ttk.Label(win, text="created_at:").grid(row=4, column=0, padx=10, pady=5)
    entry_created_at= ttk.Entry(win, width=30)
    entry_created_at.grid(row=4, column=1, padx=10, pady=5)

    ttk.Label(win, text="user_id:").grid(row=0, column=0, padx=10, pady=5)
    entry_id = ttk.Entry(win, width=30)
    entry_id.grid(row=0, column=1, padx=10, pady=5)

    def save_news():
        
        news_id = entry_newsid.get().strip()
        title = entry_title.get().strip()
        body = entry_body.get().strip()
        created_at = entry_created_at.get().strip()
        user_id = entry_id.get().strip()
        cur.execute("INSERT INTO news VALUES(%s,%s,%s,%s,%s)",(news_id,title,body,created_at,user_id,))
        conn.commit()
        win.destroy()
        

        #Button(win, text="Save", command=save_users).pack()
        
    ttk.Button(win, text="Save", command=save_news).grid(row=4, column=1)

def delete_news():
    win=tk.Toplevel(root)
    win.title("delete news")
    win.geometry("300x200")

    ttk.Label(win,text="news_id:").grid(row=0,column=0,padx=10,pady=5)
    entry_newsid=ttk.Entry(win,width=30)
    entry_newsid.grid(row=0,column=1,padx=0,pady=5)
    
    def save_id():
        news_id=entry_newsid.get().strip()
        cur.execute("DELETE FROM news WHERE id=%s",(id,) )
        conn.commit()
        win.destroy()
    ttk.Button(win,text="SAVE",command=save_id).grid(row=5,column=1)

def update_news():
    win = tk.Toplevel(root)
    win.title("Update news")
    win.geometry("300x250")

    

    ttk.Label(win, text="news_id:").grid(row=1, column=0, padx=10, pady=5)
    entry_newsid= ttk.Entry(win, width=30)
    entry_newsid.grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(win, text="title:").grid(row=2, column=0, padx=10, pady=5)
    entry_title= ttk.Entry(win, width=30)
    entry_title.grid(row=2, column=1, padx=10, pady=5)
    
    ttk.Label(win, text="body:").grid(row=3, column=0, padx=10, pady=5)
    entry_body= ttk.Entry(win, width=30)
    entry_body.grid(row=3, column=1, padx=10, pady=5)

    ttk.Label(win, text="created_at:").grid(row=4, column=0, padx=10, pady=5)
    entry_created_at= ttk.Entry(win, width=30)
    entry_created_at.grid(row=4, column=1, padx=10, pady=5)


    ttk.Label(win, text="user_id:").grid(row=0, column=0, padx=10, pady=5)
    entry_userid = ttk.Entry(win, width=30)
    entry_userid.grid(row=0, column=1, padx=10, pady=5)


    def save_update():
        userid = entry_userid.get().strip()
        newsid = entry_newsid.get().strip()
        title = entry_title.get().strip()
        body = entry_body.get().strip()
        created_at = entry_created_at.get().strip()

        cur.execute("UPDATE news SET title=%s,body=%s,created_at=%s WHERE userid=%s",
                    (title,body,created_at, userid))
        conn.commit()
        win.destroy()

    ttk.Button(win, text="Save Update", command=save_update).grid(row=3, column=1, pady=10)



def show_users():
    window = tk.Toplevel(root)
    window.title("All users")
    tree = ttk.Treeview(window, columns=("userid","name","email","age","contact_number"), show="headings")
    tree.heading("userid", text="userid")
    tree.heading("name", text="name")
    tree.heading("email", text="email")
    tree.heading("age", text="age")
    tree.heading("contact_number", text="contact_number")
    
    tree.pack(fill=tk.BOTH, expand=True)
    for row in tree.get_children():
        tree.delete(row)
    cur.execute("SELECT * FROM user")
    rows = cur.fetchall()

    for r in rows:
        tree.insert("",tk.END, values=r)



"""def add_users():
    win = tk.Toplevel(root)
    win.title("Add User")
    win.geometry("300x200")


    ttk.Label(win, text="Name:").grid(row=0, column=0, padx=10, pady=5)
    entry_name = ttk.Entry(win, width=30)
    entry_name.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(win, text="email:").grid(row=1, column=0, padx=10, pady=5)
    entry_email= ttk.Entry(win, width=30)
    entry_email.grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(win, text="id:").grid(row=2, column=0, padx=10, pady=5)
    entry_id= ttk.Entry(win, width=30)
    entry_id.grid(row=2, column=1, padx=10, pady=5)



    id = entry_id.get().strip()
    name = entry_name.get().strip()
    email = entry_email.get()


    cur.execute("INSERT INTO user VALUES (%s, %s, %s)", (id, name, email))
    conn.commit()
    win.destroy()

    ttk.Button(win, text="Save", command=save).grid(row=3, column=1, pady=10)"""


def add_users():
    win = tk.Toplevel(root)
    win.title("Add User")
    win.geometry("300x200")

    ttk.Label(win, text="userid:").grid(row=2, column=0, padx=10, pady=5)
    entry_userid= ttk.Entry(win, width=30)
    entry_userid.grid(row=2, column=1, padx=10, pady=5)

    ttk.Label(win, text="Name:").grid(row=0, column=0, padx=10, pady=5)
    entry_name = ttk.Entry(win, width=30)
    entry_name.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(win, text="email:").grid(row=1, column=0, padx=10, pady=5)
    entry_email= ttk.Entry(win, width=30)
    entry_email.grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(win, text="age:").grid(row=2, column=0, padx=10, pady=5)
    entry_age= ttk.Entry(win, width=30)
    entry_age.grid(row=2, column=2, padx=10, pady=5)

    ttk.Label(win, text="contact_number:").grid(row=3, column=0, padx=10, pady=5)
    entry_num= ttk.Entry(win, width=30)
    entry_num.grid(row=3, column=2, padx=10, pady=5)

    
    
    
    def save_users():
        name = entry_name.get().strip()
        user_id = entry_userid.get().strip()
        email = entry_email.get().strip()
        age = entry_age.get().strip()
        contact_number = entry_num.get().strip()

        cur.execute("INSERT INTO user VALUES(%s,%s,%s,%s,%s)",(user_id,name,email,age,contact_number))
        conn.commit()
        win.destroy()
        

        #Button(win, text="Save", command=save_users).pack()
        
    ttk.Button(win, text="Save", command=save_users).grid(row=4, column=1)

def delete_user():
    win = tk.Toplevel(root)
    win.title("delete User")
    win.geometry("300x200")

    ttk.Label(win, text="userid:").grid(row=0, column=0, padx=10, pady=5)
    entry_userid= ttk.Entry(win, width=30)
    entry_userid.grid(row=0, column=1, padx=10, pady=5)

    def save_delete():
        delete_userid = entry_userid.get().strip()
        cur.execute("DELETE FROM user WHERE id=%s",(delete_userid,))
        conn.commit()
        win.destroy()
    ttk.Button(win, text="Save", command=save_delete).grid(row=4, column=1)

def update_user():
    win = tk.Toplevel(root)
    win.title("Update User")
    win.geometry("300x250")

    ttk.Label(win, text="User ID:").grid(row=0, column=0, padx=10, pady=5)
    entry_userid = ttk.Entry(win, width=30)
    entry_userid.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(win, text="New Name:").grid(row=1, column=0, padx=10, pady=5)
    entry_name = ttk.Entry(win, width=30)
    entry_name.grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(win, text="New Email:").grid(row=2, column=0, padx=10, pady=5)
    entry_email = ttk.Entry(win, width=30)
    entry_email.grid(row=2, column=1, padx=10, pady=5)

    
    ttk.Label(win, text="new age:").grid(row=3, column=0, padx=10, pady=5)
    entry_age= ttk.Entry(win, width=30)
    entry_age.grid(row=3, column=2, padx=10, pady=5)

    ttk.Label(win, text="new contact_number:").grid(row=4, column=0, padx=10, pady=5)
    entry_num= ttk.Entry(win, width=30)
    entry_num.grid(row=4, column=2, padx=10, pady=5)

    def save_update():
        user_id = entry_userid.get().strip()
        new_name = entry_name.get().strip()
        new_email = entry_email.get().strip()
        new_age = entry_age.get().strip()
        new_number = entry_num.get().strip()

        cur.execute("UPDATE user SET name=%s, email=%s WHERE id=%s",
                    (new_name, new_email,new_age,new_number ,user_id))
        conn.commit()
        win.destroy()

    ttk.Button(win, text="Save Update", command=save_update).grid(row=3, column=1, pady=10)






btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
#tk.Button(btn_frame, text="Show News", width=20, command=show_news).grid(row=0, column=0, padx=10)
#tk.Button(btn_frame, text="Show Users", width=20, command=show_users).grid(row=0, column=1, padx=10)

user_label = tk.Label(root, text="FOR USER", font=("Arial", 16, "bold"))
user_label.pack(pady=10)
tk.Button(btn_frame, text="add user ", width=30, bg="black", fg="white", command=add_users).pack(pady=3)
ttk.Button(btn_frame, text=" view user", width=30, command=show_users).pack(pady=3)
ttk.Button(btn_frame, text=" delete user", width=30, command=delete_user).pack(pady=3)
ttk.Button(btn_frame, text=" update user", width=30, command=update_user).pack(pady=3)

t_label = tk.Label(root, text="FOR NEWS", font=("Arial", 16, "bold")).pack(pady=10)
tk.Button(btn_frame, text="add news ", width=30, bg="black", fg="white", command=add_news).pack(pady=3)
ttk.Button(btn_frame, text=" view news", width=30, command=show_news).pack(pady=3)
ttk.Button(btn_frame, text=" delete news", width=30, command=delete_news).pack(pady=3)
ttk.Button(btn_frame, text=" update news", width=30, command=update_news).pack(pady=3)

root.mainloop()


conn.close()
"""my question is ,should i have to view details all or the specific one searched by id"""