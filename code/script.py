import pandas as pd

# Función para cargar datos
def cargar_datos(ruta):
    return pd.read_csv(ruta,sep=';')

# Función para convertir 'dt' a datetime y añadir columna 'year'

def procesar_fechas(df):
    df['dt'] = pd.to_datetime(df['dt'])
    df['year'] = df['dt'].dt.year
    return df

# Ejecución del script
if __name__ == "__main__":
    ruta = '/Users/debbieorozco/Documents/GitHub/examen_prueba_2025/data/datos_mock.csv'
    df = cargar_datos(ruta)  
    df = procesar_fechas(df)
    print(df.head())


