import sqlite3
from pathlib import Path
from pprint import pprint


class Database:
    def __init__(self) -> None:
        db_path = Path(__file__).parent.parent / 'batabase.sqlite'
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()

    def drop_tables(self):
        self.cursor.execute("DROP TABLE IF EXISTS product")
        self.db.commit()

    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS product (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price INTEGER,
                picture TEXT
                )
            """
        )
        self.db.commit()

    def populate_tables(self):
        self.cursor.execute(
            """
            INSERT INTO product (name, price, picture)
                VALUES 
                ('Аниме 1', 9.99, 'https://static.anixart.tv/posters/1jfv1ltf3Mz52dkymwqyY9zCa51AEQ.jpg'),
                ('Аниме 2', 19.99, 'https://example.com/picture2.jpg'),
                ('Аниме 3', 29.99, 'https://example.com/picture3.jpg'),
                ('Аниме 4', 39.99, 'https://example.com/picture4.jpg'),
                ('Аниме 5', 49.99, 'https://example.com/picture5.jpg'),
                ('Аниме 6', 59.99, 'https://example.com/picture6.jpg'),
                ('Аниме 7', 69.99, 'https://example.com/picture7.jpg'),
                ('Аниме 8', 79.99, 'https://example.com/picture8.jpg'),
                ('Аниме 9', 89.99, 'https://example.com/picture9.jpg')
            """
        )
        self.db.commit()

    def get_all_product(self):
        self.cursor.execute("SELECT name, price FROM product")
        return self.cursor.fetchall()


if __name__ == '__main__':
    db = Database()
    db.drop_tables()
    db.create_table()
    db.populate_tables()
    pprint(db.get_all_product())