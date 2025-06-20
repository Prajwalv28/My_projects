#!/usr/bin/env python
# coding: utf-8

# In[8]:


import tkinter as tk
from tkinter import ttk
import sqlite3

# Function to retrieve trains booked by a passenger based on first and last names (Q1)
def retrieve_trains():
    conn = sqlite3.connect('RRS.db') 
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    query = f"""SELECT p.first_Name, p.last_Name, T.TrainNumber, T.TrainName
                FROM Booked b
                JOIN Passenger p ON b.Passenger_SSN = p.SSN
                JOIN Train t ON b.Train_Number = t.TrainNumber
                WHERE p.first_name = '{first_name}' AND p.last_name = '{last_name}'"""
    cursor = conn.execute(query)
    rows = cursor.fetchall()
    display_results(rows,("First Name", "Last Name", "Train Number", "Train Name"))
    conn.close()

# Function to retrieve passengers on a specific date with confirmed tickets (Q2)
def retrieve_passengers_on_date():
    conn = sqlite3.connect('RRS.db')  
    entered_date = entry_date.get()
    query = f"""SELECT p.first_Name, p.last_Name
                FROM Passenger p
                JOIN Booked b ON b.Passenger_SSN = p.SSN
                JOIN Train t ON t.TrainNumber = b.Train_Number
                JOIN TrainStatus ts ON ts.TrainName = t.TrainName
                WHERE b.status='Booked' AND DATE(ts.TrainDate)='{entered_date}'"""
    cursor = conn.execute(query)
    rows = cursor.fetchall()
    display_results(rows,("First Name", "Last Name"))
    conn.close()

# Function to retrieve passengers and train information based on age range input (Q3)
def retrieve_passengers_by_age():
    conn = sqlite3.connect('RRS.db')  
    input1 = int(entry_age1.get())
    input2 = int(entry_age2.get())
    query = f"""SELECT t.TrainNumber, t.TrainName, t.SourceStation, t.DestinationStation,
                p.first_name, p.last_name, p.address AS Address, b.Ticket_Type,
                b.status AS TicketStatus
                FROM passenger p
                JOIN booked b ON p.SSN = b.Passenger_ssn
                JOIN train t ON b.Train_Number = t.TrainNumber
                WHERE strftime('%Y', 'now') - strftime('%Y', p.bdate) BETWEEN {input1} AND {input2}"""
    cursor = conn.execute(query)
    rows = cursor.fetchall()
    display_results(rows,("Train Number", "Train Name","Source Station", "Destination Station",
                "First_name", "Last_name", "Address", "Ticket Type","status" ))
    conn.close()

# Function to retrieve all the train name along with count of passengers it is carrying.       
def trains_with_passenger_count():
    conn = sqlite3.connect('RRS.db')  
    query = """SELECT t.TrainName, COUNT(b.Passenger_SSN) AS PassengerCount
                FROM train t
                LEFT JOIN Booked b ON t.TrainNumber = b.Train_Number
                WHERE b.status='Booked'
                GROUP BY t.TrainName"""
    cursor = conn.execute(query)
    rows = cursor.fetchall()
    display_results(rows,("Train name", "Count"))
    conn.close()
    
# Function to retrieve all passengers with confirmed status traveling in a specific train (Q5)
def retrieve_passengers_in_train():
    conn = sqlite3.connect('RRS.db')  
    train_name = entry_train_name.get()
    query = f"""SELECT p.first_name, p.last_name, p.address, b.Ticket_Type
                FROM passenger p
                JOIN booked b ON p.SSN = b.Passenger_ssn
                JOIN train t ON b.Train_Number = t.TrainNumber
                WHERE t.TrainName = '{train_name}' AND b.status = 'Booked'"""
    cursor = conn.execute(query)
    rows = cursor.fetchall()
    display_results(rows, ("first_name","last_name", "address", "Ticket Type"))
    conn.close()
    
# Function to cancel a ticket and update passenger status from waiting list to confirmed (Q6)

def cancel_ticket_and_update_waiting_list():
    conn = sqlite3.connect('RRS.db')
    # Fetching train number for the cancelled ticket
    cancelled_ssn = int(entry_cancelled_ssn.get())
    select_cancelled_query = f""" SELECT Train_Number 
                                  FROM Booked 
                                  WHERE Passenger_ssn = {cancelled_ssn} AND Status = 'Booked'"""
    cursor = conn.execute(select_cancelled_query)
    cancelled_record = cursor.fetchone()
    cursor.close()
    # Checking if the cancelled ticket exists and getting details
    if cancelled_record:
        cancelled_record=cancelled_record[0]
        
        # Deleting the record of the cancelled ticket
        delete_query = f"DELETE FROM Booked WHERE Passenger_ssn = {cancelled_ssn}"
        conn.execute(delete_query)
        conn.commit()
        # Fetching the next passenger from the waiting list for the same train
        select_waiting_query = f"""SELECT * 
                                   FROM Booked 
                                   WHERE Status = 'WaitL' AND Train_Number = {cancelled_record} LIMIT 1"""
        cursor = conn.execute(select_waiting_query)
        waiting_record = cursor.fetchone()
        cursor.close()
        if waiting_record:
            # Updating the status of the passenger from waiting list to confirmed
            waiting_passenger_ssn = waiting_record[0]
            update_query = f"""UPDATE Booked 
                               SET Status = 'Booked' 
                               WHERE Passenger_ssn = {waiting_passenger_ssn}"""
            conn.execute(update_query)
            conn.commit()
            confirmation_label.config(text=f"Ticket canceled and waiting list passenger {waiting_passenger_ssn} for Train Number {cancelled_record} confirmed.")
        else:
            confirmation_label.config(text="Ticket canceled, but no waiting list passengers available.")
    else:
        confirmation_label.config(text="No booked ticket found with the provided details.")

    conn.commit()
    conn.close()
# Function to display query results 
def display_results(rows, headings):
    # Creating a new window to display query results
    result_window = tk.Toplevel(root)
    result_window.title("Query Results")
    
    # Creating a treeview widget
    tree = ttk.Treeview(result_window, columns=headings, show="headings")
    for i, heading in enumerate(headings):
        tree.heading(heading, text=heading)
   
    # Configuring heading colors
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading", background="black", foreground="white")
    tree.pack()

    if rows:
        for row in rows:
            tree.insert("", tk.END, values=row)
    else:
        tree.insert("", tk.END, values=("No results found",))
        
# GUI setup
root = tk.Tk()
root.title("Railway Reservation System")

# Widgets for Query 1 (Retrieve trains by passenger's first and last names)
label_q1 = tk.Label(root, text="1. Trains booked by Passenger's Names")
label_q1.pack()

label_first_name = tk.Label(root, text="Enter First Name:")
label_first_name.pack()
entry_first_name = tk.Entry(root)
entry_first_name.pack()

label_last_name = tk.Label(root, text="Enter Last Name:")
label_last_name.pack()
entry_last_name = tk.Entry(root)
entry_last_name.pack()

retrieve_trains_button = tk.Button(root, text="Retrieve Trains", command=retrieve_trains)
retrieve_trains_button.pack()
        
# Widgets for Query 2 (Retrieve passengers on a specific date with confirmed tickets)
label_q2 = tk.Label(root, text="2. Passengers Names on a Specific Date with Confirmed Tickets")
label_q2.pack()
label_date = tk.Label(root, text="Enter Date (YYYY-MM-DD):")
label_date.pack()
entry_date = tk.Entry(root)
entry_date.pack()

retrieve_passengers_on_date_button = tk.Button(root, text="Retrieve Passengers on Date", command=retrieve_passengers_on_date)
retrieve_passengers_on_date_button.pack()
        
# Widgets for Query 3 (Retrieve passengers and train information based on age range)
label_q3 = tk.Label(root, text="3. Passengers and Train Information by Age Range")
label_q3.pack()

label_age1 = tk.Label(root, text="Enter Age Range (From):")
label_age1.pack()
entry_age1 = tk.Entry(root)
entry_age1.pack()

label_age2 = tk.Label(root, text="Enter Age Range (To):")
label_age2.pack()
entry_age2 = tk.Entry(root)
entry_age2.pack()

retrieve_passengers_by_age_button = tk.Button(root, text="Retrieve Info", command=retrieve_passengers_by_age)
retrieve_passengers_by_age_button.pack()

# Widgets for Query 4 (List all train names with the count of passengers)
label_q4 = tk.Label(root, text="4. Train Names with Carrying Passenger Count")
label_q4.pack()
list_trains_button = tk.Button(root, text="Click", command=trains_with_passenger_count)
list_trains_button.pack()

# Widgets for Query 5 (Retrieve passengers with confirmed status traveling in a specific train)
label_q5 = tk.Label(root, text="5. Passengers with Confirmed Status in a Specific Train")
label_q5.pack()

label_train_name = tk.Label(root, text="Enter Train Name:")
label_train_name.pack()
entry_train_name = tk.Entry(root)
entry_train_name.pack()

retrieve_passengers_in_train_button = tk.Button(root, text="Retrieve Passengers", command=retrieve_passengers_in_train)
retrieve_passengers_in_train_button.pack()

# Widgets for Query 6 (Cancel ticket and update waiting list)
label_q6 = tk.Label(root, text="6: Cancel Ticket and Update Waiting List")
label_q6.pack()

label_cancelled_ssn = tk.Label(root, text="Enter SSN of Cancelled Ticket:")
label_cancelled_ssn.pack()
entry_cancelled_ssn = tk.Entry(root)
entry_cancelled_ssn.pack()

cancel_and_update_button = tk.Button(root, text="Cancel Ticket and Update Waiting List", command=cancel_ticket_and_update_waiting_list)
cancel_and_update_button.pack()

# Label for displaying confirmation
confirmation_label = tk.Label(root, text="")
confirmation_label.pack()

root.mainloop()


# In[ ]:





# In[ ]:




