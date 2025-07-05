from scapy.all import *

INTERFAZ_VPN = "ztrf23gpht"
PUERTO_RTSP = 8554

def ver_paquetes(pkt):
    if pkt.haslayer(TCP) and pkt.haslayer(Raw):
        carga = pkt[Raw].load
        if b"RTSP" in carga or b"OPTIONS" in carga or b"DESCRIBE" in carga or b"SETUP" in carga or b"PLAY" in carga:
            print("\nPaquete RTSP detectado:")
            try:
                print(carga.decode(errors='ignore'))
            except:
                print("[!] Paquete no decodificable (probablemente binario)")

print(f"Escuchando trÃ¡fico RTSP TCP en interfaz '{INTERFAZ_VPN}' puerto {PUERTO_RTSP}...")
sniff(
    iface=INTERFAZ_VPN,
    filter=f"tcp port {PUERTO_RTSP}",
    prn=ver_paquetes,
    store=0
)