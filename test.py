import pytest
import requests
import pprint
import sqlite3


@pytest.fixture(scope='session')
def database_connection():
    connection = sqlite3.connect('dogs.db')
    yield connection
    connection.close()

def check_table_exist(database_connection):
    with database_connection as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * from Dogs")
        result = cursor.fetchone()
        assert result is not 0

def check_insert_table(database_connection):
    with database_connection as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Dogs (Name, Breed) VALUES (?, ?)", ("Teo", "Valdayan dalmatan"))
        result = cursor.fetchone()
        assert result is not 0

def check_update_table(database_connection):
    with database_connection as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Dogs Set Name = ? WHERE Breed = ?", ("Charik", "Valdayan dalmatan"))
        result = cursor.fetchone()
        assert result is not 0

def test_select_table_dog(database_connection):
        with database_connection as conn:
            cursor = conn.cursor()
            conn.commit()

            check_table_exist(database_connection)

def test_insert_table_dogs(database_connection):
        with database_connection as conn:
            cursor = conn.cursor()
            conn.commit()

            check_insert_table(database_connection)

def test_update_table_dogs(database_connection):
        with database_connection as conn:
            cursor = conn.cursor()
            conn.commit()

            check_update_table(database_connection)

def test_delete_from_table_dog(database_connection):
        with database_connection as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Dogs WHERE Name = ?", ("Charik"))
            conn.commit()