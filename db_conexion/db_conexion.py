import psycopg2

# Configuración de la conexión a la base de datos
host = "localhost"          # Dirección del servidor PostgreSQL
database = "db_proyecto"    # Nombre de la base de datos
user = "postgres"         # Nombre de usuario de PostgreSQL
password = "admin"  # Contraseña del usuario
port = 5432                 # Puerto de PostgreSQL (por defecto)

try:
    # Conectar a PostgreSQL
    conexion = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port
    )
    print("✅ Conexión exitosa a la base de datos 'db_proyecto'")

    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()

    # Consulta de prueba: Mostrar todas las tablas
    print("\nDatos de la tabla 'productos':")
    cursor.execute("SELECT * FROM productos;")
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

    print("\nDatos de la tabla 'ventas':")
    cursor.execute("SELECT * FROM ventas;")
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

    # Cerrar cursor y conexión
    cursor.close()
    conexion.close()
    print("\n🔒 Conexión cerrada correctamente")

except Exception as e:
    print("❌ Error al conectar a PostgreSQL:", e)
