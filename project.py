
from tkinter import *
import sqlite3
from tkinter import filedialog

import datetime

from PIL import Image, ImageTk


z=5.0


import sqlite3

# Connect to the SQLite database or create it if it doesn't exist
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Check if the 'databasc_table' table already exists in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='databasc_table';")
table_exists = cursor.fetchone()

if table_exists:
    # Table already exists, you can choose to drop it or skip the creation
    print("Table 'databasc_table' already exists.")
else:
    # Create the 'databasc_table' table with the necessary columns
    cursor.execute('''CREATE TABLE IF NOT EXISTS databasc_table
               (
               NAME TEXT NOT NULL,
               ADDRESS VARCHAR NOT NULL,
               PHONNUMBER INTEGER CHECK(length(PHONNUMBER) = 10) NOT NULL,
               பொருள்_NAME VARCHAR NOT NULL,  -- Changed column name to avoid duplicates
               பொருள்பெயர் VARCHAR NOT NULL,
               எண்ணிக்கை INTEGER NOT NULL,
               குறைகள் VARCHAR NOT NULL,
               பொருள்_எடை INTEGER NOT NULL,  -- Changed column name to avoid duplicates
               வட்டி INTEGER NOT NULL,
               அசல் INTEGER NOT NULL
               );''')





# Function to insert data into the 'STUDE_Information' table
def insert_data():
    name1 = entry1.get()
    name2 = entry2.get()
    name3 = entry3.get()
    global y
    # Get the selected gender from checkboxes
    name4 = y
    
    global z
    name5 = entry4.get()
    name6 = entry5.get()
    name7 = entry6.get()
    name8 = entry7.get()
    name9 = z
    name0 = entry8.get()
    
    try:
        with sqlite3.connect('data.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO databasc_table (NAME, ADDRESS, PHONNUMBER, பொருள்_NAME, பொருள்பெயர், எண்ணிக்கை, குறைகள், பொருள்_எடை, வட்டி, அசல்) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (name1, name2, name3, name4, name5, name6, name7, name8, name9, name0)
            )
            conn.commit()
        print(f"Inserted '{name1}', '{name2}', '{name3}', '{name4}', '{name5}', '{name6}', '{name7}', '{name8}', '{name9}', '{name0}'")
    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {e}")







        
win = Tk()


# Set the window's geometry (size)
win.geometry("1024x768")




# Open the image using Pillow
image = Image.open("C:/project/3.jpg")
photo_image = ImageTk.PhotoImage(image)



# Create a label widget to display the background image
background_label = Label(win, image=photo_image)
background_label.place(relwidth=1, relheight=1)






# Create labels for the text entry widgets
Label(win, text="Name:", font=('Helvetica 12'), anchor="w").grid(row=0, column=0, padx=10, pady=10)
Label(win, text="ADDRESS:", font=('Helvetica 12'), anchor="w").grid(row=1, column=0, padx=10, pady=10)
Label(win, text="PHONNUMBER:", font=('Helvetica 12'), anchor="w").grid(row=2, column=0, padx=10, pady=10)
Label(win, text="பொருள்:", font=('Helvetica 12'), anchor="w").grid(row=3, column=0, padx=10, pady=10)
Label(win, text="வட்டி:", font=('Helvetica 12'), anchor="w").grid(row=4, column=0, padx=10, pady=10)
Label(win, text="பொருள் பெயர்:", font=('Helvetica 12'), anchor="w").grid(row=5, column=0, padx=10, pady=10)
Label(win, text="எண்ணிக்கை:", font=('Helvetica 12'), anchor="w").grid(row=6, column=0, padx=10, pady=10)
Label(win, text="குறைகள்:", font=('Helvetica 12'), anchor="w").grid(row=7, column=0, padx=10, pady=10)
Label(win, text="பொருள் எடை:", font=('Helvetica 12'), anchor="w").grid(row=8, column=0, padx=10, pady=10)
Label(win, text="அசல்:", font=('Helvetica 12'), anchor="w").grid(row=9, column=0, padx=10, pady=10)




import tkinter as tk
from tkinter import Entry, Label  # Add this import








def the_h(event=None):  # Modified the_h function to accept an event
    num = entry7.get()
    try:
        tamp = int(num) * 4000  # Convert num to an integer
        label_result.config(text=tamp)  # Update label with the result
    except ValueError:
        label_result.config(text="Invalid input")

# Create a label widget for displaying the result
label_result = tk.Label(win, text="", font=('Helvetica 12'), anchor="w")
label_result.grid(row=8, column=3, padx=10, pady=10)








# Create five text entry widgets
entry1 = Entry(win, width=30, justify=LEFT, bg="white", font=('Times', 12))
entry2 = Entry(win, width=30, justify=LEFT, bg="white", font=('Times', 12))
entry3 = Entry(win, width=30, justify=LEFT, bg="white", font=('Times', 12))
entry4 = Entry(win, width=30, justify=LEFT, bg="white", font=('Times', 12))
entry5 = Entry(win, width=30, justify=LEFT, bg="white", font=('Times', 12))
entry6 = Entry(win, width=30, justify=LEFT, bg="white", font=('Times', 12))
entry7 = Entry(win, width=30, justify=LEFT, bg="white", font=('Times', 12))
entry8 = Entry(win, width=30, justify=LEFT, bg="white", font=('Times', 12))










entry1.grid(row=0, column=1, padx=10, pady=10)
entry2.grid(row=1, column=1, padx=10, pady=10)
entry3.grid(row=2, column=1, padx=10, pady=10)
entry4.grid(row=5, column=1, padx=10, pady=10)
entry5.grid(row=6, column=1, padx=10, pady=10)
entry6.grid(row=7, column=1, padx=5, pady=5)
entry7.grid(row=8, column=1, padx=10, pady=8)
entry8.grid(row=9, column=1, padx=10, pady=8)




# Bind the function to the <Return> key press event for the Entry widget
entry7.bind("<Return>", the_h)










import tkinter as tk

def update_y(selected):
    global y
    if selected == "1":
        y = "தங்கம்"
    elif selected == "2":
        y = "வெள்ளி"
    print(y)


# Initialize the global variable 'y'
y = "தங்கம்"

# Initialize the radio variable
radio_var = tk.StringVar()
radio_var.set("1")  # Set default value to "1"

# Create two radio buttons using grid
radio1 = tk.Radiobutton(win, text="தங்கம்", variable=radio_var, value="1", command=lambda: update_y(radio_var.get()))
radio1.grid(row=3, column=1)

radio2 = tk.Radiobutton(win, text="வெள்ளி", variable=radio_var, value="2", command=lambda: update_y(radio_var.get()))
radio2.grid(row=3, column=2)











import tkinter as tk

def update_z(selected_value):
    global z
    if selected_value == "2.5":
        z = 2.5
    elif selected_value == "2":
        z = 2
    elif selected_value == "1.5":
        z = 1.5
    else:
        z = 2.1
    print(f"Selected value: {selected_value}, z: {z}")


# Initialize the global variable 'z'
z = 2.5

# Initialize the radio variable
radio_var = tk.StringVar()
radio_var.set("2.5")

# Create three radio buttons using grid
radio3 = tk.Radiobutton(win, text="2.5", variable=radio_var, value="2.5", command=lambda: update_z(radio_var.get()))
radio3.grid(row=4, column=3)

radio4 = tk.Radiobutton(win, text="2", variable=radio_var, value="2", command=lambda: update_z(radio_var.get()))
radio4.grid(row=4, column=2)

radio5 = tk.Radiobutton(win, text="1.5", variable=radio_var, value="1.5", command=lambda: update_z(radio_var.get()))
radio5.grid(row=4, column=1)






import tkinter as tk
import datetime




# Function to update the time
def update_time():
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    timetoday.config(text=formatted_datetime)
    win.after(1000, update_time)  # Update time every second

# Create a label for displaying the date and time
timetoday = tk.Label(win, text="", font=('Helvetica 12'), anchor="w")
timetoday.grid(row=0, column=6, padx=10, pady=10)

# Start updating the time
update_time()

















# Create a button to insert data
insert_button1 = Button(win, text="Insert Data", command=insert_data)
insert_button1.grid(row=10, column=2, columnspan=2, padx=10, pady=10)






import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('data.db')

# Execute an SQL query to fetch the data
query = "SELECT * FROM databasc_table"
df = pd.read_sql_query(query, conn)

# Export the data to an Excel file
df.to_excel('databasc_table.xlsx', index=False)

# Close the database connection
conn.close()


import tkinter as tk
import subprocess


# Function to run the "cd" command in Command Prompt
def run_command():
    command = 'cd C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python311\\Aparajest'
    command1 ='databasc_table.xlsx'
    try:
        subprocess.run(command, shell=True, check=True)
        subprocess.run(command1, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {str(e)}")



# Create a button to run the command
command_button = tk.Button(win, text="Run Command Prompt", command=run_command)

command_button.grid(row=11, column=3, padx=10, pady=8)






# Start the Tkinter main loop
win.mainloop()









