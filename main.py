#Miguel Cuentas - T00067657
from historia_clinica import Paciente
from cama import Cama
from medicamentos import Medicamento

pacientes = []
camas = []

while True:
  print("\033[1m---------------------------------------\033[0m")
  print("\033[1mBienvenido!\033[0m")
  print("1. Ingresar paciente")
  print("2. Gestionar historia clínica electrónica de un paciente")
  print("3. Generar reportes de indicadores")
  print("4. Salir")
  print("\033[1m---------------------------------------\033[0m")
  opcion = int(input("\nIngrese el número de la opción deseada: "))

  if opcion == 1:
    documento = int(input("\nIngrese su documento de identidad: "))
    nombre = input("Ingrese su nombre: ")
    sexo = input("Ingrese su sexo: ")
    fecha_nacimiento = input("Ingrese su fecha de nacimiento: ")

    print("\033[1mDatos personales introducidos!\033[0m")
    signos_vitales = input("\nAhora bien. Ingrese sus signos vitales: ")
    nota_evolucion = input("Ingrese la nota de evolución: ")
    imagenes_diagnosticas = input("Ingrese las imágenes diagnósticas: ")

    print("\033[1m\nRESULTADO EXAMENES\033[0m")
    print("1. Enfermedad Cronica")
    print("2. Enfermedad Preventiva")
    print("3. Enfermedad no grave")
    resultados_exam = int(input("Ingrese los resultados de sus exámenes: "))
    while resultados_exam < 1 or resultados_exam > 3:
      print("\nIngrese una opción válida por favor")
      resultados_exam = int(input("Ingrese los resultados de sus exámenes: "))

    nombre_med = input("\nIngrese el nombre de los medicamentos formulados: ")
    dosis_med = input("Ingrese la dosis de los medicamentos formulados: ")
    medicamento = Medicamento(nombre_med, dosis_med)

    print("\033[1m\nSERVICIOS\033[0m")
    print("1. Psiquiatría")
    print("2. Cardiología")
    print("3. Dermatología")
    print("4. Ginecología")
    print("5. Odontología")
    print("6. Pediatría")
    print("7. Traumatología")
    print("8. Urología")
    print("9. Otra")
    servicio = int(input("Ingrese el número de la opción deseada: "))
    while servicio < 1 or servicio > 9:
      servicio = int(input("\nIngrese el número de la opción deseada: "))
    dia_estancia = int(input("Ingrese los días de estancia del paciente: "))

    admision = True
    paciente = Paciente(documento, nombre, sexo, fecha_nacimiento, servicio,
                        admision)
    paciente.historia_clinica.agregar(signos_vitales, nota_evolucion,
                                      imagenes_diagnosticas, resultados_exam,
                                      medicamento, dia_estancia)
    pacientes.append(paciente)

    if len(camas) < 300:
      nueva_cama = Cama()
      nueva_cama.asignar_paciente(paciente)
      camas.append(nueva_cama)
      print("\nHistoria clínica ingresada exitosamente.")
    else:
      print("\nNo hay camas disponibles. El paciente no puede ser admitido.")

  elif opcion == 2:
    documento = int(
        input("\nIngrese el documento de identidad del paciente: "))
    for paciente in pacientes:
      if paciente.documento == documento:
        print("\033[1m\n¿Qué desea cambiar del paciente:\033[0m",
              paciente.nombre)
        print("1. Signos vitales")
        print("2. Nota de evolución")
        print("3. Imágenes diagnósticas")
        print("4. Resultados de exámenes")
        print("5. Medicamentos formulados")
        print("6. Dar de alta")
        opcion = int(input("Ingrese el número de la opción deseada: "))
        while opcion < 1 or opcion > 6:
          print("\nOpción inválida.")
          opcion = int(input("Ingrese el número de la opción deseada: "))

        if opcion == 1:
          sig = input("\nIngrese los signos vitales nuevos del paciente: ")
          paciente.historia_clinica.signos_vitales = sig
        elif opcion == 2:
          nota = input(
              "\nIngrese las nuevas notas de evolución del paciente: ")
          paciente.historia_clinica.notas_evolucion = nota
        elif opcion == 3:
          imagen = input(
              "\nIngrese las nuevas imágenes diagnósticas del paciente: ")
          paciente.historia_clinica.imagenes_diagnosticas = imagen
        elif opcion == 4:
          resultado = input(
              "\nIngrese los nuevos resultados de exámenes del paciente: ")
          paciente.historia_clinica.resultados_examenes = resultado
        elif opcion == 5:
          nom_medicamento = input(
              "\nIngrese los nuevos medicamentos formulados del paciente: ")
          dos_medicamento = input("Ingrese la nueva dosis de medicamento: ")
          paciente.historia_clinica.medicamentos_formulados.nombre = nom_medicamento
          paciente.historia_clinica.medicamentos_formulados.dosis = dos_medicamento
        elif opcion == 6:
          for cama in camas:
            if cama.paciente == paciente:
              cama.liberar_cama(paciente)
              camas.remove(cama)
              break
        print("Historia clínica actualizada exitosamente.")
        break
    else:
      print("No se encontró un paciente con ese documento.")

  elif opcion == 3:
    print("\033[1m\n¿Qué reporte necesita?\033[0m")
    print("1. Porcentaje de ocupación hospitalaria")
    print("2. Promedio de estancia de servicios")
    print("3. Cantidad de admisiones y altas por servicio")
    print("4. Pacientes con enfermedades crónicas")
    print("5. Prescripción de medicamentos por servicio.")

    opcion = int(input("Ingrese el número de la opción deseada: "))
    # Validación de opciones
    while opcion < 1 or opcion > 5:
      print("Opción inválida.")
      opcion = int(input("Ingrese el número de la opción deseada: "))

    # Porcentaje de ocupación hospitalaria
    if opcion == 1:
      porcentaje = (len(camas) * 100) / 300
      print("El porcentaje de ocupación hospitalaria es de:",
            round(porcentaje, 2), "%")

    # Promedio de estancia de servicios
    elif opcion == 2:
      cont_dias_estancia = [0] * 9
      cont_pacientes_servicio = [0] * 9

      # Calcular el total de días de estancia y el número de pacientes por servicio
      for paciente in pacientes:
        cont_dias_estancia[paciente.servicio -
                           1] += paciente.historia_clinica.dia_estancia
        cont_pacientes_servicio[paciente.servicio - 1] += 1
      # Calcular el promedio de estancia por servicio
      print("Promedio de estancia por servicio:")
      for servicio in range(9):
        promedio = cont_dias_estancia[servicio] / cont_pacientes_servicio[
            servicio] if cont_pacientes_servicio[servicio] > 0 else 0
        print(f"Servicio {servicio + 1}: {promedio} días")

    elif opcion == 3:
      cont_admisiones = [0] * 9
      cont_altas = [0] * 9

      for paciente in pacientes:
        if not paciente.admision:
          cont_altas[paciente.servicio - 1] += 1
        if paciente.admision:
          cont_admisiones[paciente.servicio - 1] += 1

      print("Cantidad de admisiones y altas por servicio:")
      for i in range(9):
        print(
            f"Servicio {i + 1}: Admisiones={cont_admisiones[i]}, Altas={cont_altas[i]}"
        )

    elif opcion == 4:
      enfermedades_cronicas = [
          paciente for paciente in pacientes
          if paciente.historia_clinica.resultados_examenes == 1
      ]

      if enfermedades_cronicas:
        print("Pacientes con enfermedades crónicas:")
        for paciente in enfermedades_cronicas:
          print(f"Nombre: {paciente.nombre}, Documento: {paciente.documento}")
      else:
        print("No hay pacientes con enfermedades crónicas.")

    elif opcion == 5:
      medicamentos_por_servicio = {}

      for paciente in pacientes:
        servicio = paciente.servicio
        medicamento_nombre = paciente.historia_clinica.medicamentos_formulados.nombre

        if servicio not in medicamentos_por_servicio:
          medicamentos_por_servicio[servicio] = []

        medicamentos_por_servicio[servicio].append(medicamento_nombre)

      # Imprimir los medicamentos por servicio
      if (len(medicamentos_por_servicio) > 0):
        print("Prescripción de medicamentos por servicio:")
        for servicio, medicamentos in medicamentos_por_servicio.items():
          cantidad_medicamentos = len(medicamentos)
          nombres_medicamentos = ', '.join(medicamentos)
          print(
              f"Servicio {servicio}: {nombres_medicamentos} - Cantidad: {cantidad_medicamentos}"
          )
      else:
        print("No hay medicamentos formulados.")

  elif opcion == 4:
    print("\033[1m---------------------------------------\033[0m")
    print("\033[1mSaliendo del programa...\033[0m")
    print("\033[1m---------------------------------------\033[0m")
    print("Finalizado")
    break

  else:
    print("Opción no válida. Por favor, ingrese una opción válida.\n")
