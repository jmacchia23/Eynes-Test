'''Escribir una clase en python llamada círculo que contenga un radio, con un método que
devuelva el área y otro que devuelva el perímetro del círculo.

Si se instancia la clase con radio <= 0 mostrar una excepción indicando un error amigable al
usuario e impidiendo la instanciación.

Si printeamos el objeto creado debe mostrarse una representación amigable.

El objeto debe tener su atributo radio modificable, si se le intenta setear un valor <= 0
mostrar un error y no permitir modificación.

Permitir la multiplicación del circulo: Circulo * n debe devolver un nuevo objeto con el radio
multiplicado por n. No permitir la multiplicación por números <= 0'''

from numpy import pi


class CeroError(Exception):
    def __init__(self, radio):
        if radio <= 0:
            super().__init__('El radio del círculo debe ser mayor o igual a 1')
        else:
            self.radio = radio
   

class Circulo(CeroError):

    def __init__(self,radio):
        try:
            if radio > 0:
                self.radio = radio
            else:
                raise CeroError(radio)
        except:
            print('Error: el círculo debe tener un radio mayor a 0')
  

    def __str__(self):
        return 'radio: {}'.format(self.radio)


    def calc_area(self):
        area = pi * (radio **2)
        return area


    def calc_perimetro(self):
        
        perim = 2 * pi * radio
    

    def set_radio(self,radio):
        try:
            if radio > 0:
                self.radio = radio
            else:
                raise CeroError(radio)
        except:    
            print('Error: el círculo debe tener un radio mayor a 0')


    def multiplicación(self,num):
        try:
            if num >0:
                mult = self.radio * num
                nuevocirculo = Circulo(mult)
                return nuevocirculo
            else:
                raise CeroError(num)
        except:
            print('Error: no es posible crear un nuevo círculo al multiplicar el radio actual por 0')
 


