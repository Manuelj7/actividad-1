def main():

    estudiantes = []

    cantidad = int(input("Cuantos estudiantes desea ingresar: "))

    for i in range(cantidad):

        print("\nEstudiante", i+1)

        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        estado = input("Estado (activo/inactivo): ")

        materias = []
        notas = {}

        num_materias = int(input("Cuantas materias tiene (minimo 3): "))

        while num_materias < 3:
            print("Debe ingresar minimo 3 materias")
            num_materias = int(input("Cuantas materias tiene: "))

        for j in range(num_materias):

            materia = input("Nombre de la materia: ")

            nota = float(input("Nota (0.0 - 5.0): "))

            while nota < 0 or nota > 5:
                print("Nota invalida")
                nota = float(input("Nota (0.0 - 5.0): "))

            materias.append(materia)
            notas[materia] = nota

        estudiante = {
            "nombre": nombre,
            "edad": edad,
            "estado": estado,
            "materias": materias,
            "notas": notas
        }

        estudiantes.append(estudiante)

    for est in estudiantes:

        promedio = sum(est["notas"].values()) / len(est["notas"])

        mejor = max(est["notas"], key=est["notas"].get)
        peor = min(est["notas"], key=est["notas"].get)

        print("\nEstudiante:", est["nombre"])
        print("Promedio:", round(promedio,2))
        print("Mejor materia:", mejor)
        print("Peor materia:", peor)

        if promedio >= 3:
            print("Aprueba")
        else:
            print("No aprueba")


if __name__ == "__main__":
    main()