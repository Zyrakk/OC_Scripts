import time
import threading
import os

def cpu_load(work_time, rest_time, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        start = time.time()
        # Trabajando por el tiempo de trabajo especificado
        while (time.time() - start) < work_time:
            pass
        # Durmiendo por el tiempo de descanso especificado
        time.sleep(rest_time)

# Parámetros
num_cores = os.cpu_count()  # Obtiene el número de núcleos del sistema
cpu_usage = 0.20
total_duration = 20  # 1 hora en segundos

# Calculando tiempos de trabajo y descanso
cycle_duration = 1  # 1 segundo
work_time = cycle_duration * cpu_usage
rest_time = cycle_duration - work_time

# Creando y iniciando hilos
threads = []
for _ in range(num_cores):
    thread = threading.Thread(target=cpu_load, args=(work_time, rest_time, total_duration))
    thread.start()
    threads.append(thread)

# Esperando a que todos los hilos terminen
for thread in threads:
    thread.join()

print("CPU load script completed.")
