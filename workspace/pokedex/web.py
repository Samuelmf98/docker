from flask import Flask, render_template
import pandas as pd
import psycopg2


app = Flask(__name__)

# Parámetros de conexión a la base de datos PostgreSQL
db_params = {
    'host': "localhost", 
    'port': 5432,
    'database': "mydatabase",
    'user': "myuser",
    'password':"mypassword"
}

# Nombre de la tabla que deseas cargar en el DataFrame
nombre_tabla = 'public.pokedex_table'

# Consulta SQL para seleccionar todos los datos de la tabla
consulta_sql = f'SELECT * FROM {nombre_tabla};'

# Función para conectar a la base de datos y cargar datos en un DataFrame
def cargar_datos_desde_postgresql(params, consulta):
    try:
        # Conectar a la base de datos
        conexion = psycopg2.connect(**params)

        # Cargar datos en un DataFrame
        df = pd.read_sql_query(consulta, conexion)

        # Cerrar la conexión
        conexion.close()

        return df

    except Exception as e:
        print(f"Error: {e}")
        return None

# Cargar datos en un DataFrame
dataframe_resultado = cargar_datos_desde_postgresql(db_params, consulta_sql)

# Imprimir el DataFrame
print(dataframe_resultado)

@app.route('/')
def index():
    # Renderiza una plantilla HTML con el DataFrame
    return render_template('index.html', pokedex_data=dataframe_resultado.to_html(classes='data', index=False), titles=dataframe_resultado.columns.values)

if __name__ == '__main__':
    app.run(debug=True, port=5001) 