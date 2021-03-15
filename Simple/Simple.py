'''Hacer una función que genere una lista de diccionarios que contengan id y edad, donde
edad sea un número aleatorio entre 1 y 100 y la longitud de la lista sea de 10
elementos. retornar la lista.
Hacer otra función que reciba lo generado en la primer función y ordenarlo de mayor a
menor. Printear el id de la persona más joven y más vieja. Devolver la lista ordenada.'''

from numpy import random

#Genera y retorna lista de 10 diccionarios que contienen id y edad aleatoria entre 1 y 100 
def gen_lista_dicc():
   
    lista_diccionarios = []
    
    for x in range(10):

        age = random.randint(1,100)
        dicc = {'id': x, 'edad': age}
        lista_diccionarios.append(dicc)
    print(lista_diccionarios)
    return(lista_diccionarios)


#Recibe la lista retornada por gen_lista_dicc y la ordena de mayor a menor
def sort_lista_dicc(lista_diccionarios):

    lista_diccionarios.sort(key = lambda edad: edad['edad'], reverse= True)
    print('id de la persona más joven ', lista_diccionarios[-1]['id'])
    print('id de la persona más vieja ', lista_diccionarios[0]['id'])

    return lista_diccionarios

