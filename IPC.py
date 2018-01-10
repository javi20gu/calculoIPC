import matplotlib.pyplot as plt

def calcular(*args):
    global n_porcentaje
    if len(args[0]) == 12 and len(n_porcentaje) == 4:
        calculos1 = (n_porcentaje[0] * (datos_tabla[4]/datos_tabla[0])) + (n_porcentaje[1] * (datos_tabla[5] / datos_tabla[1])) + (n_porcentaje[2] * (datos_tabla[6]/datos_tabla[2])) + (n_porcentaje[3] * (datos_tabla[7]/datos_tabla[3]))
        calculos2 = (n_porcentaje[0] * (datos_tabla[8]/datos_tabla[0])) + (n_porcentaje[1] * (datos_tabla[9]/datos_tabla[1])) + (n_porcentaje[2] * (datos_tabla[10]/datos_tabla[2])) + (n_porcentaje[3] * (datos_tabla[11]/datos_tabla[3]))
    elif len(args[0]) == 9 and len(n_porcentaje) == 3:
        calculos1 = (n_porcentaje[0] * (datos_tabla[3]/datos_tabla[0])) + (n_porcentaje[1] * (datos_tabla[4] / datos_tabla[1])) + (n_porcentaje[2] * (datos_tabla[5]/datos_tabla[2]))
        calculos2 = (n_porcentaje[0] * (datos_tabla[6]/datos_tabla[0])) + (n_porcentaje[1] * (datos_tabla[7]/datos_tabla[1])) + (n_porcentaje[2] * (datos_tabla[8]/datos_tabla[2]))
    elif len(args[0]) == 6 and len(n_porcentaje) == 2:
        calculos1 = (n_porcentaje[0] * (datos_tabla[2]/datos_tabla[0])) + (n_porcentaje[1] * (datos_tabla[3] / datos_tabla[1]))
        calculos2 = (n_porcentaje[0] * (datos_tabla[4]/datos_tabla[0])) + (n_porcentaje[1] * (datos_tabla[5]/datos_tabla[1]))
    else:
        print("Error Comprueba los argumentos.")
    return calculos1,calculos2

numero_bienes = eval(input("Introduce el numero de Bienes: "))
datos_bienes = []
datos_anos = []
tabla = []
datos = []
X = [1,2]
Y1 = []
Y2 = []
datos_tabla = []
n_porcentaje = []

for i in range(numero_bienes):
    print(f"\tBien Numero: {i+1}")
    bienes = i + 1
    datos_bienes.append(bienes)

numero_anos = eval(input("Introduce el numero de Años: "))
for i in range(numero_anos+1):
    print(f"\tAño Numero: {i}")
    anos = i
    datos_anos.append(anos)
tabla = [datos_anos, datos_bienes]

n_porcentaje = eval(input('Introduce los porcentajes seguidos: '))

for i in range(len(datos_anos)):
    for a in range(len(datos_bienes)):
        datos = eval(input(f'Introduce el dato para el año: {i} en el bien {a+1}: '))
        datos_tabla.append(datos)

calculos1, calculos2 = calcular(datos_tabla)

Y1.append(100)
Y2.append(100)
Y1.append(calculos1)
Y2.append(calculos2)
total = []
total.append(Y1[1])
total.append(Y2[1])

plt.suptitle("Evolución del IPC",fontsize=26)
plt.subplot2grid((2,2),(0,0),rowspan=2)
plt.title("Total del IPC", fontsize=18)
plt.xlabel("Numero de Años")
plt.ylabel("Valor del IPC ")
plt.plot(X,total)

plt.subplot2grid((2,2),(0,1))
plt.title("IPC del Año 1", fontsize=15)
plt.xlabel("Numero de Años")
plt.ylabel("Valor del IPC ")
plt.plot(X,Y2)

plt.subplot2grid((2,2),(1,1))
plt.title("IPC del Año 2", fontsize=15)
plt.xlabel("Numero de Años")
plt.ylabel("Valor del IPC ")
plt.plot(X,Y1)
plt.show()