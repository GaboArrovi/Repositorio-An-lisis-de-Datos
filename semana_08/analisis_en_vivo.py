"""Semana 8: la red hospitalaria nos contrata como analistas de datos.

Construimos el informe debajo de este inicio con GUIA_ESTUDIANTE.md.
Leemos la fuente preparada en fuente.py y contamos las menciones recibidas.
"""

from fuente import cargar_datos


USAR_RESPALDO = False  # Lo cambiamos solo si recibimos copias actualizadas.
registros, equivalencias, origen = cargar_datos(USAR_RESPALDO)
print("Fuente:", origen)
print("Registros recibidos:", len(registros))
print("Equivalencias publicadas:", len(equivalencias))

#Fase 1: contar medicamentos
conteo_medicamentos = {}
conteo_recetas = 0

#Fase 2: limpieza de datos
equivalencias = {
    "acetaminofén": "acetaminofen",
    "paracetamol": "acetaminofen",
    "antiácido": "antiacido",
    "losartán": "losartan"
}

for registro in registros:
    for medicamento in registro['medicamentos']:
        nombre = medicamento.strip().lower()
        #aplicación de fase 2
        if nombre in equivalencias:
            nombre = equivalencias[nombre]
        
        if nombre in conteo_medicamentos:
            conteo_medicamentos[nombre] += 1
        else:
            conteo_medicamentos[nombre] = 1
        conteo_recetas += 1


print("\n-------- CONTEO DE MEDICAMENTOS ---------")
print("Total de recetas:", conteo_recetas)
print(conteo_medicamentos)
for medicamento, cantidad in conteo_medicamentos.items():
    print(f"- {medicamento}: {cantidad}")

#Cuántos pacientes atendió cada sede:
conteo_hospital = {}
total_pacientes = 0

for registro in registros:
    hospital = registro['hospital']
    if hospital not in conteo_hospital:
        conteo_hospital[hospital] = 0
    conteo_hospital[hospital] += 1
print("\nAtenciones por hospital")
for hospital, cantidad in conteo_hospital.items():
    print("-", hospital,":", cantidad)