
#funcao para pesquisa dos dados no banco de dados 
def buscarAtleta(dicionario, nome):
    chaves = []
    for chave in dicionario:
        if chave.startswith(nome):
            chaves.append(chave)
    return chaves

def mostrarAtleta(bancoAtleta, chaves):
    table = []
    for chave in chaves:
        table.append([
            bancoAtleta[chave]["nome"],
            bancoAtleta[chave]["rg"],
            bancoAtleta[chave]["cpf"],
            bancoAtleta[chave]["posicao"],
            bancoAtleta[chave]["endereco"],
        ])
    print(table)
    input('\nDigite enter para retornar ao menu: ')
