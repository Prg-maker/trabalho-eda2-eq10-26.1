import processamento_de_dados as pdd
import os
from grafos import criar_grafo

words_list = {}
data_path = os.path.join('data', 'text')
savement_path = "data/processed/words_list.json"

for period in os.listdir(data_path):

    period_path = os.path.join(data_path, period)

    if os.path.isdir(data_path):

        words_list[period] = []
        for file in os.listdir(period_path):
            if file.endswith("txt"):

                file_path = os.path.join(period_path, file)
                words = pdd.load_words(file_path)
        
            frequency = {}
            for word in words:
                frequency[word] = frequency.get(word, 0) + 1

            words_list[period].append(frequency)

pdd.list_write(savement_path, words_list)

# cria um grafo para cada epoca
grafos_por_epoca = {}
for period, documentos in words_list.items():
    grafos_por_epoca[period] = criar_grafo(documentos)
    print(f"Grafo {period}: {len(grafos_por_epoca[period])} vértices")


from algoritmos import kruskal_todas_epocas, salvar_todos_resultados
resultados_kruskal = kruskal_todas_epocas(grafos_por_epoca)
salvar_todos_resultados(resultados_kruskal)