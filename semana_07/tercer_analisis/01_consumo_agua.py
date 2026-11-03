"""Caso 1: cambio del consumo diario de agua. Complete el programa."""

consumos_litros = [120, 115, 108, 102, 96]

# TODO: Calcule el consumo total y el promedio diario.
# TODO: Compare el primer día con el último: litros ahorrados y porcentaje
#       de reducción respecto al primer día.
# TODO: Clasifique: >=15 % reducción alta; >0 % reducción moderada;
#       de lo contrario, sin reducción.
# TODO: Muestre los cinco resultados.
# Control: total 541 L; promedio 108,2 L; ahorro 24 L; reducción 20 %;
#          reducción alta.
# Prueba: use temporalmente cinco consumos iguales. Debe indicar 0 % y
# "Sin reducción". Restaure la lista antes de entregar.
consumo_total = sum(consumos_litros)
promedio_diario = consumo_total / len(consumos_litros)

primer_dia = consumos_litros[0]
ultimo_dia = consumos_litros[-1]

litros_ahorrados = primer_dia - ultimo_dia
porcentaje_reduccion = (litros_ahorrados - primer_dia) / 100

if porcentaje_reduccion >= 15:
    resultado = 'Reducción alta'
elif porcentaje_reduccion > 0:
    resultado = 'Reducción moderada'
else:
    resultado = 'Sin reducción'

print(f'Consumo total: {consumo_total} L')
print(f'Promedio diario: {promedio_diario} L')
print(f'Litro ahorrados: {litros_ahorrados} L')
print(f'Porcentaje de reducción: {porcentaje_reduccion} %')
print(f'Clasificación: {resultado}')