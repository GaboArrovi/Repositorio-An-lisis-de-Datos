from sedes import emprendimientos

print('Emprendimientos registrados: ',len(emprendimientos))
print('Primer emprendimiento:', emprendimientos[0]['nombre'])
print('Ventas de primer emprendimiento:', emprendimientos[0]['ventas'])

print("Análisis semanal de emprendedores")
provincias = set()

for empre in emprendimientos:
    total = sum(empre['ventas'])
    porcentaje = total / empre['meta'] * 100

    provincias.add(empre['provincia'])
    
    if porcentaje >= 100:
        estado = "Meta alcanzada"
    elif porcentaje >= 80:
        estado = "Cerca de la meta"
    else:
        estado = "Requiere atención!"
        
    print(
        f"{empre["nombre"]} | Total: ₡{total:,.2f} | "
        f"Cumplimiento: {porcentaje:.2f}% | {estado}"
    )

print("Provincias set:",provincias)