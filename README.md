# Tarea 3 Redes - Inyección y Modificación de Tráfico con Scapy

Este proyecto corresponde a la **Tarea 3 del curso de Redes**, en la cual se analiza el comportamiento de una arquitectura cliente-servidor ante la **inyección y modificación de paquetes de red**, utilizando la herramienta **Scapy** y el protocolo **RTSP** para transmisión de video.

---

## 📌 Objetivo

- Interceptar, modificar e inyectar tráfico no esperado entre cliente y servidor.
- Analizar los efectos que estas alteraciones provocan sobre el servicio.
- Utilizar **fuzzing** y modificaciones específicas de campos del protocolo.

---

## 🧩 Estructura del proyecto

```
.
├── cliente/
│   ├── Dockerfile
│   ├── script_inyeccion.py
│   └── script_modificacion.py
├── servidor/
│   ├── Dockerfile
│   └── servidor.py
├── video/
│   └── demo.mp4
├── informe/
│   └── informe.pdf
└── README.md
```

---

## ⚙️ Requisitos

- Docker (recomendado para cliente y servidor)
- Python 3.x
- Scapy (`pip install scapy`) si se instala localmente
- ffmpeg (para enviar video RTSP)

---

## 🚀 Instalación y ejecución

### Servidor (Docker)

Desde la carpeta `servidor/`, construye y ejecuta el contenedor del servidor RTSP:

```bash
cd servidor
docker build -t servidor-rtsp .
docker run -it --rm --name servidor-rtsp --net=host servidor-rtsp
```

> ⚠️ Usamos `--net=host` para permitir acceso completo al tráfico de red, necesario para probar Scapy.

---

### Cliente (Docker con Scapy)

Desde la carpeta `cliente/`, construye y ejecuta el contenedor con Scapy:

```bash
cd cliente
docker build -t cliente-scapy .
docker run -it --rm --name cliente-scapy --net=host --cap-add=NET_ADMIN --cap-add=NET_RAW cliente-scapy
```

---

## 🎥 Envío de flujo RTSP desde el cliente

Para enviar un flujo de video de prueba al servidor usando RTSP (por ejemplo, con `ffmpeg`):

```bash
ffmpeg -re -stream_loop -1 -i video_prueba.mp4 -c copy -f rtsp rtsp://localhost:8554/mistream
```

- `-re`: envía el video en tiempo real.
- `-stream_loop -1`: repite el video infinitamente.
- `-i video_prueba.mp4`: tu archivo de video local.
- `rtsp://localhost:8554/mistream`: dirección del servidor RTSP (ajústala si es diferente).

> Si el servidor escucha en otra IP, reemplaza `localhost` por la IP correspondiente (por ejemplo, `192.168.1.100`).

---

## 🧪 Scripts Scapy

### 1. Inyecciones con fuzzing

```bash
python3 script_inyeccion.py
```

Este script realiza **2 inyecciones de paquetes modificados aleatoriamente** que simulan datos corruptos o inesperados para probar la robustez del servidor.

---

### 2. Modificación de campos del protocolo

```bash
python3 script_modificacion.py
```

Este script realiza **3 modificaciones dirigidas** a campos específicos del protocolo, como el tipo de mensaje o el contenido de los datos, para observar comportamientos anómalos.

---

## 📹 Video demostrativo

Se encuentra disponible en la carpeta `/video/demo.mp4`.

También puedes verlo en [YouTube](https://youtube.com/...) *(reemplaza con el enlace si corresponde).*

---

## 📝 Informe

El informe completo con el análisis, resultados y conclusiones se encuentra en la carpeta `/informe/informe.pdf`.

---

## 📚 Autores

- Nombre 1 – Rol: Servidor
- Nombre 2 – Rol: Cliente / Scapy

---

## ✉️ Contacto

Para cualquier duda o comentario sobre este trabajo, puedes escribir a:

- alumno1@uc.cl
- alumno2@uc.cl
