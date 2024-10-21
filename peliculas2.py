from datetime import datetime
# No sé si es necesario importar datetime en este caso, o si ya viene importado junto con Show.
from peliculas import Show

class Cine:

    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

        self.pases = []

    def __str__(self):
        return f"El cine {self.nombre}, situado en {self.direccion}"

    def ver_cartelera (self, pase):

        for pase in self.pases:
            print(f"{pase.hora}: {pase.pelicula}")

class Pelicula(Show):

    def __init__(self, titulo, tipo="Film", terminada=False, fecha_entrada= datetime.now()):
    # No me queda claro el tema de las herencias en este caso:
    # la única singularidad de Pelicula con respecto a Show es que el tipo es fijo,
    # no sé cómo crear la clase heredera sin volver a declararla entera.
        self.titulo = titulo
        self.tipo = tipo
        self.terminada = False
        self.fecha_entrada = fecha_entrada

        self.pases_disponibles = []

    def donde_la_veo(self, pase):
        for pase in self.pases_disponibles:
            print(f"Puedes disfrutar de {self.titulo} en el cine {pase.cine} a las {pase.hora}")

class Pase:

    def __init__(self, cine, pelicula, hora):

        if not isinstance(cine, Cine):
             raise ValueError(f"El parámetro {cine} no es un cine")
        
        if not isinstance(pelicula, Pelicula):
            raise ValueError(f"El parámetro {pelicula} no es una película")
        
        self.cine = cine
        self. pelicula = pelicula
        self.hora = hora

        pelicula.pases_disponibles.append(self)
        cine.pases.append(self)
    
# Hasta aquí el ejercicio. Ahora, las comprobaciones, con una nueva función absurda
# que apenas ahorra tiempo.
def crear_de_una_vez_pelicula_cine_y_pase(titulo, nombre_cine, direccion_cine, hora_pase):

    """
    Esta función permite generar una instancia cine, una instancia película 
    y una instancia pase a la vez para ahorrar tiempo 
    a la hora de comprobar que todo va bien.
    """

    titulo = Pelicula(titulo)
    nombre_cine = Cine(nombre_cine, direccion_cine)
    pase = Pase(nombre_cine, titulo, hora_pase)

    titulo.donde_la_veo(pase)
    nombre_cine.ver_cartelera(pase)

crear_de_una_vez_pelicula_cine_y_pase("Drive", "Golem", "Calle Falsa, 123", "17.30")

