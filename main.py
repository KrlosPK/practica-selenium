import os
import pandas as pd
import pdfkit
from smtplib import SMTP
from dotenv import load_dotenv
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader

from assets.motivosDespido import get_motivo_despido

# Cargamos las variables de entorno
load_dotenv(override=False)

print(os.environ.get("OUTLOOK_EMAIL"))

# Configuraciones para generar el PDF
path_to_wkesohpta = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_to_wkesohpta)

# * 1. Leer la tabla de datos
firedEmployees = pd.read_csv("./assets/empleados.csv", encoding="utf-8")

# Configuraciones para obtener la plantilla HTML
env = Environment(loader=FileSystemLoader(".", encoding="utf-8"))
template = env.get_template("./assets/template.html")

# Configuraciones para enviar los correos
sender_email = os.environ.get("OUTLOOK_EMAIL")
sender_password = os.environ.get("OUTLOOK_PASSWORD")

smtp_server = "smtp.office365.com"
smtp_port = 587
smtp_username = sender_email
smtp_password = sender_password

# * 2. Rellenar la plantilla de la carta de despido
for index, row in firedEmployees.iterrows():

    # Configuramos el mensaje
    msg = MIMEMultipart()
    msg["From"] = sender_email
    row["correo jefe"] = row["correo jefe"]
    msg["To"] = row["correo jefe"]
    msg["Subject"] = "Carta de despido"
    msg.attach(
        MIMEText("", "html")
    )  # Acá podemos poner algo en el body si es necesario

    # Generamos las variables para agregar a la plantilla
    carta_despido = template.render(
        nombre=row["nombre"],
        apellidos=row["apellidos"],
        cargo=row["cargo"],
        fechaContratacion=row["fecha de contratacion"],
        motivo_despido=get_motivo_despido(
            row["motivo de despido"], row["fecha de contratacion"]
        ),
        fecha_despido=row["fecha de despido"],
        jefe_inmediato=row["jefe inmediato"],
    )

    # Generamos las cartas de despido en HTML con base en las variables del CSV
    with open(
        f'./letters/carta_despido_{row["nombre"]}_{row["apellidos"]}.html',
        "w",
        encoding="utf-8",
    ) as f:
        f.write(carta_despido)

    carta_html = f'./letters/carta_despido_{row["nombre"]}_{row["apellidos"]}.html'
    carta_file = f'carta_despido_{row["nombre"]}_{row["apellidos"]}.pdf'
    carta_pdf = f"./letters_pdf/{carta_file}"

    # * 3. Generar el PDF de la carta
    pdfkit.from_file(
        carta_html,
        output_path=carta_pdf,
        configuration=config,
    )

    # * 4. Enviar el correo electrónico
    with open(carta_pdf, "rb") as f:
        pdf_attachment = MIMEApplication(f.read(), _subtype="pdf")
        pdf_attachment.add_header(
            "Content-Disposition", "attachment", filename=carta_file
        )
        msg.attach(pdf_attachment)

    with SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, row["correo jefe"], msg.as_string())
