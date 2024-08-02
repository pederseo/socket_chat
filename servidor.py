import socket
import threading

def manejar_cliente(cliente_socket):
    '''Función para manejar las conexiones de los clientes'''
    while True:
        try:
            mensaje = cliente_socket.recv(1024)  # Recibir mensaje del cliente
            if mensaje:
                print(f"Mensaje recibido: {mensaje.decode('utf-8')}")
                broadcast(mensaje, cliente_socket)  # Enviar mensaje a todos los clientes
            else:
                eliminar_cliente(cliente_socket)
                break
        except:
            eliminar_cliente(cliente_socket)
            break

def broadcast(mensaje, cliente_socket):
    '''Función para enviar mensajes a todos los clientes'''
    for cliente in clientes:
        if cliente != cliente_socket:
            try:
                cliente.send(mensaje)  # Enviar mensaje a otro cliente
            except:
                eliminar_cliente(cliente)

def eliminar_cliente(cliente_socket):
    '''Función para eliminar un cliente de la lista'''
    if cliente_socket in clientes:
        clientes.remove(cliente_socket)
        cliente_socket.close()


# Configuración del servidor
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_socket.bind(('0.0.0.0', 12345))  # Vincular el socket a la dirección y puerto
servidor_socket.listen(5)  # Escuchar hasta 5 conexiones entrantes
print("Servidor escuchando en el puerto 12345")

clientes = []  # Lista para almacenar los sockets de los clientes

# Aceptar conexiones entrantes
while True:
    cliente_socket, direccion = servidor_socket.accept()
    clientes.append(cliente_socket)
    print(f"Conexión aceptada de {direccion}")
    hilo_cliente = threading.Thread(target=manejar_cliente, args=(cliente_socket,))
    hilo_cliente.start()
