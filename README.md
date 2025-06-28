# Tarea 3 Redes - Inyección y Modificación de Tráfico con Scapy

Este proyecto corresponde a la **Tarea 3 del curso de Redes**, en la cual se analiza el comportamiento de una arquitectura cliente-servidor ante la **inyección y modificación de paquetes de red**, utilizando la herramienta **Scapy**.

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
│   └── servidor.py
├── video/
│   └── demo.mp4
├── informe/
│   └── informe.pdf
└── README.md
```

---

## ⚙️ Requisitos

- Docker (recomendado para el cliente)
- Python 3.x
- Scapy (`pip install scapy`) si se instala localmente

---

## 🚀 Instalación y ejecución

### Servidor

```bash
cd servidor
python3 servidor.py
```

Asegúrate de que el servidor esté corriendo antes de ejecutar Scapy.

---

### Cliente con Scapy (usando contenedor)

```bash
cd cliente
docker build -t scapy-container .
docker run -it --net=host --cap-add=NET_ADMIN --cap-add=NET_RAW scapy-container
```

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
