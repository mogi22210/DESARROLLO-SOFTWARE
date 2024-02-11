from medicamentos import Medicamento


class HistoriaClinica:
    def __init__(self):
        self.signos_vitales = []
        self.notas_evolucion = []
        self.imagenes_diagnosticas = []
        self.resultados_examenes = 0
        self.medicamentos_formulados = Medicamento("", 0)
        self.dia_estancia = 0

    def agregar(self, signos, nota, imagen, resultado, medicamento, dia_estancia):
        self.signos_vitales.append(signos)
        self.notas_evolucion.append(nota)
        self.imagenes_diagnosticas.append(imagen)
        self.resultados_examenes = resultado
        self.medicamentos_formulados = medicamento
        self.dia_estancia = dia_estancia


class Paciente:
    def __init__(self, documento, nombre, sexo, fecha_nacimiento, servicio, admision):
        self.documento = documento
        self.nombre = nombre
        self.sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento
        self.servicio = servicio
        self.historia_clinica = HistoriaClinica()
        self.admision = admision
