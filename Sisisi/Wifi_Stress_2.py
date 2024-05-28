import subprocess
import time
import random

# Array de direcciones
direcciones = ["ping.online.net", "ping6.online.net", "ping-90ms.online.net", "ping6-90ms.online.net", "iperf3.moji.fr"]

# Comando base
command_base = "iperf3 -c {} -u -b 850M -t 1800"

# Función para ejecutar el comando y detenerse en caso de éxito
def execute_command(address):
    command = command_base.format(address)
    while True:
        try:
            print(f"Ejecutando comando: {command}")
            result = subprocess.run(command, shell=True, check=True, capture_output=True)
            print(f"Comando exitoso para {address}")
            print(result.stdout.decode())
            return True  # Salir del bucle si el comando se ejecuta correctamente
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar comando para {address}: {e}")
            print("Reintentando con una dirección diferente en 5 segundos...")
            time.sleep(5)  # Esperar 5 segundos antes de reintentar
            return False  # Indicar que hubo un fallo y se necesita reintentar con otra dirección

# Lista de direcciones pendientes de ejecución
pending_addresses = direcciones.copy()

# Mientras haya direcciones pendientes
while pending_addresses:
    # Seleccionar una dirección aleatoria de las pendientes
    address = random.choice(pending_addresses)
    # Intentar ejecutar el comando
    if execute_command(address):
        # Si el comando tuvo éxito, salir del bucle principal
        break
    else:
        # Si falló, eliminar la dirección de la lista para no intentar nuevamente con la misma inmediatamente
        pending_addresses.remove(address)

print("Script finalizado.")
