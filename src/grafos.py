def criar_grafo(documentos):
    
    """
    constroi um grafo de coocorrência a partir dos documentos de uma época
    cada vértice representa uma palavra e cada aresta o peso da relação entre duas palavras,
    calculado pela multiplicação de suas frequências no mesmo documento
    """
    grafo = {}
    
    for documento in documentos:
        palavras = list(documento.keys())
        
        # garante a criação de todos os vértices primeiro O(V)
        for palavra in palavras:
            if palavra not in grafo:
                grafo[palavra] = {}
                
        # cria ou incrementa as arestas com o peso multiplicativo O(E)
        for i in range(len(palavras)):
            for j in range(i + 1, len(palavras)):
                palavra_a = palavras[i]
                palavra_b = palavras[j]
                peso = documento[palavra_a] * documento[palavra_b]
                
                grafo[palavra_a][palavra_b] = grafo[palavra_a].get(palavra_b, 0) + peso
                grafo[palavra_b][palavra_a] = grafo[palavra_b].get(palavra_a, 0) + peso
                
    return grafo