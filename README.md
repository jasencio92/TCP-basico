# TCP básico con python

# Herramientas:
    Python 3
    socket

# Información
* El servidor TCP escucha en un puerto específico (5000), por lo que debes crear un socket de servidor y configurarlo para que escuche conexiones entrantes.
* El servidor debe aceptar conexiones y, una vez que se establece la conexión, podrá recibir y enviar datos.
* El servidor está configurado para escuchar en localhost (IP 127.0.0.1) y el puerto 5000

```
1.- Escuchar conexiones: server_socket.listen(5) configura el servidor para que escuche hasta 5 conexiones en espera.
2.- Aceptar conexiones: server_socket.accept() acepta una conexión entrante y devuelve un socket de cliente (client_socket) y la dirección del cliente (client_address).
3.- Intercambiar datos: El servidor envía un mensaje al cliente con client_socket.send() y luego recibe datos con client_socket.recv().
4.- Cerrar la conexión: Una vez que se han recibido los datos y se ha respondido al cliente, la conexión se cierra con client_socket.close().
```

# Ejemplo de uso:
 - Ejecutar el servidor (server.py) y posterior el cliente (customer.py) en otra terminal.
    terminal 1:
        python3 server.py
    terminal 2:
        python3 customer.py
 - El cliente debe ingresar un mensaje y luego enviarlo al servidor.
 - El cliente recibe y muestra el mensaje en consola y procede a devolverlo en mayusculas.
 - Si el usuario ingresa la palabra "desconexion", procede a finalizar la conexión.

# Resumen
Esto debería mostrar cómo el cliente se conecta al servidor, recibe un mensaje de bienvenida y luego envía un mensaje al servidor.
Este es un ejemplo básico de un servidor y cliente TCP en Python 3.
Valida si el usuario envia mensajes, si no envia se procede a cerrar la conexión.

<i>Jorge Asencio' :)</i>