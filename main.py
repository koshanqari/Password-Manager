from tkinter import *
from PIL import ImageTk, Image
import random
import pandas
import os
#constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
BACKGROUND_COLOR = "White"

#All the functions fxns go in here
def gen_pass():
    '''Generates 10 character password and puts up on the {password_e} entry'''
    print("FXN password Generator")

    password = ""
    for i in range(10):
        password += chr(random.randint(33, 126))
    password_e.delete(0, END)
    password_e.insert(0, password)




def show_pass():
    '''shows the saved data'''
    os.system('cls')
    print("FXN password shower")
    df = pandas.read_csv("data\data.csv")
    print(df)


def save_data():
    '''saves the data on the entry fields'''
    print("FXN data saver")
    dic = {
        "Website" : [website_v.get()],
        "User Id" : [userid_v.get()],
        "Password": [password_v.get()]
    }
    print(dic)
    df = pandas.DataFrame(dic)
    print(df)

    df.to_csv("data\data.csv", mode="a", header=False, index=False)
    print(df)


def update(index):
    print(type(index))
    df = pandas.read_csv("data\data.csv")
    df.at[index, 'Website'] = website_v.get()
    df.at[index, "User Id"] = userid_v.get()
    df.at[index, "Password"] = password_v.get()

    print(df)


def update_option():
    '''opens up the update option'''
    print("data updating")
    update_l = Label(text="Serial no.")
    update_l.place(x=10, y=200)
    update_v = IntVar(root)
    update_e = Entry(root, text="Name: ", textvariable=update_v)
    update_e.place(x=70, y=200)
    
    save_data_b.config(text="SAVE UPDATE", command=lambda: update(update_v.get()))

    



#setting up main window 
root = Tk()
root.minsize(SCREEN_WIDTH, SCREEN_HEIGHT)
root.maxsize(SCREEN_WIDTH, SCREEN_HEIGHT)
root.config(background=BACKGROUND_COLOR)
root.title("K.Qaris Password Manager")
root.iconbitmap('pics\icon.ico')


#GUI ------------------------------------------------------------------


#/resizing and setting an image-----------

# # Read the Image
image = Image.open("pics\logo2.png")
# Resize the image using resize() method
resize_image = image.resize((100, 100))
img = ImageTk.PhotoImage(resize_image)
# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.pack()

#----------------------------------------


#creating labels and inputs--------------
#website
website_l = Label(text="Website")
website_v = StringVar(root)
website_e = Entry(root, text="Name: ", textvariable=website_v)
website_l.place(x=10, y=250)
website_e.place(x=70, y=250)
#userid
userid_l = Label(text="User Id")
userid_v = StringVar(root)
userid_e = Entry(root, text="Name: ", textvariable=userid_v)
userid_l.place(x=10, y=300)
userid_e.place(x=70, y=300)
#password
password_l = Label(text="Password")
password_v = StringVar(root)
password_e = Entry(root, text="Name: ", textvariable=password_v)
password_l.place(x=10, y=350)
password_e.place(x=70, y=350)

#generate password 
password_b = Button(text="Generate Password", command=gen_pass)
password_b.place(x=170, y=350)

#show password
show_pass_b = Button(text="Show Saved Pass", command=show_pass)
show_pass_b.pack()

#update data
update_data_b = Button(text="update data", command=update_option)
update_data_b.pack()

#save data
save_data_b = Button(text="Save", command=save_data)
save_data_b.place(x=250, y=400)



#GUI--------------------------------------------------------------------



#App loop
root.mainloop()
