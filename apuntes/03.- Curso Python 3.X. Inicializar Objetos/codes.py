class Punto:
   'Representa coordenadas geometricas bidimensionales'
   def __init__(self, x=0, y=0):
      '''Inicializa la posicion de un nuevo punto. Las coordenadas x e y pueden ser especificadas. Si no lo son, el punto por defecto sera el de origen'''
      self.mover(x,y)
   def mover(self, x, y):
      "Reinicia el punto al origen geometrico: 0,0"
      self.x = x
      self.y = y
   def calcular_distancia(self, otro_punto):
      """Calcula la distancia desde este punto a un segundo punto pasado como parametro. La distancia devuelve un float"""
      return math.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)  

punto1 = Punto()
print( punto1.x, punto1.y ) # imprime 0 0

punto2 = Punto(4)
print( punto2.x, punto2.y ) # imprime 4 0

punto3 = Punto(0, 4)
print( punto3.x, punto3.y ) # imprime 0 4