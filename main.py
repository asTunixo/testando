# Implementação de uma lista vazia com o nome de lista_livro e a variável id_global com valor inicial igual a 0 
lista_livro = []
id_global = 0

# print com uma mensagem de boas-vindas que apareça o seu nome
print('Bem-vindo a central de controle de livros do Antonio Sergio Cardoso Sachinski Junior')

# Implementação de uma função chamada cadastrar_livro(id)
def cadastrar_livro(id):
  print('\nMenu de cadastro:')
  print('Índice: ', id_global)

# Pergunta nome, autor, editora do livro
  nome = input('Digite o nome do livro: ')
  autor = input('Digite o nome do autor do livro: ')
  editora = input('Digite o nome da editora do livro: ')

# Armazena o id (este é fornecido via parâmetro da função), nome, autor, editora dentro de um dicionário
  dic_livro = {'id' : id_global, 'nome' : nome, 'autor' : autor, 'editora' : editora}

# Copiar o dicionário para dentro da lista_livro;
  lista_livro.append(dic_livro.copy())
  print('Livro cadastrado.')
  
# Implementação de uma função chamada consultar_livro()
def consultar_livro():
    while True:
        print('\nMenu de consulta:')

# Pergunta qual opção deseja (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Autor / 4. Retornar ao menu) e   printar a “Opção inválida" se entrar com valor diferente de 1, 2, 3 ou 4 
        m2 = input('1 - Consultar Todos \n2 - Consultar por Id \n3 - Consultar por Autor \n4 - Retornar ao menu \nEscolha a opção desejada: ')
        if m2 == '1':
            for livro in lista_livro:
                for chave, valor in livro.items():
                    print('{}: {}'.format(chave, valor))
        elif m2 == '2':
            id_desejado = int(input('Digite o Id para consulta: '))
            livro_encontrado = False
            for livro in lista_livro:
                if livro['id'] == id_desejado:
                    for chave, valor in livro.items():
                        print('{}: {}'.format(chave, valor))
                    livro_encontrado = True
                    break 
            if not livro_encontrado:
                print('Id inválida. Tente novamente.')
        elif m2 == '3':
            autor_desejado = str(input('Digite o nome do autor para consulta: '))
            autor_encontrado = False
            for livro in lista_livro:
                if livro['autor'] == autor_desejado:
                    for chave, valor in livro.items():
                        print('{}: {}'.format(chave, valor))
                    autor_encontrado = True
            if not autor_encontrado:
                print('Nome inválido. Tente novamente.')
        elif m2 == '4':
            return
        else:
            print('Opção inválida. Tente novamente.')


   
# Implementação de uma função chamada remover_livro()
def remover_livro():
  while True:
    print('\nMenu de remoção:')
    
# Pergunta pelo id do colaborador a ser removido
    id_remover = int(input('Digite o Id para remoção: '))
    for livro in lista_livro:
      if livro['id'] == id_remover:

# Remover o livro da lista_livro
        lista_livro.remove(livro)
        print('Livro removido.')
        return
      else:
        print('Id inválida. Tente novamente.')
        continue
        
# Main
while True:
  print('\nMenu principal:')

# Pergunta qual opção deseja (1. Cadastrar Livro / 2. Consultar Livro / 3. Remover Livro / 4. Encerrar Programa)e executar o printar de “Opção inválida" se entrar com valor diferente de 1, 2, 3 ou 4 
  m1 = input('1 - Cadastrar livro \n2 - Consultar livro(s) \n3 - Remover livro \n4 - Sair \nEscolha a opção desejada: ')
  if m1 == '1':
    id_global += 1
    cadastrar_livro(id_global)
  elif m1 == '2':
    consultar_livro()
  elif m1 == '3':
    remover_livro()
  elif m1 == '4':
    break
  else:
    print('Opção inválida. Tente novamente.')
    continue
    