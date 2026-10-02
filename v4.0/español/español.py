print (60 * "-")
choice = input("Elija: \n 1 - Convertir todas las unidades \n 2 - Convertir una unidad \n" + 60 * '-' + "\n> ")

if choice == "1":
    # Carregar o arquivo de idioma correspondente
    from . import todaunidad
    pass
elif choice == "2":
    # Carregar o arquivo de idioma correspondente
    from . import unaunidad
    pass
else:
    print("Opción inválida.")
    exit(1)