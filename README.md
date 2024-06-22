# Análise de Votações de Deputados

Este projeto consiste em um programa em Python que analisa dados de votações de deputados, criando um grafo direcionado ponderado. O programa oferece as seguintes funcionalidades:

1. **Informar arquivo de votações:** Permite ao usuário informar um arquivo CSV contendo dados de votações de deputados. O programa lê este arquivo e cria o grafo com base nos dados fornecidos.

2. **Gerar arquivos de saída:** Após a leitura do arquivo de votações, o programa pode gerar dois arquivos de saída. O primeiro arquivo contém informações sobre o grafo gerado, incluindo o número de nós (deputados) e caminhos (votações em que os deputados votaram de maneira semelhante). O segundo arquivo contém o nome de cada deputado e o número de votações em que ele votou.

3. **Consultar API:** O programa também pode consultar a API da Câmara dos Deputados para obter informações sobre votações em tempo real. Ele cria ou atualiza o grafo com base nessas informações.

## Observações

- Certifique-se de que o arquivo de votações está no formato CSV e contém as informações necessárias para a análise (como ID da votação, voto do deputado e nome do deputado).
- O programa faz uso da biblioteca `requests` para consultar a API da Câmara dos Deputados e da biblioteca `tqdm` para exibir barras de progresso durante o processamento.

Este projeto foi desenvolvido como um desafio pessoal, sem o uso de bibliotecas externas, como Pandas, e pode ser expandido para incluir mais funcionalidades e análises sobre os dados de votações dos deputados.
