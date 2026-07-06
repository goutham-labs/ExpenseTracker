import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD_HERE",
    database="expense_tracker"
)

cursor = conn.cursor()

def add_expense(date, category, amount, description):
    sql = """
    INSERT INTO expenses
    (expense_date, category, amount, description)
    VALUES (%s,%s,%s,%s)
    """

    cursor.execute(sql, (date, category, amount, description))
    conn.commit()

def get_expenses():
    cursor.execute("SELECT * FROM expenses")
    return cursor.fetchall()

def delete_expense(expense_id):
    sql = "DELETE FROM expenses WHERE id = %s"

    cursor.execute(sql, (expense_id,))
    conn.commit()

def get_total_expenses():
    cursor.execute(
        "SELECT IFNULL(SUM(amount), 0) FROM expenses"
    )

    return cursor.fetchone()[0]

def search_expenses(keyword):

    sql = """
    SELECT *
    FROM expenses
    WHERE category LIKE %s
       OR description LIKE %s
       OR expense_date LIKE %s
    """

    value = f"%{keyword}%"

    cursor.execute(
        sql,
        (value, value, value)
    )

    return cursor.fetchall()

def update_expense(expense_id, date, category, amount, description):

    sql = """
    UPDATE expenses
    SET expense_date=%s,
        category=%s,
        amount=%s,
        description=%s
    WHERE id=%s
    """

    cursor.execute(
        sql,
        (date, category, amount, description, expense_id)
    )

    conn.commit()

def get_category_summary():

    sql = """
    SELECT category, SUM(amount)
    FROM expenses
    GROUP BY category
    """

    cursor.execute(sql)

    return cursor.fetchall()    