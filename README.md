# Automatización Selenium

## Contexto

Estás trabajando en una empresa donde es necesario automatizar el proceso de creación y envío de cartas de despido. Se te proporciona una tabla con la información de los empleados que serán despedidos, así como una plantilla de carta de despido. Tu tarea es desarrollar un código en Python que automatice este proceso utilizando Selenium y otras librerías útiles.

## Objetivo

Automatizar la generación de cartas de despido en formato PDF y su envío por correo electrónico a los jefes inmediatos de los empleados.

## Pasos a seguir

**1. Leer la tabla de datos:**
o Utiliza pandas para leer la tabla proporcionada en formato CSV o directamente desde el DataFrame.

**2. Rellenar la plantilla de la carta de despido:**
o Utiliza una librería como Jinja2 para rellenar la plantilla de la carta con la información específica de cada empleado.

**3. Generar el PDF de la carta:**
o Utiliza WeasyPrint o pdfkit para convertir la carta en un archivo PDF.

**4. Enviar el correo electrónico:**
o Utiliza smtplib y email para enviar el PDF generado al jefe inmediato del empleado.

## Herramientas y librerías sugeridas

• pandas para manipulación de datos.

• Jinja2 para trabajar con plantillas de texto.

• WeasyPrint o pdfkit para generar PDFs.

• smtplib y email para enviar correos electrónicos.

• Selenium para automatizar cualquier interacción web que pueda ser necesaria (como abrir y verificar el correo electrónico del jefe inmediato).

**Nota: hace falta la colimna de correos jefe inmediato.**

Puedes usar, IA para crear las cartas según el motivo de despido

## Pasos para la instalación

**1. Primero debes instalar [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)**: es necesario para generar los PDFs.

**2. Luego, instala las dependencias:**

```js
pip install ./requirements.txt
```

**3. Crea las variables de entorno:** crea un archivo **.env** en la raíz del proyecto con las credenciales para enviar el correo.

Básate del archivo **[.env.example](./.env.example)**

**4. Ejecuta el proyecto:**

```js
python ./main.py
```
