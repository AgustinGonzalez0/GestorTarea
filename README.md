# Gestor de Tareas

## Descripción

**Gestor de Tareas** es una aplicación de escritorio desarrollada en Python que ofrece una solución intuitiva para gestionar y organizar tareas diarias. La aplicación cuenta con una interfaz gráfica amigable creada con Tkinter y utiliza SQLite para el almacenamiento persistente de datos. Está diseñada para ayudar a los usuarios a mantener un registro organizado de sus tareas, facilitando el seguimiento de su progreso y la priorización de actividades tanto personales como profesionales.

## Características

- **Creación y administración de tareas:**  
  Permite agregar tareas con título y descripción, asegurando que se capturan los detalles esenciales desde el inicio.

- **Gestión de estados:**  
  Cada tarea se asigna inicialmente al estado "pendiente". Los usuarios pueden marcar tareas como completadas, lo que facilita la visualización del progreso.

- **Filtrado de tareas:**  
  La aplicación ofrece opciones para filtrar tareas según su estado (todos, pendiente, completada), permitiendo una organización óptima.

- **Exportación a CSV:**  
  Los usuarios pueden exportar la lista de tareas a un archivo CSV para análisis, reporte o respaldo.

## Arquitectura y Organización del Proyecto

El proyecto sigue una estructura modular que permite una separación clara de responsabilidades:

- **`main.py`:**  
  Punto de entrada del programa. Se encarga de iniciar la aplicación invocando la ventana principal.
  
- **`ui.py`:**  
  Contiene la lógica de la interfaz gráfica. Se gestionan las entradas del usuario, se muestran las tareas y se coordinan las interacciones de los botones (agregar, eliminar, marcar completada, exportar).
  
- **`db.py`:**  
  Implementa la capa de acceso a datos utilizando SQLite. Aquí se realizan operaciones de inserción, consulta, eliminación y actualización sobre la base de datos.

Esta organización garantiza la facilidad de mantenimiento y la escalabilidad del sistema.

## Requisitos

- **Python 3.13** (o una versión compatible)  
- **Tkinter:** Incluido en la mayoría de las distribuciones de Python.  
- **SQLite:** No requiere instalación adicional al utilizar el módulo `sqlite3` que viene integrado en Python.

> **Nota:** En algunos sistemas operativos puede ser necesario instalar componentes adicionales para que Tkinter funcione correctamente.
