def main():

    inicio = int(input("Numero inicial: "))
    iteraciones = int(input("Numero de iteraciones: "))

    if iteraciones < 0:
        print("Error: numero invalido")
        return

    fibonacci = [inicio, 1]

    for i in range(iteraciones-2):
        siguiente = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(siguiente)

    print("Lista generada:", fibonacci)
    print("Cantidad de terminos:", len(fibonacci))
    print("Ultimo valor:", fibonacci[-1])


if __name__ == "__main__":
    main()