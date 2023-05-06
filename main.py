from claseConjunto import Conjunto
from menu import Menu

def test():
    A=Conjunto({1,3,5,6})
    B=Conjunto({1,2,3,4})
    print(A)
    print(B)
    menu = Menu(A, B)
    menu.ejecutar()

if __name__ == "__main__":
    test()
