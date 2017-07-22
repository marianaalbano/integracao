
user = []


def menu():
    print ("1 - Cadastro de usuário \
            2 - Acesso ao Sistema \
            3 - Sair ")
    opcao = int(input("Digite a opção desejada: "))
    return opcao


def switch(num):
    if num == 1:
        cadastro_usuario()
    elif num == 2:
        acesso_sistema()
    elif num == 3:
        print ("Saindo do sistema")
        exit()
    else:
        print ("Digite uma opção válida \n")

def cadastro_usuario():
    global user

    login = input("Digite o nome: ")
    pwd = input("Digite a senha: ")

    dados = {"usuario":login,"pwd":pwd}
    user.append(dados)
    print ("Usuário cadastrado com sucesso\n \n")



def acesso_sistema():
    global user
    username = input("Digite o usuario: ")
    pwd = input("Digite a senha: ")


    for u in user:
        if u["usuario"] == username and u["pwd"] == pwd:
            logado = True
            print ("Acesso permitido!")
            return


    print ("Acesso negado!")




if __name__ == '__main__':
    while True:
        switch(menu())
