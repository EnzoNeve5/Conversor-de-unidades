print('⠀⠀⠀⠀⣠⣴⣶⣿⣿⣿⣿⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀               ')
print('⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿     ⣿     ⣿⣿⣿⣿⣿    ⣿⣿⣿⣿⣿      ⣿⣿⣿⣿ ')
print('⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿         ⣿       ⣿      ⣿         ⣿          ')
print('⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀ ⣿        ⣿⣿⣿      ⣿      ⣿         ⣿          ')
print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿       ⣿   ⣿     ⣿      ⣿⣿⣿⣿⣿     ⣿        ')
print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿       ⣿   ⣿     ⣿      ⣿         ⣿         ')
print('⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⣿       ⣿⣿⣿⣿⣿     ⣿      ⣿         ⣿        ')
print('⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿  ⣿     ⣿    ⣿      ⣿⣿⣿⣿⣿      ⣿⣿⣿⣿  ')
print('⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀              ')
print('      ⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀              ')
print (60 * "-")
language = input("Escolha o idioma | Choose the language | Elija el idioma \n 1 - Português | Portuguese | Portugués \n 2 - Inglês | English | Inglés \n 3 - Espanhol | Spanish | Español \n" + 60 * '-' + "\n> ")

if language == "1":
    # Carregar o arquivo de idioma correspondente
    import português.português as português
    pass
elif language == "2":
    # Carregar o arquivo de idioma correspondente
    import english.english as english
    pass
elif language == "3":
    # Carregar o arquivo de idioma correspondente
    import español.español as español
    pass
else:
    print("Opção inválida. | Invalid option. | Opción inválida.")
    exit(1)