#!/bin/bash

declare -a ips=("ping.online.net", "ping6.online.net", "ping-90ms.online.net")

# iperf3 -c ping.online.net -u -b 200M -t 15

echo ${ips[@]}

"ping.online.net", "ping6.online.net", "ping-90ms.online.net", "ping6-90ms.online.net", "iperf3.moji.fr", "iperf.par2.as49434.net", "paris.testdebit.info", "lille.testdebit.info", "lyon.testdebit.info", "aix-marseille.testdebit.info", "bordeaux.testdebit.info", "speedtest.serverius.net", "nl.iperf.014.fr", "ch.iperf.014.fr", "iperf.eenet.ee", "iperf.astra.in.ua", "iperf.volia.net", "speedtest.uztelecom.uz", "iperf.it-north.net", "iperf.biznetnetworks.com", "speedtest-iperf-akl.vetta.online", "iperf.scottlinux.com", "iperf.he.net"

