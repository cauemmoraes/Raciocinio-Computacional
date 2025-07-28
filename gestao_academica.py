import json

# Aluno: Cauê Matos Moraes
# Curso: Análise e Desenvolvimento de Sistemas

# FUNÇÕES DO PROGRAMA #

# Função responsável por mostrar o menu principal.
def display_menu_principal():
  print()
  print('---- MENU PRINCIPAL ----')
  print()

  print('(1) Gerenciar estudantes.')
  print('(2) Gerenciar professores.')
  print('(3) Gerenciar disciplinas.')
  print('(4) Gerenciar turmas.')
  print('(5) Gerenciar matrículas.')
  print('(9) Sair.')

  print()

  return int(input('Informe a opção desejada: '))

# Função responsável por mostrar o menu de operações.
def display_menu_operacoes():
  print('***** MENU DE OPERAÇÕES *****')
  print()

  print('(1) Incluir.')
  print('(2) Listar.')
  print('(3) Atualizar.')
  print('(4) Excluir.')
  print('(5) Voltar ao menu principal.')

  print()

  return int(input('Informe a opção desejada: '))

# Função responsável por fazer a inclusão ao dicionário dentro da lista.
def incluir_pessoa(file):

  print('===== INCLUSÃO =====')

  cod_cadastro = int(input('Informe o código do cadastro: '))
  nome_cadastro = input('Informe o nome do cadastro: ')
  cpf_cadastro = input('Informe o CPF do cadastro: ')
  dic_cadastro = {
    "cod": cod_cadastro, 
    "nome": nome_cadastro, 
    "cpf": cpf_cadastro
  }
  
  lista = ler_arquivo(file)
  lista.append(dic_cadastro)
  salvar_arquivo(lista, file)
def incluir_conteudo(file):

  print('===== INCLUSÃO =====')

  cod_cadastro = int(input('Informe o código do cadastro: '))
  nome_cadastro = input('Informe o nome do cadastro: ')
  dic_cadastro = {
    "cod": cod_cadastro, 
    "nome": nome_cadastro
  }
  
  lista = ler_arquivo(file)
  lista.append(dic_cadastro)
  salvar_arquivo(lista, file)

# Função responsável por listar os nomes que estão dentro da lista de estudantes.
def listar_cadastro(file):
  lista = ler_arquivo(file)
  print('===== LISTAGEM =====')
  print()
  if len(lista) == 0:
    print('Não há cadastrados.')
    print()
  else:
    for cadastro in lista:
      print(f'- {cadastro}')

# Função responsável por editar o dicionário da lista, com as informções baseada no código dado pelo usuário.
def atualizar_pessoa(file):

  lista = ler_arquivo(file)
  print('===== ATUALIZAR =====')
  print()
  while (True):
    att_cod = int(input('Informe o código do cadastro a ser atualizado: '))

    modify_cadastro = None
    for cadastro in lista:
      if cadastro["cod"] == att_cod:
        modify_cadastro = cadastro
        break

    if modify_cadastro is not None:
      modify_cadastro["cod"] = int(input('Informe o novo código do cadastro: '))
      modify_cadastro["nome"] = input('Informe o novo nome do cadastro: ')
      modify_cadastro["cpf"] = input('Informe o novo CPF do cadastro: ')
      salvar_arquivo(lista, file)
      print('Aluno atualizado.')
      break
    else:
      print('Código não encontrado, tente novamente.')
def atualizar_conteudo(file):

  lista = ler_arquivo(file)
  print('===== ATUALIZAR =====')
  print()
  while (True):
    att_cod = int(input('Informe o código do cadastro a ser atualizado: '))

    modify_cadastro = None
    for cadastro in lista:
      if cadastro["cod"] == att_cod:
        modify_cadastro = cadastro
        break

    if modify_cadastro is not None:
      modify_cadastro["cod"] = int(input('Informe o novo código do cadastro: '))
      modify_cadastro["nome"] = input('Informe o novo nome do cadastro: ')
      salvar_arquivo(lista, file)
      print('Aluno atualizado.')
      break
    else:
      print('Código não encontrado, tente novamente.')
      
# Função responsável por excluir o dicionário da lista, com as informções baseada no código dado pelo usuário.
def excluir_cadastro(file):
  lista = ler_arquivo(file)
  ('===== EXCLUIR =====')
  print()
  while (True):
    del_cod = int(input('Informe o código do estudante a ser excluido: '))

    remove_cadastro = None
    for dic_cadastro in lista:
      if dic_cadastro["cod"] == del_cod:
        remove_cadastro = dic_cadastro
        break

    if remove_cadastro is not None:
      lista.remove(remove_cadastro)
      salvar_arquivo(lista, file)
      print('Aluno removido.')
      break
    else:
      print('Código não encontrado, tente novamente.')

# Função que escreve dentro do arquivo JSON.
def salvar_arquivo(lista, file):
  with open(file, 'w', encoding='utf-8') as opened_file:
    json.dump(lista, opened_file, ensure_ascii=False)

# Função que faz a leitura do arquivo JSON
def ler_arquivo(file):
  try:
    with open(file, 'r', encoding='utf-8') as opened_file:
      lista = json.load(opened_file)
    return lista
  except:
    return []

def processar_menu_operacao(user_input, file, cpf_true):
  # Chamando a função incluir_estudante.
    if user_input == 1:
      if cpf_true:
        incluir_pessoa(file)
      else:
        incluir_conteudo(file)
      print()

    # Chamando a função listar_estudantes.
    elif user_input == 2:
      listar_cadastro(file)
      print()

    # Chamando a função atualizar_estudante.
    elif user_input == 3:
      if cpf_true:
        atualizar_pessoa(file)
      else:
        atualizar_conteudo(file)
      print()

    # Chamando a função excluir_estudante.
    elif user_input == 4:
      excluir_cadastro(file)
      print()
      
    # Sair do menu de operações e valor inválido.
    elif user_input == 5:
      return False
    else:
      print('Valor Inválido, tente novamente.')

    return True

# INICIO DO PROGRAMA #

estudante_file = 'estudantes.json'
professor_file = 'professor.json'
disciplina_file = 'disciplina.json'
turma_file = 'turma.json'
matricula_file = 'matricula.json'

while(True):
# Chamando a função display_menu_principal.
  user_input = display_menu_principal()
  print()

  # Estrutura condicional em que guiará de acordo com a escolha do usuário.
  if user_input == 1:
    while(True):
      # Chamando a função display_menu_operacoes.
      user_input_2 = display_menu_operacoes()
      print()

      cpf = True
      if not processar_menu_operacao(user_input_2, estudante_file, cpf):
        break

  elif user_input == 2:
    while(True):
      # Chamando a função display_menu_operacoes.
      user_input_2 = display_menu_operacoes()
      print()
      
      cpf = True
      if not processar_menu_operacao(user_input_2, professor_file, cpf):
        break
  
  elif user_input ==3:
    while(True):
      # Chamando a função display_menu_operacoes.
      user_input_2 = display_menu_operacoes()
      print()

      cpf = False
      if not processar_menu_operacao(user_input_2, disciplina_file, cpf):
        break
  
  elif user_input == 4:
    while(True):
      # Chamando a função display_menu_operacoes.
      user_input_2 = display_menu_operacoes()
      print()

      cpf = False
      if not processar_menu_operacao(user_input_2, turma_file, cpf):
        break

  # As demais opções que ainda seguem em desenvolvimento.
  elif user_input == 5:
    while(True):
      # Chamando a função display_menu_operacoes.
      user_input_2 = display_menu_operacoes()
      print()

      cpf = False
      if not processar_menu_operacao(user_input_2, matricula_file, cpf):
        break

  # Finalizar o programa e valor inválido.
  elif user_input == 9:
    print('Obrigado! Volte sempre.')
    break
  else:
    print('Valor Inválido, tente novamente.')