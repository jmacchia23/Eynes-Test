'''Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
final.'''

from numpy import random

#Genero matriz 5x5 randomizada
def generar_matriz(filas,columnas):
    for x in range(filas):
        back=[]
        for x in range(columnas):
            back.append(random.randint(10))
        matriz.append(back)

    return matriz

#Recibe una matriz y verifica si existe una secuencia de 4 num consecutivos, muestra la posicion inicial y final de la secuencia
def verificar_secuencia_en_fila(matriz,traspuesto):
    i = 0
    cant_consecutivos = 0
    pos_ini = -1
    
    for fila in matriz:
        for element in fila:
            try:
                if (fila[i]+1) == fila[i+1]:
                    print(fila[i] ," y " ,fila[i+1] ," son consecutivos")
                   
                    if  pos_ini <= 0 and cant_consecutivos == 0:
                        pos_ini = fila[i]
                    consec = True
                    cant_consecutivos = cant_consecutivos + 1
                else:
                    #Reset de posicion de elementos y contadores.
                    cant_consecutivos = 0
                    consec = False
                    pos_ini = -1
                
                if cant_consecutivos >= 3 and consec:
                    #Informo pos incial y final de secuencia
                    print("encontre cuarto num consecutivos rey")

                    if traspuesto:
                        print('el elemento ', pos_ini, ' se encuentra en la posicion', '[',matriz.index(fila),',',fila.index(pos_ini), ']' )
                        print('el elemento ', fila[i+1], ' se encuentra en la posicion', '[',matriz.index(fila),',', fila.index(fila[i+1]), ']' )
                    else:
                        print('el elemento ', pos_ini, ' se encuentra en la posicion', '[',fila.index(pos_ini),',',matriz.index(fila), ']' )
                        print('el elemento ', fila[i+1], ' se encuentra en la posicion', '[',fila.index(fila[i+1]),',',matriz.index(fila), ']' )
                
                
                i = i +1
            except IndexError:
                i = 0
        #print('fila finalizada')


#traspone matriz e invoca a verificar_secuencia_en_fila
def verificar_secuencia_en_columna(matriz):
    matriz_traspuesta = []
    for x in range (len(matriz)):
        matriz_traspuesta.append([fila[x] for fila in matriz])

    verificar_secuencia_en_fila(matriz_traspuesta,False)

  