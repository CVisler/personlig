from dataclasses import dataclass
from pathlib import Path
import sqlite3
path_db = Path('tester.db')

import pandas as pd
import plotly.express as px

mock_df = px.data.iris()
headers = mock_df.columns.tolist()


# Create some mock data with columns name, age and address
mock_data = {
    'name': ['Otto Visler', 'John Doe', 'Jane Doe'],
    'age': [1, 2, 3],
    'address': ['Aggeren', 'Somewhere', 'Somewhere else']
}


@dataclass
class UserDB:
    conn: sqlite3.Connection = sqlite3.connect(path_db)


    def create_table(self):
        self.conn.execute(
            """CREATE TABLE IF NOT EXISTS user (name TEXT, age INTEGER, address TEXT)""")


    def create_iris(self):
        self.conn.execute(
            """CREATE TABLE IF NOT EXISTS iris (sepal_length INTEGER, sepal_width INTEGER, petal_length INTEGER, petal_width INTEGER, species TEXT, species_id INTEGER)""")


    def insert(self, name, age, address):
        insertion = ("""INSERT INTO user (name, age, address) VALUES (?, ?, ?)""", (name, age, address))


    def insert_iris(self):
        insertion = (
            """INSERT INTO iris (sepal_length,
            sepal_width,
            petal_length,
            petal_width,
            species,
            species_id) 
            VALUES (?, ?, ?, ?, ?, ?)""", 
            (mock_df.sepal_length, mock_df.sepal_width, mock_df.petal_length, mock_df.petal_width, mock_df.species, mock_df.species_id))
        self.conn.execute(insertion)


    def insert_iris_pd(self):
        mock_df.to_sql('iris', self.conn, if_exists='append', index=False, method=None)


@dataclass
class User(UserDB):
    name: str = "Otto Visler"
    age: int = 1
    address: str = "Aggeren"


def main():
    user = User()
    user.create_iris()
    user.insert_iris_pd()


if __name__ == '__main__':
    main()
