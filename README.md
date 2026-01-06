📚 Sistema de Gerenciamento Acadêmico (Python)
Este projeto consiste em um sistema de gerenciamento acadêmico em Python, executado via terminal, que permite realizar operações de CRUD (Criar, Listar, Atualizar e Excluir) utilizando arquivos JSON para persistência de dados.

🎯 Funcionalidades
O sistema possui um menu principal que dá acesso ao gerenciamento de:

👨‍🎓 Estudantes
👨‍🏫 Professores
📘 Disciplinas
🏫 Turmas
📝 Matrículas

Para cada entidade, o usuário pode realizar as seguintes operações:

- Incluir novos registros
- Listar registros cadastrados
- Atualizar registros existentes
- Excluir registros
- Voltar ao menu principal

💾 Persistência de Dados
Os dados são armazenados em arquivos JSON, um para cada tipo de cadastro:

- estudantes.json
- professor.json
- disciplina.json
- turma.json
- matricula.json

O sistema faz a leitura e escrita automática desses arquivos, garantindo que os dados sejam mantidos mesmo após o encerramento do programa.

🧠 Estrutura do Código

- Uso de funções modulares para exibição de menus, operações de CRUD e manipulação de arquivos.
- Funções genéricas reutilizadas para diferentes tipos de cadastro.
- Tratamento básico de erros ao ler arquivos JSON inexistentes.
- Interface simples e intuitiva via terminal.

🛠 Tecnologias Utilizadas

- Python 3
- Biblioteca padrão json

🚀 Objetivo
Projeto desenvolvido com fins acadêmicos, com o objetivo de praticar:

- Lógica de programação
- Estruturas de dados (listas e dicionários)
- Modularização de código
- Persistência de dados com JSON
