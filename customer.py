import socket
# Crear un socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conectarse al servidor en localhost y puerto 5000
client_socket.connect( ('localhost', 5000) )
# Recibir mensaje de bienvenida del servidor
welcome = client_socket.recv(1024).decode()
print(welcome)
while True:
    # solicitamos al usuario que ingrese un mensaje
    message = input("Ingrese un mensaje para el servidor: ")
    if len(message) > 0: # valida que tengamos datos en la entrada del input
        # enviamos el mensaje al servidor
        client_socket.send(message.encode())
        # si el mensaje es "desconexion"
        if message.lower().strip() == 'desconexion': #Valida la entrada
            # recibe la respuesta e imprime para cerrar el while y proceder a cerrar la conexión
            answer = client_socket.recv(1024).decode()
            print(answer)
            # rompe el ciclo, para cerrar la conexión
            break
        # recibe y muestra la respuesta del servidor
        answer = client_socket.recv(1024).decode()
        print(f"Servidor responde: {answer}")
    else: # si no envia un mensaje, cierra la conexión actual
        # imprime alerta
        print("Hemos decidido cerrar la conexión al no recibir ningun mensaje")
        # rompe el ciclo, para cerrar la conexión
        break
# cierra la conexión
client_socket.close()