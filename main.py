import pandas as pd
from jinja2 import Environment, FileSystemLoader
import pdfkit
from motivosDespido import get_motivo_despido

path_to_wkesohpta = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

config = pdfkit.configuration(wkhtmltopdf=path_to_wkesohpta)

# 1. Leer la tabla de datos
firedEmployees = pd.read_csv("./empleados.csv", encoding="utf-8")

env = Environment(loader=FileSystemLoader(".", encoding="utf-8"))
template = env.get_template("./template.html")

# 2. Rellenar la plantilla de la carta de despido
for index, row in firedEmployees.iterrows():

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

    with open(
        f'./letters/carta_despido_{row["nombre"]}_{row["apellidos"]}.html',
        "w",
        encoding="utf-8",
    ) as f:
        f.write(carta_despido)

    pdfkit.from_file(
        f'./letters/carta_despido_{row["nombre"]}_{row["apellidos"]}.html',
        output_path=f'./letters_pdf/carta_despido_{row["nombre"]}_{row["apellidos"]}.pdf',
        configuration=config,
    )
    # 3. Generar el PDF de la carta


# 4. Enviar el correo electrónico
