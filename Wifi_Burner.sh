#!/bin/bash

# Array de direcciones
direcciones=("ping.online.net" "ping6.online.net" "ping-90ms.online.net" "ping6-90ms.online.net" "iperf3.moji.fr" "iperf.par2.as49434.net" "paris.testdebit.info" "lille.testdebit.info" "lyon.testdebit.info" "aix-marseille.testdebit.info" "bordeaux.testdebit.info" "speedtest.serverius.net" "nl.iperf.014.fr" "ch.iperf.014.fr" "iperf.eenet.ee" "iperf.astra.in.ua" "iperf.volia.net" "speedtest.uztelecom.uz" "iperf.it-north.net" "iperf.biznetnetworks.com" "speedtest-iperf-akl.vetta.online" "iperf.scottlinux.com" "iperf.he.net")

# Función para ejecutar iperf3
function ejecutar_iperf3 {
    local direccion=$1
    iperf3 -c ping.online.net -u -b 850M -t 1800
}

# Bucle infinito para asegurarse de que iperf3 se ejecuta
while true; do
    for direccion in "${direcciones[@]}"; do
        echo "Ejecutando iperf3 con $direccion"
        ejecutar_iperf3 $direccion

        # Verificar el código de salida de iperf3
        if [ $? -eq 0 ]; then
            echo "iperf3 se ejecutó correctamente con $direccion"
            exit 0
        else
            echo "iperf3 falló con $direccion, intentando con la siguiente dirección"
        fi
    done
done