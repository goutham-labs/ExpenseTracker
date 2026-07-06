# Expense Tracker

An Expense Tracker application built using **Python, Tkinter, and MySQL**.

## Features

- Add Expenses
- Delete Expenses
- Search Expenses
- View All Expenses
- Total Expense Calculation
- Export Expenses to CSV

## Requirements

Install the required package:

```bash
pip install mysql-connector-python
```

## Database Setup

Create a MySQL database named:

```sql
CREATE DATABASE expense_tracker;
```

Before running the application, open `database.py` and replace:

```python
password="YOUR_MYSQL_PASSWORD"
```

with your own MySQL password.

## Run

```bash
python gui.py
```

## Technologies Used

- Python
- Tkinter
- MySQL
- MySQL Connector