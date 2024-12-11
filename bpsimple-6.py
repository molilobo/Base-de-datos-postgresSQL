import psycopg
import configparser

def createTable(name,conn,cur):
    data = '''
    CREATE TABLE employee (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    last_name VARCHAR(100),
    start_date date,
    salary NUMERIC(10, 2)
    )
    '''
    cur.execute(data)
    conn.commit()


def consult(cur):
    table = "item"
    data = cur.execute(f"SELECT * FROM {table}")
    for row in data:
        print(row)

def connect_postgres():
    config = configparser.ConfigParser()  # Creo el objeto de la biblioteca de configuración
    config.read("config.ini")
    config_type = "bpsimple"
    print('aqui')

    with psycopg.connect(host=config.get(config_type, "Host"), port=config.get(config_type, "Port"),
                         user=config.get(config_type, "User"),
                         dbname=config.get(config_type, "Dbname"),
                         password=config.get(config_type, "Password")) as conn:
        print("Conectado a la base de datos")
        cur = conn.cursor()
       # consult(cur)
       # createTable("employee",conn,cur)

        query=""" UPDATE orderinfo 
        set employee_id  = 1
        where orderinfo_id = 4;
        UPDATE orderinfo 
        set employee_id  = 3
        where orderinfo_id = 5;
        UPDATE orderinfo 
        set employee_id  = 3
        where orderinfo_id = 2;
        UPDATE orderinfo 
        set employee_id  = 3
        where orderinfo_id = 3;
        UPDATE orderinfo 
        set employee_id  = 2
        where orderinfo_id = 1;
         """
#para hacer el uptade es importante un uptade por caa set
        data = cur.execute(query)
        print(data)

    return cur, conn


if __name__ == "__main__":
    try:
        cursor, connection = connect_postgres()

        if connection:
            cursor.close()
            connection.close()
            print("Connection to PostgreSQL database is closed")

    except Exception as e:
        print(f"Error al conectar: {e}")
