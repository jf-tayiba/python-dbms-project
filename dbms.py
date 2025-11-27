import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox
import re


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="173212",
    database="testdb"
)
cur = conn.cursor()

root = tk.Tk()
root.title("News Feed Management System")
root.geometry("700x300")

tk.Label(root, text="📝 News Feed Management System", font=("Arial", 16, "bold")).pack(pady=20)

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_number(num):
    return num.isdigit()


def show_news_of_user(user_id,user_data):
    win = tk.Toplevel(root)
    win.transient(root)
    win.grab_set()

    win.title(f"News of User: {user_data[1]}")


    win.geometry("1000x700")
    


    search_frame = tk.Frame(win)
    search_frame.pack(pady=5)



    tk.Label(search_frame, text="Search Title:").pack(side=tk.LEFT)
    search_entry = tk.Entry(search_frame, width=30)
    search_entry.pack(side=tk.LEFT, padx=5)



    def search_news():
        keyword = "%" + search_entry.get().strip() + "%"
        tree.delete(*tree.get_children())  

        cur.execute("SELECT news_id, title, body, created_at FROM news WHERE title LIKE %s", (keyword,))
        rows = cur.fetchall()

        for r in rows:
            tree.insert("", tk.END, values=r)

    tk.Button(search_frame, text="Search", command=search_news).pack(side=tk.LEFT)
    tk.Button(search_frame, text="Clear", command=lambda: search_entry.delete(0, tk.END)).pack(side=tk.LEFT)





    tree = ttk.Treeview(win, columns=("news_id","title","body","created_at"), show="headings")
    tree.heading("news_id", text="")
    tree.column("news_id", width=0, stretch=False)
    tree.heading("title", text="Title")
    tree.heading("body", text="Body")
    tree.heading("created_at", text="Created At")
    tree.pack(fill=tk.BOTH, expand=True, pady=10)
    ttk.Button(win, text="◀️", command=win.destroy).pack(pady=10)


    btn_frame = tk.Frame(win)
    btn_frame.pack(pady=5)
    ttk.Button(btn_frame, text="📰➕Add News", command=lambda: add_news(user_id, tree)).pack(side=tk.LEFT, padx=5)
    ttk.Button(btn_frame, text="📰✏️Update News", command=lambda: update_news(tree)).pack(side=tk.LEFT, padx=5)
    ttk.Button(btn_frame, text="📰🗑️Delete News", command=lambda: delete_news(tree)).pack(side=tk.LEFT, padx=5)

    def news():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Select a news first!")
            return
        news_data = tree.item(selected_item[0], "values")
        news_id = news_data[0]

        for widget in win.winfo_children():
            if isinstance(widget, tk.Listbox):
                widget.destroy()



        list_box = tk.Listbox(win, width=80, height=20)
        list_box.pack(pady=10)
        list_box.delete(0, tk.END)

        cur.execute("SELECT * FROM news WHERE news_id=%s",(news_id,))
        rows = cur.fetchall()

        list_box.insert(tk.END, "---- NEWS ----")
        for r in rows:
            list_box.insert(tk.END, r[1])
            list_box.insert(tk.END, r[2])
            list_box.insert(tk.END, r[3])
    tk.Button(btn_frame, text="📰show_news", command=news).pack(side=tk.LEFT, padx=5)


    def load_news():
        tree.delete(*tree.get_children())
        cur.execute("SELECT news_id, title, body, created_at FROM news WHERE user_id=%s", (user_id,))
        for r in cur.fetchall():
            tree.insert("", tk.END, values=r)
    load_news()


def add_news(user_id, tree=None):
    win = tk.Toplevel(root)
    win.transient(root)
    win.grab_set()

    win.title("Add News")
    win.geometry("300x200")

    ttk.Label(win, text="Title:").grid(row=0, column=0, padx=10, pady=5)
    entry_title = ttk.Entry(win, width=30)
    entry_title.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(win, text="Body:").grid(row=1, column=0, padx=10, pady=5)
    entry_body = ttk.Entry(win, width=30)
    entry_body.grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(win, text="Date:").grid(row=2, column=0, padx=10, pady=5)
    entry_date = ttk.Entry(win, width=30)
    entry_date.grid(row=2, column=1, padx=10, pady=5)

    def save():
        title = entry_title.get().strip()
        body = entry_body.get().strip()
        date = entry_date.get().strip()
        if not title or not body or not date:
            messagebox.showerror("Error", "All fields are required!")
            return
        cur.execute("INSERT INTO news (user_id, title, body, created_at) VALUES (%s,%s,%s,%s)",
                    (user_id, title, body, date))
        conn.commit()
        win.destroy()
        if tree:
            tree.delete(*tree.get_children())
            cur.execute("SELECT news_id, title, body, created_at FROM news WHERE user_id=%s", (user_id,))
            for r in cur.fetchall():
                tree.insert("", tk.END, values=r)
    ttk.Button(win, text="Save", command=save).grid(row=3, column=1, pady=10)

def update_news(tree):
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Select a news to update!")
        return
    news_data = tree.item(selected[0], "values")
    news_id = news_data[0]

    win = tk.Toplevel(root)
    win.transient(root)
    win.grab_set()

    win.title("Update News")
    win.geometry("300x200")

    ttk.Label(win, text="Title:").grid(row=0, column=0, padx=10, pady=5)
    entry_title = ttk.Entry(win, width=30)
    entry_title.grid(row=0, column=1, padx=10, pady=5)
    entry_title.insert(0, news_data[1])

    ttk.Label(win, text="Body:").grid(row=1, column=0, padx=10, pady=5)
    entry_body = ttk.Entry(win, width=30)
    entry_body.grid(row=1, column=1, padx=10, pady=5)
    entry_body.insert(0, news_data[2])

    ttk.Label(win, text="Date:").grid(row=2, column=0, padx=10, pady=5)
    entry_date = ttk.Entry(win, width=30)
    entry_date.grid(row=2, column=1, padx=10, pady=5)
    entry_date.insert(0, news_data[3])

    def save():
        cur.execute("UPDATE news SET title=%s, body=%s, created_at=%s WHERE news_id=%s",
                    (entry_title.get(), entry_body.get(), entry_date.get(), news_id))
        conn.commit()
        win.destroy()
        tree.item(selected[0], values=(news_id, entry_title.get(), entry_body.get(), entry_date.get()))
    ttk.Button(win, text="Save Update", command=save).grid(row=3, column=1, pady=10)

def delete_news(tree):
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Select a news to delete!")
        return
    news_data = tree.item(selected[0], "values")
    news_id = news_data[0]
    if messagebox.askyesno("Delete News", f"Do you want to delete '{news_data[1]}'?"):
        cur.execute("DELETE FROM news WHERE news_id=%s", (news_id,))
        conn.commit()
        tree.delete(selected[0])
        messagebox.showinfo("Deleted", "News deleted successfully!")


def add_user(tree=None):
    win = tk.Toplevel(root)
    win.transient(root)
    win.grab_set()

    win.title("Add User")
    win.geometry("300x250")

    ttk.Label(win, text="Name:").grid(row=0, column=0, padx=10, pady=5)
    entry_name = ttk.Entry(win, width=30)
    entry_name.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(win, text="Email:").grid(row=1, column=0, padx=10, pady=5)
    entry_email = ttk.Entry(win, width=30)
    entry_email.grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(win, text="Age:").grid(row=2, column=0, padx=10, pady=5)
    entry_age = ttk.Entry(win, width=30)
    entry_age.grid(row=2, column=1, padx=10, pady=5)

    ttk.Label(win, text="Contact:").grid(row=3, column=0, padx=10, pady=5)
    entry_contact = ttk.Entry(win, width=30)
    entry_contact.grid(row=3, column=1, padx=10, pady=5)

    def save():
        name = entry_name.get().strip()
        email = entry_email.get().strip()
        age = entry_age.get().strip()
        contact = entry_contact.get().strip()

        if not name or not email or not age or not contact:
            messagebox.showerror("Error", "All fields are required!")
            return
        if not is_valid_email(email):
            messagebox.showerror("Error", "Invalid email!")
            return
        if not is_valid_number(age) or not is_valid_number(contact):
            messagebox.showerror("Error", "Age and Contact must be numbers!")
            return

        cur.execute("INSERT INTO user (name,email,age,contact_number) VALUES(%s,%s,%s,%s)",
                    (name,email,age,contact))
        conn.commit()
        win.destroy()
        if tree:
            refresh_users(tree)
    ttk.Button(win, text="Save", command=save).grid(row=4, column=1, pady=10)

def update_user(tree):
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Select a user to update!")
        return
    user_data = tree.item(selected[0], "values")
    user_id = user_data[0]

    win = tk.Toplevel(root)
    win.transient(root)
    win.grab_set()

    win.title("Update User")
    win.geometry("300x250")



    ttk.Label(win, text="Name:").grid(row=0, column=0, padx=10, pady=5)
    entry_name = ttk.Entry(win, width=30)
    entry_name.grid(row=0, column=1, padx=10, pady=5)
    entry_name.insert(0, user_data[1])

    ttk.Label(win, text="Email:").grid(row=1, column=0, padx=10, pady=5)
    entry_email = ttk.Entry(win, width=30)
    entry_email.grid(row=1, column=1, padx=10, pady=5)
    entry_email.insert(0, user_data[2])

    ttk.Label(win, text="Age:").grid(row=2, column=0, padx=10, pady=5)
    entry_age = ttk.Entry(win, width=30)
    entry_age.grid(row=2, column=1, padx=10, pady=5)
    entry_age.insert(0, user_data[3])

    ttk.Label(win, text="Contact:").grid(row=3, column=0, padx=10, pady=5)
    entry_contact = ttk.Entry(win, width=30)
    entry_contact.grid(row=3, column=1, padx=10, pady=5)
    entry_contact.insert(0, user_data[4])

    def save():
        cur.execute("UPDATE user SET name=%s,email=%s,age=%s,contact_number=%s WHERE user_id=%s",
                    (entry_name.get(), entry_email.get(), entry_age.get(), entry_contact.get(), user_id))
        conn.commit()
        win.destroy()
        refresh_users(tree)
    ttk.Button(win, text="Save Update", command=save).grid(row=4, column=1, pady=10)

def delete_user(tree):
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Select a user to delete!")
        return
    user_data = tree.item(selected[0], "values")
    user_id = user_data[0]
    if messagebox.askyesno("Delete User", f"Delete user '{user_data[1]}' and all their news?"):
        cur.execute("DELETE FROM news WHERE user_id=%s", (user_id,))
        cur.execute("DELETE FROM user WHERE user_id=%s", (user_id,))
        conn.commit()
        tree.delete(selected[0])
        messagebox.showinfo("Deleted", "User and their news deleted successfully!")


def refresh_users(tree):
    tree.delete(*tree.get_children())
    cur.execute("SELECT * FROM user")
    for r in cur.fetchall():
        tree.insert("", tk.END, values=r)


def show_users():
    win = tk.Toplevel(root)
    win.transient(root)
    win.grab_set()

    win.title("Users")
    win.geometry("700x400")
    


    search_frame = tk.Frame(win)
    search_frame.pack(pady=5)
    tk.Label(search_frame, text="Search Name:").pack(side=tk.LEFT)
    search_entry = tk.Entry(search_frame, width=30)
    search_entry.pack(side=tk.LEFT, padx=5)

    def search_user():
        keyword = "%" + search_entry.get().strip() + "%"
        tree.delete(*tree.get_children())
        cur.execute("SELECT * FROM user WHERE name LIKE %s", (keyword,))
        for r in cur.fetchall():
            tree.insert("", tk.END, values=r)
    tk.Button(search_frame, text="Search", command=search_user).pack(side=tk.LEFT, padx=5)
    tk.Button(search_frame, text="Clear", command=lambda: search_entry.delete(0, tk.END)).pack(side=tk.LEFT)

    tree = ttk.Treeview(win, columns=("user_id","name","email","age","contact_number"), show="headings")
    tree.heading("user_id", text="")
    tree.column("user_id", width=0, stretch=False)
    tree.heading("name", text="Name")
    tree.heading("email", text="Email")
    tree.heading("age", text="Age")
    tree.heading("contact_number", text="Contact")
    tree.pack(fill=tk.BOTH, expand=True, pady=10)
    ttk.Button(win, text="◀️", command=win.destroy).pack(pady=10)

    refresh_users(tree)

    btn_frame = tk.Frame(win)
    btn_frame.pack(pady=5)

    ttk.Button(btn_frame, text="➕ Add User", command=lambda: add_user(tree)).pack(side=tk.LEFT, padx=5)
    ttk.Button(btn_frame, text="✏️Update User", command=lambda: update_user(tree)).pack(side=tk.LEFT, padx=5)
    ttk.Button(btn_frame, text="🗑️Delete User", command=lambda: delete_user(tree)).pack(side=tk.LEFT, padx=5)


    def on_user_double_click(event):
        selected = tree.selection()
        if not selected:
            return
        user_data = tree.item(selected[0], "values")
        user_id = user_data[0] 
        if messagebox.askyesno("Choose Action", "Do you want to show this user's news?"):
            show_news_of_user(user_id,user_data)

    tree.bind("<Double-1>", on_user_double_click)

def view_all_news():
    win = tk.Toplevel(root)
    win.transient(root)
    win.grab_set()

    win.title("All News")
    win.geometry("1000x500")

    search_frame = tk.Frame(win)
    search_frame.pack(pady=5)



    tk.Label(search_frame, text="Search Title:").pack(side=tk.LEFT)
    search_entry = tk.Entry(search_frame, width=30)
    search_entry.pack(side=tk.LEFT, padx=5)



    def search_news():
        keyword = "%" + search_entry.get().strip() + "%"
        tree.delete(*tree.get_children())  

        cur.execute("SELECT news_id,user_id, title, body, created_at FROM news WHERE title LIKE %s", (keyword,))
        rows = cur.fetchall()

        for r in rows:
            tree.insert("", tk.END, values=r)

    tk.Button(search_frame, text="Search", command=search_news).pack(side=tk.LEFT)
    tk.Button(search_frame, text="Clear", command=lambda: search_entry.delete(0, tk.END)).pack(side=tk.LEFT)

    tree = ttk.Treeview(win,columns=("news_id","user_id","title","body","created_at"),show="headings")

    tree.heading("news_id", text="")
    tree.column("news_id", width=0, stretch=False)
    tree.heading("user_id", text="")
    tree.column("user_id", width=0, stretch=False)
    tree.heading("title", text="Title")
    tree.heading("body", text="Body")
    tree.heading("created_at", text="Created At")

    tree.pack(fill=tk.BOTH, expand=True, pady=10)

    cur.execute("SELECT news_id,user_id, title, body, created_at FROM news")
    for row in cur.fetchall():
        tree.insert("", tk.END, values=row)
    
    def on_user_double_click(event):
        selected = tree.selection()
        if not selected:
            return
        news_data = tree.item(selected[0], "values")
        news_id = news_data[0]
        
        for widget in win.winfo_children():
            if isinstance(widget, tk.Listbox):
                widget.destroy()

        list_box = tk.Listbox(win, width=80, height=20)
        list_box.pack(pady=10)
        list_box.delete(0, tk.END)
        cur.execute("SELECT news_id, title, body, created_at FROM news WHERE news_id=%s", (news_id,))
        rows = cur.fetchall()

        list_box.insert(tk.END, "---- NEWS ----")
        for r in rows:
            list_box.insert(tk.END, r[1])
            list_box.insert(tk.END, r[2])
            list_box.insert(tk.END, r[3])
    tree.bind("<Double-1>", on_user_double_click)



    ttk.Button(win, text="◀️ back", command=win.destroy).pack(pady=10)





btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)


ttk.Button(btn_frame, text="View Users 👥", width=30, command=show_users).pack(pady=5)
ttk.Button(btn_frame, text="View All News 📰", width=30, command=view_all_news).pack(pady=5)


root.mainloop()
conn.close()
