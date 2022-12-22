from files.lib_Usuarios import Usuario

def menu_principal ():
    print("\n*** MENU ***")
    print("1 - Cadastrar novo usuario\n"
          "2 - verificar lista de usuarios\n"
          "3 - Ultimo cadastrado\n"
          "4 - Deletar Item\n"
          "5 - mudar perido\n"
          "6 - mudar idade\n"
          "S - sair\n")
    return input()

sair = False
lista= []
while sair == False:
    menu = menu_principal()
    objeto = ""
    if menu == "1":
        nome = input("Nome: ")
        idade = input("Idade: ")
        lista.append(Usuario(nome,idade))
    elif menu == "2":
        for objeto in lista:
            objeto.printaUsuario()
            if objeto.periodo > 0:
                objeto.mostraPeriodo()
    elif menu == "3":
        objeto = lista[-1]
        objeto.printaUsuario()
    elif menu =="4":
        nome = input("Nome: ").capitalize()
        for objeto in lista:
            if nome == objeto.nome:
                lista.remove(objeto)
    elif menu == "5":
        nome = input("Nome: ").capitalize()
        for objeto in lista:
            if nome == objeto.nome:
                objeto.mudaPerido()
    elif menu == "6":
        nome = input("Nome: ").capitalize()
        for objeto in lista:
            if nome == objeto.nome:
                nidade = int(input("Nova idade: "))
                objeto.mudaIdade(nidade)
    elif menu == "S":
        sair = True