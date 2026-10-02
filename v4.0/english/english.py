print (60 * "-")
choice = input("Choose: \n 1 - Convert all units \n 2 - Convert one unit \n" + 60 * '-' + "\n> ")

if choice == "1":
    # Carregar o arquivo de idioma correspondente
    from . import everyunit
    pass
elif choice == "2":
    # Carregar o arquivo de idioma correspondente
    from . import oneunit
    pass
else:
    print("Invalid option.")
    exit(1)