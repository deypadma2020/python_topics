import mysql.connector as mysql_conn
from mysql.connector import Error
from getpass import getpass


class MySQLApp:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            host = input("Enter your MySQL host name (e.g., localhost): ").strip()
            user = input("Enter your MySQL Username: ").strip()
            password = getpass("Enter MySQL password: ").strip()
            print("Password entered securely.")

            self.conn = mysql_conn.connect(host=host, user=user, password=password)

            if self.conn.is_connected():
                print("Successfully connected to MySQL")
                self.cursor = self.conn.cursor()

        except Error as e:
            print(f"Connection failed: {e}")
            exit()

    def show_databases(self):
        try:
            self.cursor.execute("SHOW DATABASES;")
            databases = self.cursor.fetchall()
            print("Databases:")
            for db in databases:
                print(" -", db[0])
        except Error as e:
            print(f"Error fetching databases: {e}")

    def use_or_create_database(self):
        try:
            db_name = input("Enter the database name to use/create: ").strip()
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`;")
            self.cursor.execute(f"USE `{db_name}`;")
            print(f"Using database: {db_name}")
        except Error as e:
            print(f"Error using/creating database: {e}")

    def show_tables(self):
        try:
            self.cursor.execute("SHOW TABLES;")
            tables = self.cursor.fetchall()
            print("Tables:")
            for tbl in tables:
                print(" -", tbl[0])
        except Error as e:
            print(f"Error fetching tables: {e}")

    def create_table(self):
        try:
            table_name = input("Enter table name to create: ").strip()
            col_defs = input("Enter column definitions (e.g., emp_id VARCHAR(10), emp_name VARCHAR(50)): ").strip()
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS `{table_name}` ({col_defs});")
            print(f"Table `{table_name}` created.")
        except Error as e:
            print(f"Error creating table: {e}")

    def insert_data(self):
        try:
            table_name = input("Enter the table name to insert into: ").strip()
            self.cursor.execute(f"DESCRIBE `{table_name}`;")
            columns = [col[0] for col in self.cursor.fetchall()]
            print(f"ℹColumns: {columns}")

            values_input = input(f"Enter comma-separated values for {columns}: ").strip()
            values = [v.strip() for v in values_input.split(',')]
            if len(values) != len(columns):
                print("Number of values doesn't match number of columns.")
                return

            values_str = "', '".join(values)
            query = f"INSERT INTO `{table_name}` ({', '.join(columns)}) VALUES ('{values_str}');"
            self.cursor.execute(query)
            print("Data inserted successfully.")
        except Error as e:
            print(f"Error inserting data: {e}")

    def run_custom_query(self):
        try:
            query = input("Enter your SQL query: ").strip()
            self.cursor.execute(query)

            if query.strip().lower().startswith("select"):
                result = self.cursor.fetchall()
                print("Query result:")
                for row in result:
                    print(row)
            else:
                print("Query executed.")

        except Error as e:
            print(f"Query error: {e}")

    def menu(self):
        while True:
            print("\nChoose an option:")
            print("1. Show databases")
            print("2. Use/Create a database")
            print("3. Show tables")
            print("4. Create a table")
            print("5. Insert data")
            print("6. Run a custom query")
            print("7. Exit")

            choice = input("Enter your choice: ").strip()

            try:
                if choice == '1':
                    self.show_databases()
                elif choice == '2':
                    self.use_or_create_database()
                elif choice == '3':
                    self.show_tables()
                elif choice == '4':
                    self.create_table()
                elif choice == '5':
                    self.insert_data()
                elif choice == '6':
                    self.run_custom_query()
                elif choice == '7':
                    print("Exiting...")
                    break
                else:
                    print("Invalid option.")
                self.conn.commit()

            except Error as e:
                print(f"Error during operation: {e}")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("MySQL connection closed.")


def main():
    app = MySQLApp()
    try:
        app.connect()
        app.menu()
    finally:
        app.close()


if __name__ == "__main__":
    main()
