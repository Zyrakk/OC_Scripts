import time

# Cantidad de GB para usar
gb = 6

# Cantidad de segundos que debe durar el script
seg = 3600

# Cada elemento ocupa 1 byte. 6GB son aproximadamente 6 * 1024 * 1024 * 1024 bytes
data = bytearray(gb * 1024**3)

# Mantener los datos en memoria
time.sleep(seg)