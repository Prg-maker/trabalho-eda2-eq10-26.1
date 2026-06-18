# Estrutura do Projeto

## Arquivos

- **main.py**: Este é o arquivo principal do programa. Ele inicializa os dados, criando a lista de ocorrências, e chama as funções do grafo e dos algoritmos.
- **algoritmos.py**: Neste arquivo, estão os algoritmos de grafos utilizados para a análise dos dados, como o BFS (Busca em Largura) e o algoritmo de Kruskal. Este arquivo não deve ter imports.
- **grafos.py**: Criação e manipulação dos gráfos. Este arquivo não deve ter imports.
- **processamento_de_dados.py**: Este módulo é responsável por abrir os arquivos de texto, realizar seu tratamento com a biblioteca de PLN e, além disso, efetuar o salvamento dos dados processados.

## Pasta do Dados (data)

### Pasta *text*

Esta pasta armazena os dados iniciais gerados para a análise. Os textos devem estar separados em suas respectivas pastas de acordo com cada época dentro deste repositório. Em nosso caso, são cinco pastas para cada época, com seis textos em cada uma.

### Pasta *processed*

Esta pasta armazena os dados obtidos pelo programa, sendo atualizada toda vez que o sistema é iniciado. Os arquivos são salvos nos formatos *.json* ou *.txt*, dependendo do caso.

- **words_list.json**: Trata-se da lista de ocorrências de cada palavra em cada texto. O sistema salva os dados no formato ilustrado abaixo:

```
{
    "epoca1": [
        {
            "amor": 5,
            "tempo": 3,
            "vida": 2
        },
        {
            "guerra": 4,
            "soldado": 2,
            "terra": 1
        }
    ],
    "epoca2": [
        {
            "maquina": 8,
            "industria": 6
        }
    ]
}
```