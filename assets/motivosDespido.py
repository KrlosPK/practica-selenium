motivos_despido = {
  'Rendimiento insuficiente': 'Lamentamos informarle que su empleo con nuestra empresa será terminado a partir del {{ fecha_despido }}. Esta decisión ha sido tomada debido a su rendimiento insuficiente, que no ha cumplido con los estándares esperados a pesar de los esfuerzos de apoyo y capacitación proporcionados.',

  'Reestructuración': 'Lamentamos informarle que su empleo con nuestra empresa será terminado a partir del {{ fecha_despido }}. Esta decisión ha sido tomada debido a una reestructuración interna necesaria para la viabilidad de la empresa en el largo plazo.',

  'Conducta inapropiada': 'Lamentamos informarle que su empleo con nuestra empresa será terminado a partir del {{ fecha_despido }}. Esta decisión ha sido tomada debido a conducta inapropiada en el lugar de trabajo, que ha violado nuestras políticas internas y normas de comportamiento.',

  'Ausentismo': 'Lamentamos informarle que su empleo con nuestra empresa será terminado a partir del {{ fecha_despido }}. Esta decisión ha sido tomada debido a su ausentismo recurrente, que ha afectado negativamente la operación y eficiencia del equipo.',

  'Reducción de personal': 'Lamentamos informarle que su empleo con nuestra empresa será terminado a partir del {{ fecha_despido }}. Esta decisión ha sido tomada debido a una reducción de personal necesaria para ajustar la estructura organizacional a las nuevas condiciones del mercado.'
}

def get_motivo_despido(motivo_despido, fecha_despido):
  return motivos_despido[motivo_despido].replace('{{ fecha_despido }}', fecha_despido)