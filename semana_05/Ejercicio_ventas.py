ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]
meta_centro = 640000
meta_norte = 700000

total_centro = sum(ventas_centro)
cantidad_centro = len(ventas_centro)
print(cantidad_centro)

promedio_centro = total_centro / cantidad_centro
print(promedio_centro)

menor_centro = min(ventas_centro)
mayor_centro = max(ventas_centro)

porcentaje_logro_centro = total_centro * 100 / meta_centro
print(total_centro)
print(porcentaje_logro_centro)

total_norte = sum(ventas_norte)
cantidad_norte = len(ventas_norte)
print(cantidad_norte)

promedio_norte = total_norte / cantidad_norte
print(promedio_norte)

menor_norte = min(ventas_norte)
mayor_norte = max(ventas_norte)

porcentaje_logro_norte = total_norte * 100 / meta_norte
print(total_norte)
print(porcentaje_logro_norte)

# comparación de tiendas
if total_centro > meta_centro:
    estado_centro = 'meta superada'
elif total_centro == meta_centro:
    estado_centro = 'meta lograda'
else:
    estado_centro = 'Meta NO LOGRADA'
print(estado_centro)

if total_norte > meta_norte:
    estado_norte = 'meta superada'
elif total_norte == meta_norte:
    estado_norte = 'meta lograda'
else:
    estado_norte = 'Meta NO LOGRADA'
print(estado_norte)

# Resultados:
if total_centro < total_norte:
    tienda_mayor_ventas = 'Tienda de Centro'
elif total_norte > total_centro:
    tienda_mayor_ventas = 'Tienda del Norte'
else:
    tienda_mayor_ventas = 'Mismo total'
    
print('COMPARACIÓN SEMANAL DE TIENDAS')
print(f"Centro - total ₡{total_centro:,.2f} | Meta ₡{meta_centro:,.2f} | cumplimiento {porcentaje_logro_centro:,.0f}%")
print(f'Centro logro: {estado_centro}\n')
print(f"Norte - total ₡{total_norte:,.2f} | Meta ₡{meta_norte:,.2f} | cumplimiento {porcentaje_logro_norte:,.0f}%")
print(f'Centro logro: {estado_norte}\n')

print('Tienda con mayor ventas:',tienda_mayor_ventas)

#Conclusiones:
#La tienda del norte fue la que vendió más
#Precisamente fue la tienda del norte la que logró alcanzar y superar la meta, a diferencia de la del centro (la cual no alcanzó la meta)
#Podríamos decir que fue la tienda del centro la que tuvo más variación, teniendo 28000 colones de diferencia (cuando la del norte presenta 25000)