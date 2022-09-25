#uso de objetos namedtuple
#importando modulo collections
import collections

def main():
    #Crie uma namedtuple para armazenar coordenadas
    #cardinalidade

    coordenadas = collections.namedtuple("Coordenadas","x y")

    p1=coordenadas(10,20)
    p2= coordenadas(30,40)
    print(p1, p2)
    print(p1.x,p1.y)
    #Use _replace() para criar uma instancia nova
    p1 = p1._replace(x=100)
    print(p1)


main()