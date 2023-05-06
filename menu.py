from claseConjunto import Conjunto

class Menu:
    __switcher=None
    __A={}
    __B={}
    def __init__(self, A, B):
        self.__A = A
        self.__B = B
        self.__switcher = {
            1: self.opcion1,
            2: self.opcion2,
            3: self.opcion3,
            4: self.opcion4
        }

    def opcion1(self):
        print("Unión de conjuntos.")
        union=self.__A+self.__B
        print("La unión de", self.__A, "y", self.__B, "es", union)

    def opcion2(self):
        print("Diferencia de conjuntos")
        diferencia = self.__A-self.__B
        print("La diferencia de", self.__A, "y", self.__B, "es", diferencia)

    def opcion3(self):
        print("Verificación de igualdad de conjuntos")
        if self.__A == self.__B:
            print(f"Los conjuntos {self.__A} y {self.__B} son iguales")
        else:
            print(f"Los conjuntos {self.__A} y {self.__B} no son iguales")

    def opcion4(self):
        print("Saliendo del programa...")

    def ejecutar(self):
        while True:
            print("Bienvenido al menú de opciones")
            print("1. Unión de conjuntos.")
            print("2. Diferencia de conjuntos.")
            print("3. Verificación de igualdad de conjuntos.")
            print("4. Salir")
            opcion = int(input("Ingrese una Opcion: "))

            # Utilizamos el switcher para llamar a la función correspondiente a la opción seleccionada
            func = self.__switcher.get(opcion, lambda: print("Opción no válida"))
            if func:
                func()
            else: 
                func()
            if 4==opcion:
                break
            

            
