from datetime import datetime

class Show:

    def __init__(self, titulo, tipo, terminada = False, fecha_entrada=datetime.now()):

        self.titulo = titulo
        self.tipo = tipo
        self.terminada = terminada
        self.fecha = fecha_entrada

    def __str__(self):
        return f"La película {self.titulo}"

mis_pelis = []

# Realmente, el ejercicio llega hasta aquí, muy pobre e incompleto 
# (como digo en el siguiente comentario, no queda resuelto el problema de marcar un película como terminada); 
# lo que viene a continuación es una función, tal vez absurda,
# para crear objetos película y agregarlos directamente a la lista.

def crear_pelicula_y_agregar_a_lista(titulo, tipo_de_show, lista_destino, terminada = False):

  """
  Crea objetos de la clase Película y los envía directamente a la lista de destino elegida.
  Para generar dichos objetos, recibe los atributos necesarios para la creación de la instancia,
  así como la lista destino donde se almacenarán.
  """

  if type(titulo) is not str:

    raise TypeError("Este programa solo acepta cadenas de palabras.")
 
  else:

    titulo = Show(titulo, tipo_de_show, terminada)

  lista_destino.append(titulo)

crear_pelicula_y_agregar_a_lista("Star Wars", "Película", mis_pelis)
crear_pelicula_y_agregar_a_lista("The Wire", "Serie", mis_pelis, terminada = True ) 
# Como decía antes, en realidad, no he solucionado que "The Wire" sea marcada como terminada;
# la solución que Claudia enseñó en la clase del sábado, 
# en la que define un método que marque una película como terminada en la creación de la clase es perfecta, 
# pero no quise incluir dicha idea en mi código porque no la considero como propia.
crear_pelicula_y_agregar_a_lista("Mulholland Drive", "Película", mis_pelis)
crear_pelicula_y_agregar_a_lista("Woodworm", "Documental", mis_pelis)

for i in mis_pelis:

    print(f'Titulo: {i.titulo} \t Tipo: {i.tipo} \t ¿Está terminada? {i.terminada} \t Fecha: {i.fecha}')