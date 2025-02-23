"""
module -- community.py
    
    Adds to and manages a dynamic set of volunteer 
        field data; intended to streamline sharing between 
        community actors and stakeholders involved in 
        local development initiatives which may benefit 
        from neighborhood tree data.
        
"""

from neighborhood import Neighborhood
from parcel import Parcel
from tree import Tree

import sqlite3

class Community:
    
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.create_tables()

    def create_tables(self):
        cursor = self.connection.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS neighborhoods (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                district TEXT NOT NULL
            )
        ''')
        # creating Neighborhood table

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS parcels (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                address TEXT NOT NULL,
                dist_id INTEGER,
                FOREIGN KEY (dist_id) REFERENCES neighborhoods (id)
            )
        ''')
        # creating Parcel table

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS trees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                status TEXT,
                species TEXT,
                maturation TEXT,
                health TEXT,
                last_seen TEXT,
                parcel_id INTEGER,
                FOREIGN KEY (parcel_id) REFERENCES parcels (id)
            )
        ''')
        # creating Tree table

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                affiliation TEXT NOT NULL,
                entry_date TEXT NOT NULL
            )
        ''')

        self.connection.commit()
    
    def add_user(self, user_name, affiliation):
        if user_name and affiliation:
            
            entry_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor = self.connection.cursor()
            cursor.execute('INSERT INTO users (name, affiliation, entry_date) VALUES (?, ?, ?)',
                           (user_name, affiliation, entry_date))
            self.connection.commit()

    def get_user_info(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT name, affiliation, entry_date FROM users ORDER BY entry_date DESC LIMIT 1')
        user_info = cursor.fetchone()
        return user_info

    def add_neighborhood(self, dist_id):
        
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO neighborhoods (id) VALUES (?)', (dist_id,))
        self.connection.commit()
        
        return dist_id
        

    def add_parcel(self, address, dist_id):
       
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO parcels (address, dist_id) VALUES (?, ?)', 
                       (address, dist_id)
                       )
        self.connection.commit()

    def add_tree(self, tree):
        cursor = self.connection.cursor()
        cursor.execute('SELECT id FROM parcels WHERE address=? AND dist_id=?', 
                       (tree.address, tree.dist_id)
                       )
        existing_parcel = cursor.fetchone()

        if existing_parcel:
            parcel_id = existing_parcel[0]
        else:
            cursor.execute('INSERT INTO parcels (address, dist_id) VALUES (?, ?)', 
                           (tree.address, tree.dist_id)
                           )
            parcel_id = cursor.lastrowid
    
        cursor.execute('''
            INSERT INTO trees (status, species, maturation, health, last_seen, parcel_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (tree.status, tree.species, tree.maturation, tree.health, tree.last_seen, parcel_id))
    
        if existing_parcel:
            dist_id = tree.dist_id
        else:
            dist_id = tree.dist_id
            tree.parcel = Parcel(tree.address, tree.district)
            tree.parcel.add_tree(tree)
    
        self.connection.commit()
