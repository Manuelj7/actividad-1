def pedir_nombre():

    nombre = input("Nombre: ")

    while len(nombre) < 3:
        print("Nombre invalido")
        nombre = input("Nombre: ")

    return nombre


def pedir_edad():

    edad = int(input("Edad: "))

    while edad < 0 or edad > 120:
        print("Edad invalida")
        edad = int(input("Edad: "))

    return edad


def pedir_correo():

    correo = input("Correo: ")

    while "@" not in correo or (".com" not in correo and "edu.co" not in correo):
        print("Correo invalido")
        correo = input("Correo: ")

    return correo


def main():

    usuarios = []

    nombre = pedir_nombre()
    edad = pedir_edad()
    correo = pedir_correo()

    usuario = {
        "nombre": nombre,
        "edad": edad,
        "correo": correo
    }

    usuarios.append(usuario)

    print("Usuario guardado:", usuarios)


if __name__ == "__main__":
    main()