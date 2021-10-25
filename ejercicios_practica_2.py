# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    #archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    csvfile = open('stock.csv')
    stock = list(csv.DictReader(csvfile))
    print(stock)  
    
    total = 0  
    for x in range(len(stock)):
        total += int(stock[x]["tornillos"])

    print("el total de tornillos es:",total)

def ej4():
    print('Ejercicios con archivos CSV 2º')
    #archivo = open('propiedades.csv',"r")
    propiedades = list(csv.DictReader(open("propiedades.csv")))
    print(propiedades)

    cantidad_2 = 0
    cantidad_3 = 0
    sin_datos = 0
    
    print(len(propiedades))
   

    """
    # opcion mas corta... 
    
    for x in range(len(propiedades)):
            if propiedades[x]["ambientes"] == "2":
                cantidad_2 += 1
            elif propiedades[x]["ambientes"] == "3":
                cantidad_3 += 1"""
                
    for x in range(len(propiedades)):
        try:
            if int(propiedades[x]["ambientes"]) == 2:
                cantidad_2 +=1
            elif int(propiedades[x]["ambientes"]) == 3:
                cantidad_3 +=1
        except:
            sin_datos += 1
    
    print("La cantidad de dptos de 2 ambientes es:", cantidad_2)
    print("La cantidad de dptos de 3 ambientes es:", cantidad_3)
    print("La cantidad de dptos sin datos es:", sin_datos)
      
    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
