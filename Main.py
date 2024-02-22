from multipledispatch import dispatch

#*args
def calcularPromedio(*args):
    if (len(args) == 1):
        return args
    elif (len(args) == 2):
        return (args[0] + args[1])/2
    elif (len(args) == 3):
        return (args[0] + args[1] + args[2])/3
    elif (len(args) == 4):
        return (args[0] + args[1] + args[2] + args[3])/4
    else:
        return "Se ha Excedido el Número de Argumentos que Soporta el Método"
    
    #Forma Fácil
    #if (len(args) != 0:):
        #return sum(args)/len(args)

#isinstance
def multiplicar(a,b):
    if isinstance (a, int) and isinstance (b, int):
        return a * b
    elif isinstance (a, float) and isinstance (b, float):
        return a * b
    elif isinstance (a, str) and isinstance (b, int):
        texto = ""
        for i in range (b):
            texto += a
        return texto
    elif isinstance (a, int) and isinstance (b, str):
        texto = ""
        for i in range (a):
            texto += b
        return texto
    else:
        return "Error, los Parámetros son Incorrectos"
    
#multiple dispatch
@dispatch(list, int)
def agregarElemento(lista, a):
    lista.append(a)
    return lista

@dispatch(list, int, bool)
def agregarElemento(lista, a, ubicacion):
    nuevaLista = []
    if(ubicacion == True):
        nuevaLista.append(a)
        for elemento in lista:
            nuevaLista.append(elemento)
        return nuevaLista

    
class Main():
    def main():
        lista = [1, 2, 3]
        opcion = 999

        while(opcion != 0):
            opcion = int(input("MENÚ PRINCIPAL\n1. Calcular Promedio Multiples Números\n2. Multiplicar Números y Texto\n3. Agregar Elementos (Inicio - Fin) a una Lista\n0. Salir\n-->"))
            if(opcion == 1):
                promedio1 = calcularPromedio(5)
                print("El promedio es: {}".format(promedio1))
                promedio2 = calcularPromedio(3,6)
                print("El promedio es: {}".format(promedio2))
                promedio3 = calcularPromedio(3,6,9)
                print("El promedio es: {}".format(promedio3))
                promedio4 = calcularPromedio(3,6,9,12)
                print("El promedio es: {}".format(promedio4))
                promedioError = calcularPromedio(3,6,9,12,15)
                print("El promedio es: {}".format(promedioError))

            elif(opcion == 2):
                multiplicacion1 = multiplicar(2,5)
                print("La multiplicación es: {}".format(multiplicacion1))
                multiplicacion2 = multiplicar(2.5,4.0)
                print("La multiplicación es: {}".format(multiplicacion2))
                multiplicacion3 = multiplicar("Hola", 3)
                print("La multiplicación es: {}".format(multiplicacion3))
                multiplicacion4 = multiplicar(4, "Hola")
                print("La multiplicación es: {}".format(multiplicacion4))
                multiplicacionError = multiplicar("Hola", "Mundo")
                print("La multiplicación es: {}".format(multiplicacionError))

            elif (opcion == 3):
                print(lista)
                print(agregarElemento(lista, 4))
                print(agregarElemento(lista, 5, True))

            elif (opcion == 0):
                print("Saliendo del Programa...")

            else:
                print("Opción no Válida, Intente de Nuevo.")


    main()