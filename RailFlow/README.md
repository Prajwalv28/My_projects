
# 🚆 RailFlow: Intelligent Railway Reservation & Ticket Management System

**RailFlow** is a Python and SQLite-powered Railway Reservation System that simulates real-world train ticketing operations with a user-friendly GUI. This project demonstrates SQL query handling, age-based passenger segmentation, and smart waitlist management — all integrated into an intuitive desktop app using Tkinter.

---

## Features

- 🔍 Passenger train booking lookup
- 📅 Date-based passenger retrieval
- 🧓 Age range-based filtering with train insights
- 🚆 Train-wise passenger count reports
- 🧾 Train-specific ticket summary
- ❌ Smart ticket cancellation with automated waitlist confirmation

---

## 🛠️ Tech Stack

- **Python 3**
- **SQLite3**
- **Tkinter (GUI)**
- SQL Joins, Filters, Grouping, and Dynamic Querying

---

## 💻 How to Run

```bash
# 1. Download only the RailFlow folder from GitHub using svn
svn export https://github.com/<Prajwalv28>/My_projects/trunk/RailFlow

# 2. Navigate into the downloaded folder
cd RailFlow

# 3. Ensure required CSVs exist in the RRS/ folder:
#    - booked1.csv
#    - Passenger1.csv
#    - Train_status.csv
#    - Train.csv

# 4. Run the application
python CODE.py

```

Make sure `RRS.db`, `RRS.sql`, and the `RRS/` folder with CSV files are present in the same directory.

---

## SQL Query Examples

- Find trains booked by a passenger:
```sql
SELECT p.first_Name, p.last_Name, T.TrainNumber, T.TrainName
FROM Booked b
JOIN Passenger p ON b.Passenger_SSN = p.SSN
JOIN Train t ON b.Train_Number = t.TrainNumber
WHERE p.first_name = 'Art' AND p.last_name = 'Venere';
```

- Show passengers traveling on a given date:
```sql
SELECT p.first_Name, p.last_Name
FROM Passenger p
JOIN Booked b ON b.Passenger_SSN = p.SSN
JOIN Train t ON t.TrainNumber = b.Train_Number
JOIN TrainStatus ts ON ts.TrainName = t.TrainName
WHERE b.status = 'Booked' AND DATE(ts.TrainDate) = '2022-02-20';
```

---

## 📸 Snaps

![image](https://github.com/user-attachments/assets/eee06f56-89f7-47f5-bde5-8c77bdb08c11)
![image](https://github.com/user-attachments/assets/370ae856-17d0-4d8b-956d-516108ad8796)
![image](https://github.com/user-attachments/assets/1ea51c43-f973-4780-80e9-f17998b108bf)
![image](https://github.com/user-attachments/assets/d66580cd-f591-46db-b1ae-9e73c89e3947)
![image](https://github.com/user-attachments/assets/77364d6a-eab5-4455-9b41-8695f1635ca2)

---

## UI Screens

- Built-in Tkinter GUI displays user input boxes for query execution
- Real-time result windows
- Supports direct DB interaction

---

## 🧑‍💻 Author

**Prajwal Venkat Venkatesh**  
📧 prajwalvenkatv@gmail.com  
🌐 [LinkedIn](https://www.linkedin.com/in/prajwal-venkat-v-9654a5180)
