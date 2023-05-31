class Inmueble:
   def __init__(self, metros_cuadrados='', habitaciones='', bans='', **kwargs):
      super().__init__(**kwargs)
      self.metros_cuadrados = metros_cuadrados
      self.num_habitaciones = habitaciones
      self.num_bans = bans

   def mostrar(self):
      print("Detalles")
      print("======")
      print("metros cuadrados: {}".format(self.metros_cuadrados))
      print("habitaciones: {}".format(self.num_habitaciones))
      print("bans: {}".format(self.num_bans))

   def prompt_init():
      return dict(  metros_cuadrados=input("Escribe los metros cuadrados: "),
                habitaciones=input("Escribe la cantidad de habitaciones: "),
                bans=input("Escribe el numero de banos: "))
   prompt_init = staticmethod(prompt_init)

def obtener_input_valido(string_input, opciones_validas):
   string_input += " ({}) ".format((", ".join(opciones_validas)))
   respuesta = input(string_input)
   while respuesta.lower() not in opciones_validas:
      respuesta = input(string_input)
   return respuesta

class Apartamento(Inmueble):
   lavanderias_validas = ("moneda", "incluido", "ningna")
   balcones_validos = ("si", "no", "solario")

   def __init__(self, balcon='', lavanderia='', **kwargs):
      super().__init__(**kwargs)
      self.balcon = balcon
      self.lavanderia = lavanderia

   def mostrar(self):
      super().mostrar()
      print("Detalles Apartamento")
      print("lavanderia: {}".format(self.lavanderia))
      print("tiene balcon: {}".format(self.balcon))

   def prompt_init():
      parent_init = input.prompt_init()
      lavanderia = obtener_input_valido(
         "Que sistema de lavanderia tiene el inmueble? ", 
         Apartamento.lavanderias_validas )
      balcon = obtener_input_valido(
         "Tiene balcon el inmueble? ", 
         Apartamento.balcones_validos )
      parent_init.update({
         "lavanderia": lavanderia,
         "balcon": balcon
         })
      return parent_init
   prompt_init = staticmethod(prompt_init)

class Casa(Inmueble):
   garaje_valido = ("anexo", "separado", "ninguno")
   jardin_valido = ("si", "no")

   def __init__(self, num_pisos='', garaje='', jardin='', **kwargs):
      super().__init__(**kwargs)
      self.garaje = garaje
      self.jardin = jardin
      self.num_pisos = num_pisos

   def mostar(self):
      super().mostrar()
      print("Detalle Casa")
      print("# de pisos: {}".format(self.num_pisos))
      print("garaje: {}".format(self.garaje))
      print("jardin: {}".format(self.jardin))

   def prompt_init():
      parent_init = Inmueble.prompt_init()
      jardin = obtener_input_valido("La casa tiene jardin? ",
         Casa.jardin_valido)
      garaje = obtener_input_valido("Hay garaje? ",
         Casa.garaje_valido)
      num_pisos = input("Cuantos pisos? ")

      parent_init.update({
         "jardin": jardin,
         "garaje": garaje,
         "num_pisos": num_pisos
         })
      return parent_init
   prompt_init = staticmethod(prompt_init)

class Compra:
    def __init__(self, precio='', impuestos='', **kwargs):
        super().__init__(**kwargs)
        self.precio = precio
        self.impuestos = impuestos

    def mostrar(self):
        super().mostrar() 
        print("Detalle Compra")
        print("pecio venta: {}".format(self.precio))
        print("impuestos estimados: {}".format(self.impuestos))

    def prompt_init():
        return dict(
            precio = input("Cual es el precio de la venta? "),
            impuestos = input("Cuales son los impuestos estimados? "))
    prompt_init = staticmethod(prompt_init)

class Alquiler:
    def __init__(self, amueblado='', ajuar='', alquiler='', **kwargs):
        super().__init__(**kwargs)
        self.amueblado = amueblado
        self.alquiler = alquiler
        self.ajuar = ajuar

    def mostrar(self):
        super().mostrar()
        print("Detalles")
        print("Alquiler: {}".format(self.alquiler))
        print("ajuar estimado: {}".format(
            self.ajuar))
        print("amueblado: {}".format(self.amueblado))

    def prompt_init():
        return dict(
            alquiler = input("Cual es el alquiler mensual? "),
            ajuar=input("Cual es el ajuar estimado? "),
            amueblado = obtener_input_valido(
                "Esta amueblado el inmueble? ", ("si","no")))
    prompt_init = staticmethod(prompt_init)

class CasaAlquiler(Alquiler, Casa):
    def prompt_init():
        init = Casa.prompt_init()
        init.update(Alquiler.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class ApartamentoAlquiler(Alquiler, Apartamento):
    def prompt_init():
        init = Apartamento.prompt_init()
        init.update(Alquiler.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class ApartamentoCompra(Compra, Apartamento):
    def prompt_init():
        init = Apartamento.prompt_init()
        init.update(Compra.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class CasaCompra(Compra, Casa):
    def prompt_init():
        init = Casa.prompt_init()
        init.update(Compra.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)
    
class Agente:
    type_map = {
        ("casa","alquiler"): CasaAlquiler,
        ("casa","compra"): CasaCompra,
        ("apartamento","alquiler"): ApartamentoAlquiler,
        ("apartamento","compra"): ApartamentoCompra
        }
    def __init__(self):
        self.inmueble_list = []

    def mostrar_inmuebles(self):
        for inmueble in self.inmueble_list:
            inmueble.mostrar()

    def add_inmueble(self):
        tipo_inmueble = obtener_input_valido("Que tipo de inmueble? ", ("casa","apartamento")).lower()
        tipo_pago = obtener_input_valido("Que tipo de pago?" ,("compra","alquiler")).lower()

        inmuebleClass = self.type_map[(tipo_inmueble, tipo_pago)]
        init_args = inmuebleClass.prompt_init()
        self.inmueble_list.append(inmuebleClass(**init_args))

