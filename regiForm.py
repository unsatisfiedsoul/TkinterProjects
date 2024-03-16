
import tkinter as tk
from tkinter import ttk
import mysql.connector as my
import bcrypt

def get_data():
    #global username
    #global password
    username = userEntry.get()
    password = passEntry.get()

    ps = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(ps,salt)

    mydb = my.connect(
            host = "localhost",
            user = "rony",
            password = "766900",
            database = "DCS"
            )
    query = "insert into users(username, password) values (%s,%s)"
    values = (username,hashed)
    cursor = mydb.cursor()
    cursor.execute(query,values)
    mydb.commit()

    cursor.close()
    mydb.close()

    main.destroy()


    

main = tk.Tk()
main.title("Registration Form")
main.geometry("400x300")

frame = ttk.Frame(main)
frame.pack()

userLabel = ttk.Label(frame,text="Username: ")
userLabel.grid(row=0,column=0)
userEntry = ttk.Entry(frame)
userEntry.grid(row=0,column=1)
passLabel = ttk.Label(frame,text="Password: ")
passLabel.grid(row=1,column=0)
passEntry = ttk.Entry(frame,show="*")
passEntry.grid(row=1,column=1)

loginButton = ttk.Button(frame,text="Login")
loginButton.grid(row=2,column=0)
regiButton = ttk.Button(frame, text="Registration",command=get_data)
regiButton.grid(row=2,column=1)


main.mainloop()


