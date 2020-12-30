# the tkinter module has to be imported first so that we can make a GUI
from tkinter import*
import tkinter as tk
import tkinter.font as font
import sqlite3
from classes import

#I watched this tutorial youtube.com/watch?v=lcBoYduaUy0 to create most of this code
# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=10888s this video gave me an introduction to tkinter


#create the app screen
window=Tk()
window.geometry("375x600")
window.title("Corona Contacts")

# define font
site_font = font.Font(family='Helvetica', size=10, weight='bold')

'''style = Style()
# Will add style to every available button
# even though we are not passing style
# to every button widget.
style.configure('TButton', font=
('calibri', 10, 'bold', 'underline'),
                foreground='red')

With this structure I should be able to avoid entering the styling details for every button
but it doesn't work for me 
Source: https://www.geeksforgeeks.org/python-add-style-to-tkinter-button/'''

# put the site name on the top
site_name = Label(window, text="Corona Contacts", height=2)
site_name['font'] = site_font
site_name.pack()



#here is the part where the strings that were inputted are being compared with the one in the customer and restaurant dataabse
def log_in():
    print("")




#define command=sign_up
def sign_up():
    #define command=customer
    def customer():

        #define command=signup_database
        def signup_database():
            conn=sqlite3.connect("customer.db")
            cur=conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY, name text, password text, number text, mail text)")
            cur.execute("INSERT INTO test Values(Null, ?,?,?,?)", (nameE.get(), passwordE.get(), numberE.get(), mailE.get ()))
            l4 = Label(customer_window, text="Account Created").pack()
            conn.commit()
            conn.close()



        signup_window.destroy()
        customer_window = Tk()
        customer_window.geometry("375x600")
        customer_window.title("Customer - Sign Up")

        #Customer's Name
        nameL = Label(customer_window, text="User Name:").pack()
        name_text=StringVar()
        nameE= Entry (customer_window, textvariable=name_text)
        nameE.pack()

        #Customer's Password
        passwordL = Label(customer_window, text="Password:").pack()
        password_text = StringVar()
        passwordE = Entry(customer_window, textvariable=password_text)
        passwordE.pack()

        #Customer's Number
        numberL = Label(customer_window, text="Mobile Number:").pack()
        number_text = StringVar
        numberE = Entry(customer_window, textvariable=number_text)
        numberE.pack()

        # Customer's E-Mail
        mailL = Label(customer_window, text="E-Mail:").pack()
        mail_text = StringVar()
        mailE = Entry(customer_window, textvariable=mail_text)
        mailE.pack()


        #Confirm Sign Up button
        signup_confirm = Button(customer_window, width=10, activebackground="gray", text="Sign Up", command=signup_database).pack()




    # define command=restaurant
    def restaurant():

        # define command=restaurantSignup_database
        def restaurantSignup_database():
            conn = sqlite3.connect("restaurants.db")
            cur = conn.cursor()
            cur.execute(
                "CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY, name text, password text, number text, mail text, address text, capacity INTEGER)")
            cur.execute("INSERT INTO test Values(Null, ?,?,?,?,?,?)",
                        (nameE.get(), passwordE.get(), numberE.get(), mailE.get(), addressE.get(), capacityE.get()))
            l4 = Label(restaurant_window, text="Account Created").pack()
            conn.commit()
            conn.close()

        signup_window.destroy()
        restaurant_window = Tk()
        restaurant_window.geometry("375x600")
        restaurant_window.title("Restaurant - Sign Up")


        # Restaurant's Name
        nameL = Label(restaurant_window, text="User Name:").pack()
        name_text = StringVar()
        nameE = Entry(restaurant_window, textvariable=name_text)
        nameE.pack()

        # Restaurant's Password
        passwordL = Label(restaurant_window, text="Password:").pack()
        password_text = StringVar()
        passwordE = Entry(restaurant_window, textvariable=password_text)
        passwordE.pack()

        # Restaurant's Number
        numberL = Label(restaurant_window, text="Mobile Number:").pack()
        number_text = StringVar
        numberE = Entry(restaurant_window, textvariable=number_text)
        numberE.pack()

        # Restaurant's E-Mail
        mailL = Label(restaurant_window, text="E-Mail:").pack()
        mail_text = StringVar()
        mailE = Entry(restaurant_window, textvariable=mail_text)
        mailE.pack()

        # Restaurant's Address
        addressL = Label(restaurant_window, text="Address:").pack()
        address_text = StringVar()
        addressE = Entry(restaurant_window, textvariable=address_text)
        addressE.pack()

        # Restaurant's Max Capacity, I would use an IntVar() for this but somehow that doesn't work
        # so I am doing StringVar instead
        capacityL = Label(restaurant_window, text="Capacity:").pack()
        capacity_text = IntVar()
        capacityE = Entry(restaurant_window, textvariable=capacity_text)
        capacityE.pack()

        # I don't know how I should code this part but my idea was it that the Restaurant owner or employees
        # have to enter each table they have and how man seats each table has
        # Restaurant's Tables
        tabalesL = Label(restaurant_window, text="Table:").pack()

        # Restaurant's Seats
        seatsL = Label(restaurant_window, text="Seats:").pack()


        # Confirm Sign Up button
        signup_confirm = Button(restaurant_window, width=10, activebackground="gray", text="Sign Up",
                                command=restaurantSignup_database).pack()
    window.destroy()
    signup_window=Tk()
    signup_window.geometry("375x600")
    signup_window.title("Sign Up")

    # welcome text
    choose = Label(signup_window, text="Choose what kind of account you want to create", height=5, font="2").pack()
    customerB = Button(signup_window, width=20, activebackground="gray", text="Customer Account", command=customer)
    customerB.place(x=110, y=200)
    restaurantB = Button(signup_window, width=20, activebackground="gray", text="Restaurant Account", command=restaurant)
    restaurantB.place(x=110, y=270)


#welcome text
welcome = Label(window, text = "Welcome to Corona Contacts \n where we will protect your data", height=5, font="2").pack()

#log-in part
mailL = Label(window, text="E-Mail:").pack()
email_text=StringVar()
mailE = Entry(window, textvariable=email_text)
mailE.pack()


passwordL = Label(window, text="Password:").pack()
password_text=StringVar()
passwordE = Entry(window, textvariable=password_text)
passwordE.pack()


#creating log in button and configuring the style
log_in = Button (window, width = 10, activebackground = "gray", relief = FLAT, text = "Log In", command=log_in)
log_in.place(x=140, y=350)


#Forgot password - but it doesn't work for now
forgot = Label(window, text = "Forgot Password?")
forgot.place(x=135, y=380)

# creating sign up button and configuring the style
sign_up = Button(window, width = 10, activebackground = "gray", relief = FLAT, text = "Sign Up", command=sign_up)
sign_up.place(x=140, y=450)


window.mainloop()