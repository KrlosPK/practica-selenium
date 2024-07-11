import pandas as pd
import pdfkit
from jinja2 import Environment, FileSystemLoader
from assets.motivosDespido import get_motivo_despido

# Configuraciones para generar el PDF
path_to_wkesohpta = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_to_wkesohpta)

# * 1. Leer la tabla de datos
firedEmployees = pd.read_csv("./assets/empleados.csv", encoding="utf-8")

# Configuraciones para obtener la plantilla HTML
env = Environment(loader=FileSystemLoader(".", encoding="utf-8"))
template = env.get_template("./assets/template.html")

# * 2. Rellenar la plantilla de la carta de despido
for index, row in firedEmployees.iterrows():

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

    # * 3. Generar el PDF de la carta
    pdfkit.from_file(
        f'./letters/carta_despido_{row["nombre"]}_{row["apellidos"]}.html',
        output_path=f'./letters_pdf/carta_despido_{row["nombre"]}_{row["apellidos"]}.pdf',
        configuration=config,
    )

# * 4. Enviar el correo electrónico
