# Helper functions and classes to run part 1.

import sqlite3
import numpy as np

def read_coordinates(file_path):
    """
    Function reads input from txt file and returns as an array of floats.
    """
    with open(file_path) as f:
        line = f.readline()
        arr = line.replace("[", "").replace("]", "").replace(" ", "").split(",")
    return [ float(x) for x in arr ]

class SqlMock():

    def __init__(self, connection=":memory:"):
        
        """
        SQL Mock db stored in Memory. 
        """
        self.conn = sqlite3.connect(connection)
        self.cur = self.conn.cursor()
    
    def create_table(self, table_name: str, columns: list):
        """
        Creates Table in SQL Mock db
        
        table_name: "something"
        columns: ["x", "y"]
        """
        self.cur.execute("""CREATE TABLE {} 
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
        self.cur.executemany(insert_query, records)

    def read_table(self, table_name: str):
        """
        Read all data from table
        """
        self.cur.execute("""SELECT * FROM {}""".format(table_name))
        return self.cur.fetchall()

    def run_mock(self, table_name: str, columns: list, values: list):
        """
        Run mock SQL to store coordinate data.
        """
        self.create_table(table_name, columns)
        self.insert_rows(table_name, columns, values)
        self.conn.commit()

    def close_conn(self):
        """
        Close the connection.
        """
        self.conn.close()

class PolynomialSolver():

    def __init__(self, coords: list, deg: int):
        """
        Solves polynomial of given degree and coordinates
        Gives output in dictionary format.
        {
            "x": list,
            "y": list,
            "deg": int
            "coefficients": list,
            "roots": list,
        }
        
        Attributes:
                    coords: list of coords as tuples, e.g. 
                            [(x0, y0), (x1, y1), ..]
                    deg:    order of polynomial. integer."""
        self.deg = deg
        self.x = np.array(coords)[:,0]
        self.y = np.array(coords)[:,1]

    def fit_polynomial(self):
        """
        Fits x and y coordinates to a polynomial of deg
        coords are a list of tuples
        """
        coefficients = np.polyfit(self.x, self.y, deg=self.deg)
        return coefficients

    def get_roots(self, coefficients):
        """
        solves polynomial numerically for 0.
        e.g. 
        p[0] * x**n + p[1] * x**(n-1) + ... + p[n-1]*x + p[n]
        where p is the coefficients and n is the deg of polynomial
        """
        roots = np.roots(coefficients)
        return [np.real(x) for x in roots ]
    
    def solve_polynomial(self):
        """
        Solves polynomial from coordinates
        Returns information on the function.
        """
        coefficients = self.fit_polynomial()
        roots = self.get_roots(coefficients)
        return {
            "x": list(self.x),
            "y": list(self.y),
            "deg": self.deg,
            "coefficients": list(coefficients),
            "roots": list(roots)
        }



