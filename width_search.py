import queue
"""
  :)
*ENQUANTO HOUVER VERTICES NA FILA
PASSO 1 :  SALVE NUMA VARIAVEL E REMOVA UM VERTICE V DA FILA
PASSO 2 : SE V AINDA NÃO TIVER SENDO VISITADO
PASSO 3 : MARQUE V COMO VISITADO (SALVANDO EM ALGUM LUGAR )
PASSO 4 : VEJA SE É OQ VC QUER DEPENDENDO DO CONTEXTO DA QUESTÃO
PASSO 5 : COLOQUE TODOS OS FILHOS DE V QUE AINDA NÃO FORAM VISITADOS NA FILA
USANDO UMA FILA 

GRAFO IMPLEMENTADO USANDO UMA LIST DENTRO DE OUTRA LIST (MATRIZ DE ADJACENCIA)
FAZENDO A BUSCA NO GRAFO TODO COMECANDO DA RAIZ SEM PONTO DE PARTIDA 
USANDO ITERACAO
"""

from queue import Queue

graph = list(list()) #preencher o grafo como quiser

def bfs(graph,findItem) :
  fila = Queue()
  visited = set()
  start,y = graph[0][1],0
  fila.put(start)
  while len(fila) != 0 :
     v = fila.get()
     if v in visited : continue
     else :
      if v == findItem : return "number of visiteds before find {}".format(len(visited)) 
      else: 
        visited.add(v)
        for x in graph[y] :
          fila.put(x)
        y += 1
 
#chamar a bfs 

          
     
        
            
            
            
         
          
         
          
         
  





