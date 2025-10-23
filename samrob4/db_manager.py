import sqlite3

class DBManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, create_table_sql):
        self.cursor.execute(create_table_sql)
        self.conn.commit()

    def insert_data(self, table, columns, values):
        cols = ', '.join(columns)
        placeholders = ', '.join(['?' for _ in values])
        sql = f"INSERT INTO {table} ({cols}) VALUES ({placeholders})"
        self.cursor.execute(sql, values)
        self.conn.commit()

    def update_data(self, table, set_columns, values, condition):
        set_expr = ', '.join([f"{col}=?" for col in set_columns])
        sql = f"UPDATE {table} SET {set_expr} WHERE {condition}"
        self.cursor.execute(sql, values)
        self.conn.commit()

    def delete_data(self, table, condition):
        sql = f"DELETE FROM {table} WHERE {condition}"
        self.cursor.execute(sql)
        self.conn.commit()

    def fetch_all(self, table):
        sql = f"SELECT * FROM {table}"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
