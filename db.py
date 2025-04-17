import sqlite3

# ---------- Conexión y creación de tabla ----------  
def conectar():
    conexion = sqlite3.connect("tareas.db")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descripcion TEXT,
            estado TEXT DEFAULT 'pendiente'
        )
    ''')
    conexion.commit()
    return conexion

# ---------- Agregar tarea ----------  
def agregar_tarea(titulo, descripcion):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO tareas (titulo, descripcion)
        VALUES (?, ?)
    ''', (titulo, descripcion))
    conexion.commit()
    conexion.close()

# ---------- Obtener tareas ----------  
def obtener_tareas(filtro_estado=None):
    conexion = conectar()
    cursor = conexion.cursor()
    if filtro_estado and filtro_estado != "todos":
        cursor.execute('SELECT * FROM tareas WHERE estado = ?', (filtro_estado,))
    else:
        cursor.execute('SELECT * FROM tareas')
    tareas = cursor.fetchall()
    conexion.close()
    return tareas

# ---------- Eliminar tarea ----------  
def eliminar_tarea(id_tarea):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM tareas WHERE id = ?', (id_tarea,))
    conexion.commit()
    conexion.close()

# ---------- Cambiar estado ----------  
def marcar_completada(id_tarea):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        UPDATE tareas
        SET estado = 'completada'
        WHERE id = ?
    ''', (id_tarea,))
    conexion.commit()
    conexion.close()

# ---------- Exportar a CSV ----------  
def exportar_tareas_csv(nombre_archivo="tareas_exportadas.csv"):
    import csv
    tareas = obtener_tareas()
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(["ID", "Título", "Descripción", "Estado"])
        writer.writerows(tareas)
