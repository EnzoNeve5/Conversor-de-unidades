print (60 * "-")
choice = input("Escolha: \n 1 - Converter todas as unidades \n 2 - Converter uma unidade \n" + 60 * '-' + "\n> ")

if choice == "1":
    # Carregar o arquivo de idioma correspondente
    from . import todaunidade
    pass
elif choice == "2":
    # Carregar o arquivo de idioma correspondente
    from . import umaunidade
    pass
else:
    print("Opção inválida.")
    exit(1)