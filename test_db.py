import sqlite3

def test_db_connection():
    try:
        conn = sqlite3.connect('instance/holoocgsite.db')
        print("Database connection successful!")
    except sqlite3.Error as e:
        print(f"Database connection failed: {e}")
    finally:
        if conn:
            conn.close()

def query_users():
    try:
        conn = sqlite3.connect('instance/holoocgsite.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user")
        users = cursor.fetchall()
        print("Users in the database:")
        for user in users:
            print(user)
    except sqlite3.Error as e:
        print(f"Database query failed: {e}")
    finally:
        if conn:
            conn.close()

def delete_user(user):
    try:
        conn = sqlite3.connect('instance/holoocgsite.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM user WHERE id = 1")
        print(cursor.fetchall())
    except sqlite3.Error as e:
        print(f"Database query failed: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    test_db_connection()
    query_users()