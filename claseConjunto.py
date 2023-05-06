class Conjunto:
    def __init__(self, elementos):
        self.__elementos = set(elementos)

    def __str__(self):
        return f"{self.__elementos}"
        
    def getElemento(self):
        return self.__elementos

    def __add__(self, otro):
        return self.__elementos|otro.__elementos
    
    def __sub__(self,otro):
        return self.__elementos-otro.__elementos
    
    def __eq__(self,otro):
        return self.__elementos==otro.__elementos
