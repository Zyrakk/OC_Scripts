import subprocess
import time

# Array de direcciones
direcciones = [
    "ping.online.net", "ping6.online.net", "ping-90ms.online.net", "ping6-90ms.online.net", 
    "iperf3.moji.fr", "iperf.par2.as49434.net", "paris.testdebit.info", "lille.testdebit.info", 
    "lyon.testdebit.info", "aix-marseille.testdebit.info", "bordeaux.testdebit.info", 
    "speedtest.serverius.net", "nl.iperf.014.fr", "ch.iperf.014.fr", "iperf.eenet.ee", 
    "iperf.astra.in.ua", "iperf.volia.net", "speedtest.uztelecom.uz", "iperf.it-north.net", 
    "iperf.biznetnetworks.com", "speedtest-iperf-akl.vetta.online", "iperf.scottlinux.com", 
    "iperf.he.net"
]

# Comando base
command_base = "iperf3 -c {} -u -b 850M -t 18"

# Función para ejecutar el comando y reintentar en caso de fallo
def execute_command(address):
    command = command_base.format(address)
    while True:
        try:
            print(f"Ejecutando comando: {command}")
            result = subprocess.run(command, shell=True, check=True, capture_output=True)
            print(f"Comando exitoso para {address}")
            print(result.stdout.decode())
            break  # Salir del bucle si el comando se ejecuta correctamente
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar comando para {address}: {e}")
            print("Reintentando en 5 segundos...")
            time.sleep(5)  # Esperar 5 segundos antes de reintentar

# Ejecutar el comando para cada dirección
for direccion in direcciones:
    execute_command(direccion)
