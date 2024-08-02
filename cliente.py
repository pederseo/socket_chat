import socket
import threading

def recibir_mensajes(cliente_socket):
    '''Función para recibir mensajes del servidor'''

    while True:
        try:
            mensaje = cliente_socket.recv(1024)
            if mensaje:
                print(f"Mensaje recibido: {mensaje.decode('utf-8')}")
            else:
                break
        except:
            break


def enviar_mensajes(cliente_socket):
    '''Función para enviar mensajes al servidor'''

    while True:
        mensaje = input()  # Leer mensaje del usuario
        cliente_socket.send(mensaje.encode('utf-8'))  # Enviar mensaje al servidor


# Configuración del cliente
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect(('127.0.0.1', 12345))  # Conectar al servidor
print("Conectado al servidor")

# Crear hilos para recibir y enviar mensajes
hilo_recibir = threading.Thread(target=recibir_mensajes, args=(cliente_socket,))
hilo_recibir.start()

enviar_mensajes(cliente_socket)
