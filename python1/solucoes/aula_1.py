class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome.capitalize()
        self.idade = int(idade)
        self.maioridade = self.testaMarioridade()
        self.periodo = 0

    def testaMarioridade(self):
        if self.idade >= 18:
            return "Maior"
        else:
            return "Menor"
    def printaUsuario(self):
        print("{} - {} - {}".format(self.nome, self.idade, self.maioridade))

    def mudaIdade(self, idade):
        self.idade = idade
        self.maioridade = self.testaMarioridade()

    def mudaPerido(self):
        ok = False
        periodo = int(input("Entre com um periodo para o usuario {} ".format(self.nome)))
        while ok == False:
            if 0 <= periodo <= 10:
                self.periodo = int(periodo)
                ok = True
            else:
                periodo = int(input("Periodo invalido, tente novamente"))

    def mostraPeriodo(self):
        if self.periodo > 0:
            print("{} tem {} anos e esta no {}º periodo".format(self.nome, self.idade, self.periodo))
        else:
            print("{} nao esta na faculdade".format(self.nome))


def menu_principal ():
    print("\n\n____menu____")
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
        print("A lista de usuario é:")
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