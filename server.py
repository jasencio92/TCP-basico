import socket

# Crear un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configurar el servidor para que escuche en la IP localhost y puerto 12345
server_socket.bind(('localhost', 12345))

# Escuchar conexiones entrantes (máximo 5 conexiones en espera)
server_socket.listen(5)
print("Servidor escuchando en el puerto 12345...")
contador = 0

while True:
    contador += 1
    # Aceptar una conexión entrante
    client_socket, client_address = server_socket.accept()
    print(f"Conexión establecida con {client_address}")

    # Enviar un mensaje de bienvenida al cliente
    # Codificamos el mensaje antes de enviarlo
    client_socket.send(f"¡Hola, Jorge! {contador}".encode())

    # Recibir datos enviados por el cliente
    data = client_socket.recv(1024)  # Lee hasta 1024 bytes
    print(f"Datos recibidos: {data.decode()}")

    # Cerrar la conexión con el cliente
    client_socket.close()
    print(f"Conexión cerrada con {client_address}")

