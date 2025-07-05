from scapy.all import *

IP_SERVIDOR = "10.147.19.221"
PUERTO_RTSP = 8554

paquete1 = (
    "OPTIONS rtsp://{ip}:{port}/mystream RTSP/1.0\r\n"
    "CSeq: 999\r\n"
    "User-Agent: Fuzzi-inador/1.0\r\n"
    "X-Fuzz: \x00\xff\xfe\xfd\r\n"
    "\r\n"
).format(ip=IP_SERVIDOR, port=PUERTO_RTSP)

paquete2 = (
    "OPTIONS rtsp://{ip}:{port}/mystream RTSP/1.0\r\n"
    "CSeq: 9001\r\n"
    "User-Agent: JackieChan\r\n"
    "X-Random-Header: {lixo}\r\n"
    "\r\n"
).format(
    ip=IP_SERVIDOR,
    port=PUERTO_RTSP,
    lixo="".join(chr(i) for i in range(33, 127) if chr(i) not in ['\r', '\n'])
)

def construir_paquete_fuzz(payload):
    return IP(dst=IP_SERVIDOR)/TCP(dport=PUERTO_RTSP, sport=RandShort(), flags="PA")/Raw(load=payload.encode())

print("Enviando paquete 1: OPTIONS")
send(construir_paquete_fuzz(paquete1))

print("Enviando paquete 2: OPTIONS")
send(construir_paquete_fuzz(paquete2))