from flask import Flask, render_template, request
from services.servicio_clima import obtener_clima
from services.servicio_db import guardar_consulta, obtener_consultas

# Configuración de la aplicación
app = Flask(__name__)

# Ruta principal o enpoint donde se va a renderizar la página principal de consulta del clima
@app.route('/', methods=['GET', 'POST'])
def index():
    # Variables iniciales
    clima = None
    error = None
    
    # Se obtiene la consulta del enpoint / cuando pongan una ciudad en el formulario
    if request.method == 'POST':
        ciudad = request.form['ciudad']

        # Se obtiene el clima enviando la ciudad al servicio servicio_clima.py el cual se comunica con la API de OpenWeather
        clima, error = obtener_clima(ciudad)

        # Si clima no es None, se guardan los datos de la consulta en la base de datos enviando la información al servicio servicio_db.py el cual hace
        # las transacciones en la base de datos
        if clima:
            # Guardar la consulta en la base de datos
            guardar_consulta(ciudad, clima['humedad'], clima['temperatura'], clima['viento'], clima['ciudad'], clima['pais'], clima['descripcion'])

    # Se retorna el template index.html con la variable clima y error para reenderizar la página
    return render_template('index.html', clima=clima, error=error)

# Ruta para el historial de consultas del clima
@app.route('/consultas')
def consultas():
    # Se obtienen todas las consultas de la base de datos desde el servicio servicio_db.py
    todas_las_consultas = obtener_consultas()

    # Se retorna el template consultas.html con la variable todas_las_consultas para reenderizar la página
    return render_template('consultas.html', consultas=todas_las_consultas)

# Ejecución de la aplicación
if __name__ == '__main__':
    app.run(debug=True)