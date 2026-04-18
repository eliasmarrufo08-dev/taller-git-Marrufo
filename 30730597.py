#introduccion de datos y validacion paso a paso
tipoMoneda = int(input("seleccione tipo de moneda 1 BS/ 2 $"))
limiteDiario = 0

#antes usaba "if" pero preferí cambiar a while, para evitar capa 8...
while True:
   if tipoMoneda == 1:
      limiteDiario = 10000
      break
   elif tipoMoneda == 2:
      limiteDiario = 500
      break
   else:
      print("tipo de moneda no valido intente denuevo")
      tipoMoneda = int(input("seleccione tipo de moneda 1 BS/ 2 $"))

montoOriginal = int(input("introduzca monto a retirar"))

if montoOriginal % 10 != 0:
   print("Error: Monto no compatible con las denominaciones disponibles")
   exit()
elif montoOriginal > limiteDiario:
   print("Cantidad excede limite diario")
   exit()

tipoCuenta = int(input("introduzca tipo de cuenta 1 Ahorro / 2 Corriente"))

#calculo

monto = montoOriginal

while True:
   if tipoCuenta == 1:
      break
   elif tipoCuenta == 2:
      break
   else:
      print("introduzca un tipo de cuenta valido")
      tipoCuenta = int(input("introduzca tipo de cuenta 1 Ahorro / 2 Corriente"))

if tipoCuenta == 2:
   comision = montoOriginal * 0.05
else:
   comision = 0

#Desglose de billetes

billete100 = monto // 100
monto = monto % 100 
billete50 = monto // 50
monto = monto % 50
billete20 = monto // 20
monto = monto % 20
billete10 = monto // 10
monto = monto % 10

#salida de datos

totalFinal = montoOriginal + comision

match tipoMoneda:
   case 1:
      etiqueta = "Bs."
   case 2:
      etiqueta = "$"

#antes usaba este metodo para no mostrar 0 en caso de no entregarse una denominacion
#if billete100 > 0:
   #print(f"billetes de 100 entregados: {billete100}" )
#if billete50 > 0:
   #print(f"billetes de 50 entregados: {billete50}")
#if billete20 > 0:
   #print(f"billetes de 20 entregados: {billete20}")
#if billete10 > 0:
   #print(f"billetes de 10 entregados: {billete10}")

print(f"billetes de 100: {billete100}")
print(f"billetes de 50: {billete50}")
print(f"billetes de 20: {billete20}")
print(f"billetes de 10: {billete10}")
print(f"Total debitado: {totalFinal} {etiqueta}")