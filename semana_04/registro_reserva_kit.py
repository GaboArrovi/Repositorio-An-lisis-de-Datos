#Solución Misión Kit seguro
#Autor: Gabriel Arroyo V
#Fechas: 6/10/26
nombre = input('Nombre: ').strip().upper()
kit = input('Tipo de kit: ').strip().lower()
autorizacion = input('Tiene autorización? (si/no): ').lower().strip() == 'si'

try:
    cantidad = int(input('Ingrese la cantidad: '))
except ValueError:
    print('ERROR cantidad inválida, asignada -1')
    cantidad = -1
    
try:
    dias = int(input('Días de préstamos: '))
except ValueError:
    print('ERROR cantidad inválida, asignada -1')
    dias = -1
    
resultado = ''
if not nombre or kit == '' or cantidad < 1 or dias < 1:
    resultado = 'Registro rechazado: datos inválidos!'
elif autorizacion and cantidad <= 3 and not dias > 7:
    resultado = f'Solicitud aprobada para {nombre}: {cantidad} kit(s) de {kit}'
elif cantidad > 3 or dias > 7:
    resultado = 'Solicitud enviada a revisión'
else:
    resultado = 'Solicitud rechazada: se requiere autorización'

print(resultado)