"""
Analizador de red

Script realizado para el monitoreo de la red local
"""

import numpy as np
import time
import psutil 
from scapy.all import sniff, IP, TCP, UDP
import matplotlib as mtp
import scipy as sp
from sklearn.cluster import MiniBatchKMeans

#Funcion de lector de paquetes
def lector_paquetes(intervalo):
    """

    """
    # Obtener la cantidad de paquetes al inicio
    network_stats_start = psutil.net_io_counters()
    packets_received_start = network_stats_start.packets_recv
    packets_sent_start = network_stats_start.packets_sent
    
    # Esperar el lapso de tiempo especificado
    time.sleep(intervalo)
    
    # Obtener la cantidad de paquetes al final
    network_stats_end = psutil.net_io_counters()
    packets_received_end = network_stats_end.packets_recv
    packets_sent_end = network_stats_end.packets_sent
    
    # Calcular la cantidad de paquetes recibidos y enviados durante el lapso de tiempo
    packets_received_during_interval = packets_received_end - packets_received_start
    packets_sent_during_interval = packets_sent_end - packets_sent_start
    
    return packets_received_during_interval, packets_sent_during_interval

#Funcion para puertos
def lector_puertos(flag):
    """
    Si la "flag" (bandera) es detectada como amenaza dara lectura al puerto
    podran identificar mas rapido posibles amenazas
    """
    if flag > 2:
        connections = psutil.net_connections(kind='inet')
        outbound_ports = set()
        for conn in connections:
            if conn.status == psutil.CONN_ESTABLISHED:
                outbound_ports.add(conn.laddr.port)
        return outbound_ports
    
#Funcion para obtener datos mas puntuales
def datos_ocultos():
    """
    
    """
    print("Datos...")

#Funcion para clustering
def agrupamiento() -> int:
    """
    Mini Batch K-Means
    """



    print("Agrupando")

#Funcion para copilar los datos
def datos_DB(paquetes, **datos) -> None:
    """
    Guarda datos de paquetes y puertos
    """

    print("Se han guardado los registros!")

#Funcion para mostrar los datos
def mostrar_datos(**datos) -> None:
    """

    """

    print("Muestra...")

#Funcion para generar reportes en funcion de un tiempo solicitado
def generador_reportes(tiempo) -> None:
    """
    Generador de reportes de tiempo
    tiempo actual - timepo solicitado
    Solicita registros historicos
    """

    print("Datos")