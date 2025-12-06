# Técnicas de programación POO, astracción, encapsulación, herencia, polimorfismo

# Venta de ropa por catálogo

from abc import ABC, abstractmethod

# -------------------------------
# 1. ABSTRACCIÓN: clase astracta ProdoctoRopa define características fundamentales
#    como nombre, precio.
# -------------------------------
class ProductoRopa(ABC):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def descripcion(self):       # Método astracción se debe implementar en las clases hijas
        pass


# -------------------------------
# 2. ENCAPSULACIÓN : atributos privados y métodos
#     especiales para acceder a ellos de forma controlada.
# -------------------------------
class Camiseta:
    def __init__(self, nombre, precio):
        self.__nombre = nombre       # atributo privado
        self.__precio = precio       # atributo privado

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def set_precio(self, nuevo):
        if nuevo > 0:
            self.__precio = nuevo


# -------------------------------
# 3. HERENCIA: clase hija que hereda de ProductoRopa
# -------------------------------
class Pantalon(ProductoRopa): # Representa un pantalón en el catálogo
    def descripcion(self):
        return f"Pantalón: {self.nombre}"


class Blusa(ProductoRopa): # Representa una blusa en el catálogo
    def descripcion(self):
        return f"Blusa: {self.nombre}"


# -------------------------------
# 4. POLIMORFISMO : recibe cualquier objeto que derive
#     de ProductoRopa y ejecuta sus métodos característicos.
# -------------------------------
def mostrar(producto):
    return f"{producto.descripcion()} - Precio: {producto.precio}"


# -------------------------------
# PROGRAMA PRINCIPAL CATÁLOGO DE ROPA
# -------------------------------
if __name__ == "__main__":

    print("=== RESULTADOS DEL PROGRAMA ROPA POR CATÁLOGO ===\n")

    # Abstracción
    print("1) ABSTRACCIÓN:")
    print("Se usa la clase abstracta 'ProductoRopa' que define")
    print("los atributos y un método abstracto 'descripcion()'.\n")

    # Encapsulación
    print("2) ENCAPSULACIÓN:")
    c = Camiseta("Camiseta Negra", 10.00)
    print("Nombre (privado):", c.get_nombre())
    print("Precio (privado):", c.get_precio(), "\n")

    # Herencia
    print("3) HERENCIA:")
    p = Pantalon("Jeans Azul", 20.00)
    b = Blusa("Blusa Roja", 10.00)
    print("Pantalón y Blusa heredan de ProductoRopa.\n")

    # Polimorfismo
    print("4) POLIMORFISMO:")
    print(mostrar(p))
    print(mostrar(b))

