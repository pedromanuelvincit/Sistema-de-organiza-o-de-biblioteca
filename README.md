# Sistema de Organização de Biblioteca Digital

Este é um sistema simples de gerenciamento de biblioteca digital, desenvolvido em Python. O programa permite organizar e gerenciar arquivos digitais em uma pasta específica.

## Funcionalidades

### 1. Listar Documentos Digitais
- Lista todos os arquivos presentes na pasta `biblioteca digital`
- Organiza os arquivos por:
  - **Tipo de arquivo** (extensão)
  - **Ano de modificação**

### 2. Adicionar Item
- Permite copiar um arquivo para a pasta `biblioteca digital`
- O usuário deve fornecer o caminho completo do arquivo de origem
- Mantém o nome original do arquivo ao copiar

### 3. Renomear Item
- Permite renomear arquivos existentes na pasta `biblioteca digital`
- O usuário deve informar:
  - Nome atual do arquivo
  - Novo nome desejado

### 4. Remover Item
- Remove um arquivo da pasta `biblioteca digital`
- O usuário deve informar o nome do arquivo a ser removido

## Como Executar

1. Certifique-se de ter o Python instalado
2. Verifique se existe uma pasta chamada `biblioteca digital` no mesmo diretório do programa, atribua outro nome dentro do código do sistema.
3. Execute o programa com o comando:
   ```
   python main.py
   ```
4. Use o menu numérico para navegar entre as opções
5. Para sair do programa, escolha a opção `0`

## Requisitos
- Python 3.x
- Sistema operacional: Windows, Linux ou macOS
- Pasta `biblioteca digital` no mesmo diretório do programa ou altere o código conforme sua preferência
