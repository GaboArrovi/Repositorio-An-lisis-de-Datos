print('ANÁLISIS DE PROMOCIÓN')

productos = [0,"Café",5000,20]

indice_productos = (productos[0])

producto = (productos[1])
print('Producto: ',producto)
precio = (productos[2])
print('Precio: ',precio)
unidades_actuales = (productos[3])
print('Unidades actuales: ',unidades_actuales)

descuento = precio * 15 / 100
promocion = precio - descuento
ingreso_actual = precio * unidades_actuales
proyeccion = (unidades_actuales * 20 / 100) + unidades_actuales
ingreso_proyectado = promocion * proyeccion
diferencia = promocion * proyeccion - ingreso_actual

if ingreso_proyectado > 0:
    resultado = 'Lanzar promo'
else:
    resultado = 'No lanzar promo'

print(f'Ingreso actual: {ingreso_actual}')
print(f'Descuento: {descuento}')
print(f'Precio promocional: {promocion}')
print(f'Unidades proyectadas (supuesto +20%): {proyeccion}')
print(f'Ingreso con promoción: {ingreso_proyectado}')
print(f'Diferencia: {diferencia}')
print('Recomendación: ',resultado)