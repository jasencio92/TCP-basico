import socket
# ulizamos la libreria socket, para crear una conexión
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# configuramos el servidor
server.bind( ('localhost', 5000) )
# escuchar conexiones entrantes
server.listen(5) # máximo 5 conexiones
print("Servidor escuchando en el puerto 5000...")
while True: #siempre va a escuchar
    # acepta la conexión
    socket, client_address = server.accept()
    # devuelve un mensaje de conexión exitosa al clinte
    socket.send(f"¡Conexión establecida!".encode())
    while True:
        # recibe el mensaje
        data = socket.recv(1024)
        # Si no se recibe datos, cerrar la conexión
        if not data:
            socket.send("No he recibido un mensaje, ¡Hasta pronto!".encode())
            socket.close()
            break
        mensaje = data.decode().strip()
        # muestra el mensaje recibido
        print(f"Cliente envía: {mensaje}")
        # Si el mensaje es 'desconexion', cerrar la conexión.
        if mensaje.upper() == 'DESCONEXION':
            print(f"Conexión cerrada con {client_address}")
            socket.send("Cerrando conexión. ¡Hasta pronto!".encode())
            socket.close()
            break
        else:
            # Devolver el mensaje recibidio en mayúsculas
            respuesta = mensaje.upper()
            socket.send(respuesta.encode())
    print("Listo para mas conexiones")