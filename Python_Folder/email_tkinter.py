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

# --- Email Sender --- #

sender_label = Label(master, text="From", font=('Calibri', 11))
sender_label.grid(row=2, sticky=W, padx=5)

# --- Email Password --- #

paswd_label = Label(master, text="Password", font=('Calibri', 11))
paswd_label.grid(row=3, sticky=W, padx=5)

# --- Email Recipient --- #

recipient_label = Label(master, text="To", font=('Calibri', 11))
recipient_label.grid(row=4, sticky=W, padx=5)

# --- Email Subject --- #

subject_label = Label(master, text="Subject", font=('Calibri', 11))
subject_label.grid(row=5, sticky=W, padx=5)

# --- Email Body --- #

body_label = Label(master, text="Body", font=('Calibri', 11))
body_label.grid(row=6, sticky=W, padx=5)

# --- Notification --- #
notif_label = Label(master, text="", font=('Calibri', 11))
notif_label.grid(row=7, sticky=S, padx=5)

# Storage

# --- Temporary Storage --- #
temp_username = StringVar()
temp_paswd = StringVar()
temp_recipient = StringVar()
temp_subject = StringVar()
temp_body = StringVar()

# Entries

# --- Username Entry --- #
usernameEntry = Entry(master, textvariable=temp_username)
usernameEntry.grid(row=2, column=0)

# --- Password Entry --- #
paswdEntry = Entry(master, textvariable=temp_paswd)
paswdEntry.grid(row=3, column=0)

# --- Recipient Entry --- #
recipientEntry = Entry(master, textvariable=temp_recipient)
recipientEntry.grid(row=4, column=0)

# --- Subject Entry
subjectEntry = Entry(master, textvariable=temp_subject)
subjectEntry.grid(row=5, column=0)

# --- Body Entry --- #
bodyEntry = Entry(master, textvariable=temp_body)
bodyEntry.grid(row=6, column=0)

master.mainloop()
