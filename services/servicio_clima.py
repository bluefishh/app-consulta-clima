import requests

# Se configuran las variables de la API de OpenWeather para poder traer información del clima
API_KEY = '4e59698163608e4e6bc2176bf77e8491'  # Clave de API, acá puse una ficticia pero la real se saca de la web de OpenWeather
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Función para obtener el clima de una ciudad, hace la petición a la API de OpenWeather
def obtener_clima(ciudad):
    try:
        # Se hace la petición a la API de OpenWeather enviando los parámetros
        respuesta = requests.get(BASE_URL, params={'q': ciudad, 'appid': API_KEY, 'units': 'metric', 'lang': 'es'})
        
        # Si la respuesta es exitosa, se obtiene la información del clima
        if respuesta.status_code == 200:
            # Se obtienen los datos del clima en forma de diccionario o JSON
            datos = respuesta.json()
            # Se inicializan las variables con la información del JSON
            humedad = datos['main']['humidity']
            temperatura = datos['main']['temp']
            viento = datos['wind']['speed']
            icono = datos['weather'][0]['icon']
            ciudad = datos['name'];
            pais = datos['sys']['country']
            descripcion = datos['weather'][0]['description']
            # Retornar la información del clima que se sacó en las variables    
            return {
                'temperatura': round(temperatura, 2),  # Se redondea a 2 decimales de la temperatura
                'humedad': humedad,
                'viento': round(viento * 3.6, 2), # Acá se convierte de  m/s a km/h la velocidad del viento
                'icono': icono, # Icono de la imagen que se muestra en el index del clima
                'ciudad': ciudad, 
                'pais': pais,
                'descripcion': descripcion
            }, None
        else:
            # Si no se obtuvo el clima de la ciudad especificada, retornar None y el mensaje de error
            return None, "Ciudad no encontrada. Intenta de nuevo."
    except Exception as e:
        # Si no puede comunicar con la API, retornar None y el mensaje de error
        return None, f"Error al consultar la API: {str(e)}"

