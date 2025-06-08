import mysql.connector as mysql_conn
from getpass import getpass


def get_connection():
    host = input("Enter your MySQL host name (e.g., localhost): ").strip()
    user = input("Enter your MySQL Username: ").strip()
    password = getpass("Enter MySQL password: ").strip()
    print("Password entered securely.")

    conn = mysql_conn.connect(
        host=host,
        user=user,
        password=password
    )

    if conn.is_connected():
        print("Successfully connected to MySQL")
        return conn
    else:
        raise Exception("Failed to connect to MySQL")


def show_databases(cursor):
    cursor.execute("SHOW DATABASES;")
    dbs = cursor.fetchall()
    print("All existing databases:\n", dbs)


def use_or_create_database(cursor):
    db_name = input("Enter the name of the database you want to create or use: ").strip()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`;")
    cursor.execute(f"USE `{db_name}`;")
    print(f"Using database: {db_name}")
    return db_name


def show_tables(cursor):
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    print("All existing tables:\n", tables)


def create_table(cursor):
    table_name = input("Enter the name of the table you want to create: ").strip()
    col_defs = input("Enter column definitions (e.g., emp_id VARCHAR(10), emp_name VARCHAR(50)): ").strip()

    cursor.execute(f"CREATE TABLE IF NOT EXISTS `{table_name}` ({col_defs});")
    print(f"Table `{table_name}` created with columns: {col_defs}")
    return table_name


def insert_data(cursor, table_name):
    cursor.execute(f"DESCRIBE `{table_name}`;")
    columns = [col[0] for col in cursor.fetchall()]
    print(f"ℹTable columns: {columns}")

    values_input = input(f"Enter comma-separated values for {columns}: ")
    values = [v.strip() for v in values_input.split(',')]
    values_str = "', '".join(values)

    query = f"INSERT INTO `{table_name}` ({', '.join(columns)}) VALUES ('{values_str}');"
    cursor.execute(query)
    print("Values inserted successfully.")

import mysql.connector as mysql_conn

def update_data(cursor, table_name):
    """
    Updates rows in the specified table based on user input for columns, values, and condition.
    """
    try:
        columns = input("Enter column names to update (comma-separated): ").strip().split(",")
        values = input("Enter corresponding values (comma-separated): ").strip().split(",")
        condition = input("Enter the WHERE condition (e.g., id=1): ").strip()

        if len(columns) != len(values):
            raise ValueError("The number of columns and values must match.")

        set_clause = ", ".join([f"{col.strip()} = %s" for col in columns])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition};"
        cursor.execute(query, [val.strip() for val in values])

        print("Update successful.")
        
    except mysql_conn.Error as err:
        raise Exception(f"MySQL Error during update: {err}")
    except Exception as e:
        raise Exception(f"Unexpected error during update: {e}")


def alter_data(cursor, table_name):
    """
    Alters the structure of the specified table based on user input for operation and column details.
    """
    try:
        operation = input("Enter the ALTER operation (ADD/DROP COLUMN/MODIFY COLUMN): ").strip().upper()
        column_def = input("Enter the column name and datatype (e.g., age INT): ").strip()

        query = f"ALTER TABLE {table_name} {operation} {column_def};"
        cursor.execute(query)

        print("Table altered successfully.")

    except mysql_conn.Error as err:
        raise Exception(f"MySQL Error during alter: {err}")
    except Exception as e:
        raise Exception(f"Unexpected error during alter: {e}")


def delete_data(cursor, table_name):
    """
    Deletes rows from the specified table based on a condition provided by the user.
    """
    try:
        condition = input("Enter the WHERE condition for deletion (e.g., id=5): ").strip()

        query = f"DELETE FROM {table_name} WHERE {condition};"
        cursor.execute(query)

        print("Deletion successful.")

    except mysql_conn.Error as err:
        raise Exception(f"MySQL Error during delete: {err}")
    except Exception as e:
        raise Exception(f"Unexpected error during delete: {e}")



def execute_custom_query(cursor):
    query = input("Enter your SQL query (SELECT/UPDATE/DELETE/ALTER...): ").strip()
    cursor.execute(query)
    try:
        result = cursor.fetchall()
        print("Query Output:\n", result)
    except mysql_conn.errors.InterfaceError:
        print("Query executed successfully (no result to fetch).")


def main():
    conn = get_connection()
    cursor = conn.cursor()

    show_databases(cursor)
    use_or_create_database(cursor)
    show_tables(cursor)

    while True:
        print("\nChoose an option:")
        print("1. Create a table")
        print("2. Insert data")
        print("3. Execute custom SQL query")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            create_table(cursor)
        elif choice == '2':
            table_name = input("Enter the table name you want to insert data into: ").strip()
            insert_data(cursor, table_name)
        elif choice == '3':
            execute_custom_query(cursor)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

        conn.commit()

    cursor.close()
    conn.close()
    print("MySQL connection closed.")


if __name__ == "__main__":
    main()
