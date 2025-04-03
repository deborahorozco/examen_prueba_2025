import pandas as pd

# cargo los datos
def cargar_datos(ruta_archivo):
    return pd.read_csv(ruta_archivo)

# convierto 'dt' a datetime y añadir columna 'year'
def procesar_fechas(df):
    df['dt'] = pd.to_datetime(df['dt'])
    df['year'] = df['dt'].dt.year
    return df

# Ejecución del script
if __name__ == "__main__":
    df = cargar_datos('datos_mock.csv')  
    df = procesar_fechas(df)
    print(df.head())