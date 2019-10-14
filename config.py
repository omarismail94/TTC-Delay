from configparser import ConfigParser
import psycopg2
import pandas as pd

# Credit to http://www.postgresqltutorial.com/postgresql-python/connect/
 
def config(filename='database.ini', section='postgresql'):
    '''function connects to Postgres database using .ini configuaration file'''

    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return db

def query(sql_command):
    '''function that takes user query and applies it to database'''
    
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        # print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        data = pd.read_sql(sql_command, conn)

       # close the communication with the PostgreSQL
        cur.close()
        return data

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            # print('Database connection closed.')