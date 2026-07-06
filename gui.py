from tkinter import *
from tkinter import ttk
import csv

from database import (
    add_expense,
    get_expenses,
    delete_expense,
    get_total_expenses,
    search_expenses,
    update_expense,
    get_category_summary
)

import matplotlib.pyplot as plt

selected_id = None

root = Tk()

root.title("Expense Tracker")
root.geometry("900x500")

total_label = Label(
    root,
    text="Total Expenses: ₹0.00",
    font=("Segoe UI", 14, "bold")
)

total_label.grid(
    row=6,
    column=0,
    columnspan=3,
    pady=10
)

def refresh_table():

    for row in tree.get_children():
        tree.delete(row)

    expenses = get_expenses()

    for expense in expenses:
        tree.insert("", END, values=expense)

    total = get_total_expenses()

    total_label.config(
        text=f"Total Expenses: ₹{total:.2f}"
    )

def save_expense():

    add_expense(
        date_entry.get(),
        category_entry.get(),
        amount_entry.get(),
        desc_entry.get()
    )

    refresh_table()

def remove_expense():

    selected_item = tree.focus()

    if not selected_item:
        return

    values = tree.item(selected_item, "values")

    expense_id = values[0]

    delete_expense(expense_id)

    refresh_table()

    date_entry.delete(0, END)
    category_entry.delete(0, END)
    amount_entry.delete(0, END)
    desc_entry.delete(0, END)

def search_data():
    category = search_entry.get()

    print("Searching for:", category)

    results = search_expenses(category)

    print("Results:", results)

    for row in tree.get_children():
        tree.delete(row)

    for expense in results:
        tree.insert("", END, values=expense)

def load_selected():

    global selected_id

    selected_item = tree.focus()

    if not selected_item:
        return

    values = tree.item(selected_item, "values")

    selected_id = values[0]

    date_entry.delete(0, END)
    category_entry.delete(0, END)
    amount_entry.delete(0, END)
    desc_entry.delete(0, END)

    date_entry.insert(0, values[1])
    category_entry.insert(0, values[2])
    amount_entry.insert(0, values[3])
    desc_entry.insert(0, values[4])

def edit_expense():

    global selected_id

    if selected_id is None:
        return

    update_expense(
        selected_id,
        date_entry.get(),
        category_entry.get(),
        amount_entry.get(),
        desc_entry.get()
    )

    refresh_table()

    selected_id = None

def export_csv():

    expenses = get_expenses()

    with open(
        "expenses.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            ["ID", "Date", "Category", "Amount", "Description"]
        )

        writer.writerows(expenses)

    print("CSV Exported Successfully")

def show_chart():

    data = get_category_summary()

    categories = []
    amounts = []

    for row in data:
        categories.append(row[0])
        amounts.append(float(row[1]))

    plt.figure(figsize=(6, 6))

    plt.pie(
        amounts,
        labels=categories,
        autopct="%1.1f%%"
    )

    plt.title("Expenses By Category")

    plt.show()

Button(
    root,
    text="Export to CSV",
    command=export_csv
).grid(row=4, column=5, padx=10)

Label(root, text="Search Category").grid(
    row=0,
    column=3,
    padx=10
)

search_entry = Entry(root)

search_entry.grid(
    row=0,
    column=4,
    padx=10
)

Label(root, text="Date (YYYY-MM-DD)").grid(row=0, column=0, padx=10, pady=10)

date_entry = Entry(root)
date_entry.grid(row=0, column=1)

Label(root, text="Category").grid(row=1, column=0)

category_entry = Entry(root)
category_entry.grid(row=1, column=1)

Label(root, text="Amount").grid(row=2, column=0)

amount_entry = Entry(root)
amount_entry.grid(row=2, column=1)

Label(root, text="Description").grid(row=3, column=0)

desc_entry = Entry(root)
desc_entry.grid(row=3, column=1)

Button(
    root,
    text="Add Expense",
    command=save_expense
).grid(row=4, column=1, pady=10)

Button(
    root,
    text="Delete Selected",
    command=remove_expense
).grid(row=4, column=2, padx=10)

Button(
    root,
    text="Search",
    command=search_data
).grid(
    row=0,
    column=5,
    padx=10
)

Button(
    root,
    text="Show All",
    command=refresh_table
).grid(
    row=1,
    column=5,
    padx=10
)

Button(
    root,
    text="Load Selected",
    command=load_selected
).grid(row=4, column=3, padx=10)

Button(
    root,
    text="Update Expense",
    command=edit_expense
).grid(row=4, column=4, padx=10)

Button(
    root,
    text="Export CSV",
    command=export_csv
).grid(row=6, column=4)

tree = ttk.Treeview(
    root,
    columns=("ID", "Date", "Category", "Amount", "Description"),
    show="headings"
)

Button(
    root,
    text="Pie Chart",
    command=show_chart
).grid(row=6, column=5, padx=10)

tree.heading("ID", text="ID")
tree.heading("Date", text="Date")
tree.heading("Category", text="Category")
tree.heading("Amount", text="Amount")
tree.heading("Description", text="Description")

tree.grid(
    row=5,
    column=0,
    columnspan=5,
    padx=10,
    pady=20
)

refresh_table()

root.mainloop()