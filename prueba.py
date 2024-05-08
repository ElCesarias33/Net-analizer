from scapy.all import sniff, IP, TCP, UDP

# Función para procesar los paquetes capturados
def process_packet(packet):
    # Extraer características para el análisis
       if packet.haslayer(IP):
        data = {
            "src_ip": packet[IP].src,
            "dst_ip": packet[IP].dst,
            "protocol": packet[IP].proto,
            "packet_length": len(packet),
        }
        if packet.haslayer(TCP):
            data["src_port"] = packet[TCP].sport
            data["dst_port"] = packet[TCP].dport
        elif packet.haslayer(UDP):
            data["src_port"] = packet[UDP].sport
            data["dst_port"] = packet[UDP].dport
            return data
        else:
            return None

# Capturar el tráfico de red (por ejemplo, 100 paquetes)
packets = sniff(count=100, prn=process_packet)
