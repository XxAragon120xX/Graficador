import pandas as pd
import matplotlib.pyplot as plt

def cargar_datos_espectrales(archivo):
    
    try:
        # Leer el archivo
        datos = pd.read_csv(archivo, names=["X", "Y"])
        
        # Encontrar los límites de los datos
        inicio = datos.index[datos["X"] == "XYDATA"].tolist()[0]
        fin = datos.index[datos["X"] == "##### Extended Information"].tolist()[0]
        
        # Extraer los datos importantes
        datos_utiles = datos.iloc[inicio + 1:fin, :]
        datos_utiles.reset_index(drop=True, inplace=True)
        
        # Convertir a números y normalizar
        datos_utiles = datos_utiles.astype(float)
        datos_utiles["Y"] /= datos_utiles["Y"].max()
        
        return datos_utiles
    
    except Exception as error:
        print(f"Algo esta fallando maquinota: {error}")
        return None

def graficar_espectro(datos, archivo):
    """Genera la gráfica de los datos espectrales."""
    plt.figure(figsize=(10, 5))
    plt.plot(datos["X"], datos["Y"], color='darkblue', linewidth=2)
    
    plt.title(f'Espectro de {archivo}')
    plt.xlabel('Número de onda [$\mathregular{cm^{-1}]}$')
    plt.ylabel('Transmisión (u.a.)')
    
    plt.xlim(4000, 500)
    plt.ylim(0, 1.05)
    plt.grid(True, linestyle='--', alpha=0.6)
    
    plt.tight_layout()
    plt.show()

# Script principal
archivo = 'Datos-SFDA.csv'
datos = cargar_datos_espectrales(archivo)

if datos is not None:
    graficar_espectro(datos, archivo)