"""Caso 2: asistencia por bloques. Complete el análisis con un ciclo for."""

asistencias = [120, 180, 210, 250, 230]
capacidad = 300

# TODO: Recorra asistencias con for para acumular el total y contar los bloques
#       que SUPERAN el 70 % de la capacidad (210 no cuenta).
# TODO: Calcule el promedio y su porcentaje de ocupación.
# TODO: Clasifique el promedio: >=80 % alta; >=50 % media; si no, baja.
# TODO: Muestre total, promedio, porcentaje, cantidad de bloques y estado.
# Con los datos base: total 990, promedio 198, 66 %, 2 bloques, ocupación media.
# Prueba de código: use temporalmente cinco bloques con 240 asistentes cada uno
# para comprobar el límite del 80 %. Después restaure la lista.
total_asistencias = 0
bloques_mayores_70 = 0

limite = capacidad * 0.70

for asistencia in asistencias:
    total_asistencias += asistencia
    if asistencia > limite:
        bloques_mayores_70 += 1

asistencia_bloques = len(asistencias)
promedio_asistencia = total_asistencias / asistencia_bloques
porcentaje_ocupacion = (promedio_asistencia / capacidad) * 100

if porcentaje_ocupacion >= 80:
    clasificacion = 'Ocupación alta'
elif porcentaje_ocupacion >= 50:
    clasificacion = 'Ocupación media'
else:
    clasificacion = 'Ocupación baja'

print(f"Total de asistencias: {total_asistencias}")
print(f"Promedio de asistencia: {promedio_asistencia:.0f}")
print(f"Porcentaje de ocupación: {porcentaje_ocupacion:.0f} %")
print(f"Cantidad de bloques que superan el 70%: {bloques_mayores_70}")
print(f"Estado de ocupación: {clasificacion}")