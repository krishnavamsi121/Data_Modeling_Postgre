import psycopg2
from sql_queries import create_table_queries,drop_table_queries

def create_database():
    """
    Establish database connection and return conn and cursor references
    :return: (cur,conn)
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=admin")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf-8' TEMPLATE template0")
    conn.close()

    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=postgres password=admin")
    cur = conn.cursor()
    return cur,conn
def drop_tables(cur,conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

def create_tables(cur,conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    """
    Driver main function
    """
    cur, conn = create_database()
    drop_tables(cur,conn)
    print("Tables dropped successfully")

    create_tables(cur,conn)
    print("Tables created successfully")

    conn.close()


if __name__ == '__main__':
    main()
