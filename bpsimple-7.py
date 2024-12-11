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
    table = "orderinfo"
    data = cur.execute(f"SELECT o.orderinfo_id,o.employee_id,c.fname,c.lname,e.name,e.last_name FROM {table} as o "
                       f"join customer as c on c.customer_id=o.customer_id "
                       f"join employee as e on e.id=o.employee_id "
                       )
    for row in data:
        orerinfo_id = row[0];
        fname = row[2]
        lname = row[3]
        ename = row[4]
        elast_name = row[5]
        print(f"el pedido {orerinfo_id} hecho por el cliente {fname } {lname} fue atendido por el emplead@ {ename}  {elast_name } con id {row[1]}")
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
        consult(cur)



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
