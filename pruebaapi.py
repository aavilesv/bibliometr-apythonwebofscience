import pandas as pd
import psycopg2

def insert_data_from_csv_to_db(csv_path, db_config):
    # Leer el archivo CSV
    df = pd.read_csv(csv_path)

    # Conectar a la base de datos
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # Establece el esquema correcto
    cursor.execute("SET search_path TO 'Schemas';")

    # Insertar datos en la tabla
    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO pred (columna_1, columna_2) VALUES (%s, %s)",
            (row['columna_1'], row['columna_2'])
        )

    conn.commit()
    cursor.close()
    conn.close()

# Configuración de la base de datos
db_config = {
    'host': 'aplicaciones-2.cujqunpvulqc.us-east-1.rds.amazonaws.com',
    'database': 'infra_nube',
    'user': 'postgres',
    'password': 'gL2lSfFoL0Yxkb8njFGS'
}

# Ruta al archivo CSV
csv_path = r'C:\Users\User\Downloads\pred.csv'

# Llamar a la función
insert_data_from_csv_to_db(csv_path, db_config)
