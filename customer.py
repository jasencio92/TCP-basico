import socket
import time

while True:
    # Crear un socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectar al servidor en localhost y puerto 12345
    client_socket.connect(('localhost', 12345))

    # Recibir el mensaje enviado por el servidor
    data = client_socket.recv(1024)
    print(f"Mensaje del servidor: {data.decode()}")

    # Escribes un mensaje
    mensaje = input("Escribe tu mensaje: ")

    # Enviar un mensaje al servidor
    client_socket.send(mensaje.encode())

    # Cerrar la conexión
    client_socket.close()

