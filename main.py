from grafo import Grafo

def main_menu():
    grafo = Grafo()
    input_file = ''
    while True:
        print("\nMenu:")
        print("1. Informar arquivo de votações")
        print("2. Gerar arquivos de saída")
        print("3. Consultar API")
        print("4. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            input_file = input("Informe o arquivo de votações: ")
            grafo.ler_arquivo(input_file)
        elif choice == '2':
            if input_file:
                output_graph_file = input_file.replace('.csv', '-graph.txt')
                output_deputados_file = input_file.replace('.csv', '-deputados.txt')
                grafo.escrever_arquivo(output_graph_file)
                grafo.pesosaida(input_file, output_deputados_file)
                print("O grafo foi escrito nos arquivos:")
                print(output_graph_file)
                print(output_deputados_file)
            else:
                print("Por favor, informe o arquivo de votações primeiro.")
        elif choice == '3':
            if input_file:
                grafo.api()
                grafo.escrever_arquivo("API.txt")
            else:
                print("Por favor, informe o arquivo de votações primeiro.")
        elif choice == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main_menu()