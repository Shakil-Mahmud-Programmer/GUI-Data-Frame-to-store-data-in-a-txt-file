import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb

#Function
def Save_Info():
    FirstName_Info=FirstName.get()
    LastName_Info=LastName.get()
    email_info=email.get()
    password_info=password.get()
    birthday_info=birthday.get()
    UserID_Info=UserID.get()
    gender_info=gender.get()
    profession_info=profession.get()
    file=open("Info.txt","a")
    file.write("Name: ")
    file.write(FirstName_Info)
    file.write(" ")
    file.write(LastName_Info)
    file.write("\n")
    file.write("Email: ")
    file.write(email_info)
    file.write("\n")
    file.write("Password: ")
    file.write(password_info)
    file.write("\n")
    file.write("Date of birth: ")
    file.write(birthday_info)
    file.write("\n")
    file.write("User ID:")
    file.write(UserID_Info)
    file.write("\n")
    file.write("Gender: ")
    file.write(gender_info)
    file.write("\n")
    file.write("Profession: ")
    file.write(profession_info)
    file.write("\n \n \n")
    file.close()
    print("Information of",FirstName_Info,"has been register successfully !")
    mb.showinfo(title="Message",message='information has been saved !')


window=tk.Tk()
window.title("Data Form")
window.geometry("600x500")
window.iconbitmap("database.ico")
heading=tk.Label(text="Data Saving Form",bg="red",fg="white",font=("jost",20,"bold")).pack()

#First Name
First_Name=tk.Label(text="First Name:",fg="red",font=("jost",12,"bold")).place(x=50,y=100)
FirstName=tk.StringVar()
FirstName_Entry=tk.Entry(textvariable=FirstName).place(x=150,y=100)

#Last Name
Last_Name=tk.Label(text="Last Name:",fg="red",font=("jost",12,"bold")).place(x=300,y=100)
LastName=tk.StringVar()
LastName_Entry=tk.Entry(textvariable=LastName).place(x=400,y=100)

#Email
Email=tk.Label(text="Email:",fg="red",font=("jost",12,"bold")).place(x=50,y=150)
email=tk.StringVar()
email_entry=tk.Entry(textvariable=email).place(x=150,y=150)

#Password
Password=tk.Label(text="Password:",fg="red",font=("jost",12,"bold")).place(x=300,y=150)
password=tk.StringVar()
password_entry=tk.Entry(textvariable=password).place(x=400,y=150)

#Date of Birth
Birthday=tk.Label(text="Date of Birth:",fg="red",font=("jost",11,"bold")).place(x=50,y=200)
birthday=tk.StringVar()
birthday_entry=tk.Entry(textvariable=birthday).place(x=150,y=200)

#User ID
User_ID=tk.Label(text="User ID:",fg="red",font=("jost",12,"bold")).place(x=300,y=200)
UserID=tk.StringVar()
UserID_Entry=tk.Entry(textvariable=UserID).place(x=400,y=200)

#Gender
Gender=tk.Label(text="Gender:",fg="red",font=("jost",12,"bold")).place(x=50,y=250)
gender=tk.StringVar()
gender_entry=ttk.Combobox(textvariable=gender,values=["Male","Female","Other"],width=12).place(x=150,y=250)


#Profession
Profession=tk.Label(text="Profession:",fg="red",font=("jost",12,"bold")).place(x=300,y=250)
profession=tk.StringVar()
profession_entry=tk.Entry(textvariable=profession).place(x=400,y=250)


register=tk.Button(text="Register",bg="green",fg="White",font="Bold,200",height=1,width=8,command=Save_Info).place(x=250,y=300)
tk.mainloop()
