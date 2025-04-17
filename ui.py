import tkinter as tk
from tkinter import messagebox
from db import agregar_tarea, obtener_tareas, eliminar_tarea, marcar_completada, exportar_tareas_csv

def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Gestor de Tareas")
    ventana.geometry("700x600")

    # ---------- Entrada de datos ----------
    tk.Label(ventana, text="Título de la Tarea:").pack()
    entry_titulo = tk.Entry(ventana, width=50)
    entry_titulo.pack(pady=5)

    tk.Label(ventana, text="Descripción:").pack()
    entry_descripcion = tk.Text(ventana, height=5, width=50)
    entry_descripcion.pack(pady=5)

    # ---------- Filtro de estado ----------
    tk.Label(ventana, text="Filtrar tareas por estado:").pack(pady=(10, 0))
    estado_var = tk.StringVar(value="todos")
    opciones_estado = ["todos", "pendiente", "completada"]
    estado_menu = tk.OptionMenu(ventana, estado_var, *opciones_estado)
    estado_menu.pack(pady=5)

    # ---------- Listbox para mostrar tareas ----------
    tk.Label(ventana, text="Lista de Tareas:").pack(pady=(10, 0))
    lista_tareas = tk.Listbox(ventana, width=80, height=10)
    lista_tareas.pack(pady=5)

    # ---------- Función para cargar tareas al iniciar ----------
    def cargar_tareas():
        lista_tareas.delete(0, tk.END)
        estado = estado_var.get()
        tareas = obtener_tareas(filtro_estado=estado)
        for tarea in tareas:
            # Si la tupla tiene 3 elementos, asignamos "pendiente" como valor predeterminado
            if len(tarea) == 3:
                id_tarea, titulo, descripcion = tarea
                estado_tarea = "pendiente"
            elif len(tarea) == 4:
                id_tarea, titulo, descripcion, estado_tarea = tarea
            else:
                # Si se obtiene otro número inesperado de columnas, se ignora la fila
                continue
            texto = f"{id_tarea} - {titulo} - {descripcion[:40]}... - {estado_tarea}"
            lista_tareas.insert(tk.END, texto)

    # ---------- Función para agregar nueva tarea (callback) ----------
    def agregar_tarea_callback():
        titulo = entry_titulo.get()
        descripcion = entry_descripcion.get("1.0", tk.END).strip()
        if not titulo:
            messagebox.showwarning("Campo obligatorio", "El título es obligatorio.")
            return
        # Agregar tarea en la base de datos (se utiliza la función importada de db)
        agregar_tarea(titulo, descripcion)
        # Limpiar campos
        entry_titulo.delete(0, tk.END)
        entry_descripcion.delete("1.0", tk.END)
        # Refrescar lista
        cargar_tareas()
        messagebox.showinfo("Tarea agregada", f"Tarea '{titulo}' agregada con éxito.")

    # ---------- Botón para agregar tarea ----------
    tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea_callback).pack(pady=10)
    
    # Cargar tareas al iniciar
    cargar_tareas()

    # ---------- Función para eliminar tarea (callback) ----------
    def eliminar_tarea_callback():
        seleccion = lista_tareas.curselection()
        if not seleccion:
            messagebox.showwarning("Seleccionar tarea", "Selecciona una tarea para eliminar.")
            return
        indice = seleccion[0]
        tarea_texto = lista_tareas.get(indice)
        try:
            id_tarea = int(tarea_texto.split(" - ")[0])
        except (IndexError, ValueError):
            messagebox.showerror("Error", "No se pudo obtener el ID de la tarea.")
            return
        eliminar_tarea(id_tarea)
        cargar_tareas()
        messagebox.showinfo("Tarea eliminada", "Tarea eliminada con éxito.")

    # ---------- Botón para eliminar tarea ----------
    tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea_callback, bg="#e74c3c", fg="white").pack(pady=5)

    # ---------- Función para marcar tarea como completada ----------
    def completar_tarea():
        seleccion = lista_tareas.curselection()
        if not seleccion:
            messagebox.showwarning("Seleccionar tarea", "Selecciona una tarea para completar.")
            return
        indice = seleccion[0]
        tarea_texto = lista_tareas.get(indice)
        try:
            id_tarea = int(tarea_texto.split(" - ")[0])
        except (IndexError, ValueError):
            messagebox.showerror("Error", "No se pudo obtener el ID de la tarea.")
            return
        marcar_completada(id_tarea)
        cargar_tareas()
        messagebox.showinfo("Tarea completada", "La tarea fue marcada como completada.")

    # ---------- Botón para completar tarea ----------
    tk.Button(ventana, text="Marcar como completada", command=completar_tarea, bg="#2ecc71", fg="white").pack(pady=5)

    # ---------- Función para exportar tareas a CSV ----------
    def exportar_csv():
        exportar_tareas_csv("tareas_exportadas.csv")
        messagebox.showinfo("Exportación completada", "Tareas exportadas a tareas_exportadas.csv")

    # ---------- Botón para exportar tareas a CSV ----------
    tk.Button(ventana, text="Exportar tareas a CSV", command=exportar_csv, bg="#f39c12", fg="white").pack(pady=10)

    ventana.mainloop()
