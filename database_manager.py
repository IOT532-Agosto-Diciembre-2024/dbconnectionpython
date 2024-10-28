import mysql.connector
from mysql.connector import Error


class DatabaseManager:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='ecommerce_532',
                user='root',
                password='andrestorres'
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
        except Error as e:
            print(e)

    def disconnect(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()

    def insert_producto(self, name, description, price, weight):
        query = """INSERT INTO producto (nombre, descripcion, precio, peso) VALUES (%s,%s,%s,%s)"""
        values = (name, description,price, weight)
        self.cursor.execute(query, values)
        self.connection.commit()

    def list_products(self):
        query = "SELECT * FROM producto"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for row in result:
            print(row[1])
