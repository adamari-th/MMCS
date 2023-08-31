#imprima numeros mayores al tres

numero = int(input("Escriba un número entero mayor que tres: "))

if numero <= 3:
    print("¡Le he pedido un número entero mayor que tres!")
else:
    print(f"El numero {numero} es mayor que tres ")
    for i in range(3, numero):
        print(i + 1, end=",")
            

    