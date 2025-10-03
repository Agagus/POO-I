

class Material():
    def __init__(self, titulo, autor, anio):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def autor(self):
        return self.__autor
    
    @property
    def anio(self):
        return self.__anio
    
    def __eq__(self, other):
        if isinstance(other, Material):
            return self.titulo == other.titulo
        return False
    
    def __str__(self):
        return f"Titulo: {self.titulo}\nAutor: {self.autor}\nAño: {self.anio}\n"
    
class Libro(Material):
    def __init__(self, titulo, autor, anio, genero):
        super().__init__(titulo, autor, anio)
        self.__genero = genero

    def __str__(self):
        return super().__str__() + f"Género: {self.__genero}"

class Revista(Material):
    def __init__(self, titulo, autor, anio, numero_edicion):
        super().__init__(titulo, autor, anio)
        self.__numero_edicion = numero_edicion

    def __str__(self):
        return super().__str__() + f"Edición: {self.__numero_edicion}"

class DVD(Material):
    def __init__(self, titulo, autor, anio, duracion):
        super().__init__(titulo, autor, anio)
        self.__duracion = duracion

    def __str__(self):
        return super().__str__() + f"Duracion: {self.__duracion}"


class Usuario():
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__materiales_prestados = []

    @property
    def materiales_prestados(self):
        return self.__materiales_prestados

    def prestar_material(self, material):
        self.__materiales_prestados.append(material)

    def devolver_material(self, material):
        for i in self.__materiales_prestados:
            if i.__eq__(material):
                self.__materiales_prestados.remove(i)
                return
        return "El material no pertenece al usuario"

    def listar_materiales(self):
        for i in self.__materiales_prestados:
            print(i)


libro1 = Libro("100 años de soledad", "Marquez", 1960, "drama")
#print(libro1)

revista1 = Revista("Gente", "Gente y cia", 2025, 2563)
#print(revista1)

dvd1 = DVD("Bichos", "Disney", 1993, 130)
#print(dvd1)

usuario1 = Usuario("Agus")
usuario1.prestar_material(libro1)
usuario1.prestar_material(revista1)
usuario1.prestar_material(dvd1)
print("--------------------")
usuario1.devolver_material(dvd1)
usuario1.listar_materiales()


def mostrar_informacion(material):
    print(material)

print("--------------------------------")
mostrar_informacion(revista1)