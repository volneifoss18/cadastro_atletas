from cadastro import buscarAtleta, mostrarAtleta
import os

bancoAtleta = {}

while True:
    try:

        print('Escola de Formaçao Miami Dade')
        os.system('clear') or None
        menu = int(input('Escolha uma opçao: \n1-[Cadastrar atleta]\n2-[Buscar Atleta]\n3-[Sair]\nSelecione uma das opcoes: '))
        os.system('clear') or None
        if menu == 1:

            #cadastro do atleta
            nome = input('Digite o nome do atleta: ').capitalize()
            rg = int(input('Digite o RG do atleta: '))
            cpf = int(input('Digite o CPF do atleta: '))
            posicao = input('Posicao em campo do atleta: ')
            endereco = input('Digite o endereço do atleta: ')

            #adicionando cadastro ao banco de dados
            bancoAtleta[nome.lower()] = {
                "nome": nome,
                "rg": rg,
                "cpf": cpf,
                "posicao": posicao,
                "endereco": endereco
            }

        elif menu == 2:
            #busca do atleta
            nome = input('Digite o nome do atleta: ').lower()
            buscaEncontrada = buscarAtleta(bancoAtleta, nome)
            mostrarAtleta(bancoAtleta, buscaEncontrada)

        elif menu == 3:
            #parar o loop
            break
    
        else:
            #caso seja digitado outra coisa
            print('opçao invalida, digite apenas as opcoes acima')
    except:
        print('Digite opçoes validas')    

