# Automação do Cadastramento de Produtos

## Descrição do Projeto
Este projeto tem como objetivo automatizar o processo de cadastramento de uma lista de produtos em um sistema, eliminando a necessidade de inserções manuais e reduzindo o tempo necessário para concluir a tarefa. A automação é implementada com Python e bibliotecas PyAutoGUI e Pandas.

<p></p>

## Funcionalidades
- **Automação do navegador:** abre o navegador e acessa o site desejado automaticamente.
- **Login automatizado:** realiza o login com credenciais pré-definidas.
- **Importação dos dados:** carrega uma base de dados de produtos a partir de um arquivo CSV.
- **Cadastro automático:** insere os dados de cada produto no sistema, incluindo código, marca, tipo, categoria, preço unitário, custo e observações.

<p></p>

## Tecnologias utilizadas
- Python
- PyAutoGUI: para interações automatizadas com o sistema.
- pandas: para manipulação e leitura da base de dados.
- time: para controlar pausas entre as interações.

## Observações
- Certifique-se de ajustar as coordenadas (x, y) dos cliques conforme o layout do sistema.
- Use um arquivo CSV estruturado com colunas: _codigo, marca, tipo, categoria, preco_unitario, custo_ e _obs_

## Licença
Este projeto está licenciado sob licença MIT.
