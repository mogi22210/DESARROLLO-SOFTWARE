class Cama:
  def __init__(self):
      # Constructor de una cama, tiene un numero y un paciente sea relacionada a ella o no
      self.max = 300  # Tamaño maximo de camas en el hospital
      self.estado = "Disponible"
      self.paciente = None
      self.ocupacion = 0

  def asignar_paciente(self, paciente):
      self.paciente = paciente
      self.estado = "Ocupada"
      paciente.admision = True
      if self.ocupacion < self.max:
          self.ocupacion += 1

  def liberar_cama(self, paciente):
      self.paciente = None
      self.estado = "Disponible"
      paciente.admision = False
      if self.ocupacion > 0:
          self.ocupacion -= 1
