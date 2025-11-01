import os
from datetime import datetime
import shutil
# Função para exibir o menu do programa
def exibir_menu():
    print("\n=== Sistema de Gerenciamento ===")
    print("1. Listar documentos digitais")
    print("2. Adicionar item")
    print("3. Buscar item")
    print("4. Atualizar item")
    print("5. Remover item")
    print("0. Sair")
    print("============================")
# Logica do programa, aqui executa uma tarefa com base na solicitação feita pelo usuário
def main():
    # Loop infinito, o usuário pode modificar sempre que quiser suas pastas.
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ")
    #Opção para listar os documentos na pasta atual.
        if opcao == "1":
            print("\nListar documentos digitais...")
            caminho = 'biblioteca digital'
            arquivos_por_tipo = {}
            arquivos_por_data = {}
            for item in os.listdir(caminho):
                caminho_completo = os.path.join(caminho, item)
                if os.path.isfile(caminho_completo):
                    ext = os.path.splitext(item)[1].lower()  # '.pdf' ou ''
                    ano = datetime.fromtimestamp(os.path.getmtime(caminho_completo)).year
                    if ext not in arquivos_por_tipo:
                        arquivos_por_tipo[ext] = []
                    arquivos_por_tipo[ext].append(item)
                    if ano not in arquivos_por_data:
                        arquivos_por_data[ano] = []
                    arquivos_por_data[ano].append(item)

            print("\nArquivos por tipo:")
            for ext in sorted(arquivos_por_tipo):
                print(ext + ":")
                for a in sorted(arquivos_por_tipo[ext]):
                    print("  " + a)

            print("\nArquivos por ano:")
            for ano in sorted(arquivos_por_data):
                print(str(ano) + ":")
                for a in sorted(arquivos_por_data[ano]):
                    print("  " + a)
        elif opcao == "2":
            print("\nAdicionar item...")
            origem = input("Caminho do arquivo: ")
            nome_arquivo = os.path.basename(origem)
            destino = os.path.join('biblioteca digital', nome_arquivo)
            shutil.copyfile(origem, destino)
            print("Arquivo copiado!")
if __name__ == "__main__":
    main()