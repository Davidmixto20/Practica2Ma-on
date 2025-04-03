Proyecto: Verificación de Estado de Respuesta HTTP

Este proyecto verifica si una URL devuelve un código de estado 200 (OK) utilizando la biblioteca requests en Python.

Requisitos

Python 3.12.9

Biblioteca requests

Instalación

Clonar el Repositorio

Para obtener el código, clona este repositorio con:

 git clone https://github.com/usuario/proyecto.git
 cd proyecto

Crear un Entorno Virtual (Opcional)

Se recomienda utilizar un entorno virtual para gestionar las dependencias:

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

Instalar Dependencias

Ejecuta el siguiente comando para instalar requests:

pip install requests

Uso

Ejecuta el siguiente script en Python:

import requests

response = requests.get(url="https://www.google.com")

if response.status_code == 200:
    print("Response Exitosa")
else:
    print("No se pudo realizar el response")

Explicación del Código

Se importa la librería requests.

Se envía una solicitud GET a la URL https://www.google.com.

Se verifica el código de estado de la respuesta:

Si es 200, se imprime "Response Exitosa".

Si no, se imprime "No se pudo realizar el response".

Archivo .gitignore

Asegúrate de incluir un archivo .gitignore para evitar subir archivos innecesarios:

venv/
__pycache__/
*.pyc
*.pyo
*.pyd
.DS_Store

Licencia

Este proyecto es de uso libre.

Contacto

Para dudas o mejoras, contacta con el desarrollador o abre un issue en GitHub.

