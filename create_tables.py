import psycopg2

def create_database():
    """
    Establish database connection and return conn and cursor references
    :return: (cur,conn)
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=postgres username=postgres password=admin")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CRATE DATABASE sparkify WITH ENCODING 'utf-8' TEMPLATE template0")
    conn.close()

    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb username=postgres password=admin")
    cur = conn.cursor()
    return cur,conn
def drop_tables():



def create_tables():


def main():


if __name__ == '__main__':
    main()