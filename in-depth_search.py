#
"""
:)
BUSCA EM PROFUNDIDAE USANDO PILHA,IMPLEMENTACAO USADNO MATRIZ DE ADJCENCIA E NA VERSAO INTERATIVA
*NAO COMECANDO EM UM NO ESPECIFICO MAIS SIM NA RAIZ NESTA IMPLEMENTACAO , IMPLENTACAO NUM GRAFO NAO DIRENCIONADO E CONTANDO QUE NAO TEM REPETICAO
PASSO 1 : PEGAR UM VERTICE INICAL FAZER A VERIFICAÇÃO QUE QUISER E GUARDA AS INFROMAÇÔES DO CAMINHO QUE QUISER 
PASSO 2 : VERIFICAR TODOS OS VIZINHOS DESTE VERTIFICE E MARCAR OS QUE NÃO FORAM VISITADOS NUMA PILHA 

"""

graph = list(list()) #preencher o grafo como quiser

def dfs(graph,findItem) :
 y = 0
 notFind = True
 visited = set()
 while notFind :
  for x in range(graph) :
      while graph[x][y] == 0 or graph[x][y] in visited :
          if graph[x][y] == findItem : return "find on [{},{}] ".formart(x,y)
          else:
            visited.add(graph[x][y])
            y += 1
       

#chamar dfs como quiser   
 
      
    

