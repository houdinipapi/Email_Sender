from tkinter import *
import smtplib

# Main Screen
master = Tk()
master.title('Email App')

# Graphics

# --- Oth Row --- #
# Label(master, text="Custom Email App", font=('Calibri', 15)).grid(row=0, sticky=N)
top_label = Label(master, text="Custom Python Email app", font=('Calibri', 15))
top_label.grid(row=0, sticky=N)
# --- 1st Row --- #
instruct_label = Label(master, text="Fill in the form below to send an email", font=('Calibri', 11))
instruct_label.grid(row=1, sticky=W, padx=5)

# Input Fields

# --- Sender --- #

top_label = Label(master, text="Custom Python Email app", font=('Calibri', 15))
top_label.grid(row=0, sticky=N)

# --- Password --- #

top_label = Label(master, text="Custom Python Email app", font=('Calibri', 15))
top_label.grid(row=0, sticky=N)

# --- Recipient --- #

top_label = Label(master, text="Custom Python Email app", font=('Calibri', 15))
top_label.grid(row=0, sticky=N)

# --- Subject --- #

top_label = Label(master, text="Custom Python Email app", font=('Calibri', 15))
top_label.grid(row=0, sticky=N)

master.mainloop()
