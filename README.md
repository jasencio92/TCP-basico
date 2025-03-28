TCP básico con python

* El servidor TCP escucha en un puerto específico, por lo que debes crear un socket de servidor y configurarlo para que escuche conexiones entrantes.
* El servidor debe aceptar conexiones y, una vez que se establece la conexión, podrá recibir y enviar datos.
* El servidor está configurado para escuchar en localhost (IP 127.0.0.1) y el puerto 5000

1.- Escuchar conexiones: server_socket.listen(5) configura el servidor para que escuche hasta 5 conexiones en espera.
2.- Aceptar conexiones: server_socket.accept() acepta una conexión entrante y devuelve un socket de cliente (client_socket) y la dirección del cliente (client_address).
3.- Intercambiar datos: El servidor envía un mensaje al cliente con client_socket.send() y luego recibe datos con client_socket.recv().
4.- Cerrar la conexión: Una vez que se han recibido los datos y se ha respondido al cliente, la conexión se cierra con client_socket.close().

Ejemplo de uso:
 - Ejecutar el servidor (server.py) y posterior el cliente (customer.py) en otra terminal.


Esto debería mostrar cómo el cliente se conecta al servidor, recibe un mensaje de bienvenida y luego envía un mensaje al servidor.
Este es un ejemplo básico de un servidor y cliente TCP en Python 3.
