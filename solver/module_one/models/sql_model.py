# SQL Data Mock for x, y coordinates
import sqlite3

class SqlMock():

    def __init__(self, connection=":memory:"):
        """
        SQL db stored in memory. Cached on start.
        """
        self.__conn = sqlite3.connect(connection)
        self.__cur = self.conn.cursor()
    
    def create_table(self, table_name:str, columns: list):
        """
        Creates Table in SQL Mock db

        table_name: "something"
        columns: ["x", "y"]
        """
        self.__cur.execute("""CREATE TABLE {}
             ({})""".format(table_name, ",".join(columns)))

    def insert_rows(self, table_name: str, columns: list, values: list):
        """
        Insert many rows into table. 

        table_name: "something"
        columns: ["x", "y"]
        values: [x, y] where x and y are arrays of values.
        """
        insert_query = ("""INSERT INTO {}
                    ({})
                    VALUES ({});""".format(table_name, ",".join(columns), ",".join(["?" for column in columns])))

        records = list(zip(*values))
        self.cur.__executemany(insert_query, records)

    def read_table(self, table_name: str):
        """
        Read all data from table
        """
        self.__cur.execute("""SELECT * FROM {}""".format(table_name))
        return self.__cur.fetchall()
    
    def run_mock(self, table_name: str, columns: list, values: list):
        """
        Run mock SQL to store coordinate data.
        """
        self.create_table(table_name, columns)
        self.insert_rows(table_name, columns, values)
        self.__conn.commit()

    def close_conn(self):
        """
        Close the connection.
        """
        self.__conn.close()
