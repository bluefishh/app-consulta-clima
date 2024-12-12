import sqlite3

# Función para conectar a la base de datos de SQLite
def conectar_db():
    conn = sqlite3.connect('clima.db')
    return conn

# Crear la tabla de consultas si no existe para poder almacenar las consultas o histiorial
def crear_tabla():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS consultas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ciudad TEXT NOT NULL,
            clima TEXT NOT NULL,
            fecha DATETIME DEFAULT CURRENT_TIMESTAMP 
        )
    ''')
    conn.commit()
    conn.close()

# Guardar consulta en la base de datos, en la tabla consultas
def guardar_consulta(ciudad, humedad, temperatura, viento, cuidad, pais, descripcion):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO consultas (ciudad, clima, fecha) VALUES (?, ?, CURRENT_TIMESTAMP)', (ciudad, f"{temperatura}°C, {humedad}, {viento} km/h, {cuidad}, {pais}, {descripcion}"))
    conn.commit()
    conn.close()

# Obtener todas las consultas de la base de datos, tabla consultas
def obtener_consultas():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM consultas')
    consultas = cursor.fetchall()
    conn.close()
    return consultas

# Crear la tabla al iniciar el módulo
crear_tabla()