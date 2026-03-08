def main():

    print("1. Numero primo")
    print("2. Factorial")
    print("3. Contar vocales")

    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:

        num = int(input("Ingrese un numero: "))
        primo = True

        if num <= 1:
            primo = False

        for i in range(2, num):
            if num % i == 0:
                primo = False

        if primo:
            print("Es primo")
        else:
            print("No es primo")

    elif opcion == 2:

        num = int(input("Ingrese un numero: "))
        factorial = 1

        for i in range(1, num+1):
            factorial *= i

        print("Factorial:", factorial)

    elif opcion == 3:

        texto = input("Ingrese un texto: ").lower()

        vocales = {
            "a":0,
            "e":0,
            "i":0,
            "o":0,
            "u":0
        }

        for letra in texto:
            if letra in vocales:
                vocales[letra] += 1

        print("Conteo de vocales:", vocales)

    else:
        print("Opcion invalida")


if __name__ == "__main__":
    main()