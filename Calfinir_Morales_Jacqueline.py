import csv
import math
import random

trabajadores = [{"nombre": "Juan Pérez"},
                 {"nombre": "María García"},
                 {"nombre": "Carlos López"},
                 {"nombre": "Ana Martínez"},
                 {"nombre": "Pedro Rodríguez"},
                 {"nombre": "Laura Hernández"},
                 {"nombre": "Miguel Sánchez"},
                 {"nombre": "Isabel Gómez"},
                 {"nombre": "Francisco Díaz"},
                 {"nombre": "Elena Fernández"}]

def Asignar_Sueldos_Aleatorios():
    for trabajador in trabajadores:
        trabajador["sueldo"] = random.randint(300000,2500000)
    print("Sueldos Aleatorios generados")

def Clasificar_Sueldos():

    print("SUELDOS MENORES A $800.000: ")
    for trabajador in trabajadores:
        if trabajador["sueldo"] < 800000:
            print("Nombre Empleado: ", trabajador["nombre"], "Sueldo: $", trabajador["sueldo"])

    print("SUELDOS ENTRE $800.000 Y $2.000.000: ")
    for trabajador in trabajadores:
        if trabajador["sueldo"] >= 800000 and trabajador["sueldo"] <= 2000000:
            print("Nombre Empleado: ", trabajador["nombre"], "Sueldo: $", trabajador["sueldo"])

    print("SUELDOS MAYORES A $2.000.000: ")
    for trabajador in trabajadores:
        if trabajador["sueldo"] > 2000000:
            print("Nombre Empleado: ", trabajador["nombre"], "Sueldo: $", trabajador["sueldo"])


def Ver_Estadisticas():
    sueldo = []
    for trabajador in trabajadores:
        sueldo.append(trabajador["sueldo"])

    sueldomasbajo = min(sueldo)
    sueldomasalto = max(sueldo)
    promediosueldos = sum(sueldo) / len(sueldo)

    print("El sueldo más bajo es: ", sueldomasbajo)
    print("El sueldo más alto es: ", sueldomasalto)
    print("El promedio de los sueldos es: ", promediosueldos)
    

def Reporte_Sueldos():
    with open("ReporteSueldos.csv", "w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Nombre Empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])

        for trabajador in trabajadores:
            sueldo = trabajador["sueldo"]
            DescuentoSalud = sueldo * 0.07
            DescuentoAFP = sueldo * 0.12
            SueldoLiquido = sueldo - DescuentoSalud - DescuentoAFP
            writer.writerow([trabajador["nombre"], trabajador["sueldo"], DescuentoSalud, DescuentoAFP, SueldoLiquido])
            print("Nombre Empleado: " , trabajador["nombre"], " Sueldo Base: ", sueldo, " Descuento Salud: ", DescuentoSalud, " Descuento AFP: ", DescuentoAFP, " Sueldo Líquido: ", SueldoLiquido)


def Salir_Programa():
    print("Finalizando programa...")
    print("Desarrollado por Jacqueline Calfiñir")
    print("RUT 18.548.040-2")

while True:
    try:
        print("Bienvenido al programa, seleccione la acción que desea ejecutar:")
        print("1. Asignar Sueldos Aleatorios")
        print("2. Clasificar Sueldos")
        print("3. Ver Estadísticas")
        print("4. Reporte de Sueldos")
        print("6. Salir del Programa")
        opcion = int(input("Ingrese la opción (1-5): "))

        if opcion == 1:
            Asignar_Sueldos_Aleatorios()

        elif opcion ==2:
            Clasificar_Sueldos()

        elif opcion == 3:
            Ver_Estadisticas()

        elif opcion == 4:
            Reporte_Sueldos()

        elif opcion == 5:
            Salir_Programa()
            break

        else:
            print("Ingrese opción válida (1-5)")
    except ValueError:
        print("Ingrese un valor dentro de las opciones (1-5)")
