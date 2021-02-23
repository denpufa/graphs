vertices = 0
grafo = 0
caminhos = dict()

#grafo onde armazenha os valores entre as arestas
def carregarGrafo(teste,grafoTeste):
  vertices = teste
  grafo = [[0]*vertices for x in range(vertices)]
  for x in range(len(grafo)):
    for y in range(len(grafo[x])):
      aresta = grafoTeste[x][y]
      if aresta > 0:
        grafo[x][y] = aresta


#dijkstra
#retorna quantos foram pegos no decorrer do menor caminho
def menor(inicial,final):
  pass


def salvarCaminho(final,caminho):
  caminhos[final] = caminho

def melhorCaminho(inicial,presiso_pegar):
  quantos_pegos_no_menor,final_menor =  0,0
  for x in presiso_pegar:
    caminho_pegando = menor(inicial,x)
    if caminho_pegando > quantos_pegos_no_menor :
      quantos_pegos_no_menor = caminho_pegando 
      final_menor = x
  print('Um bom caminho é começãr por essa sequência de pratileiras : ',caminhos[final_menor] )

#interface de teste
grafoTeste1 = [[0,5,9],[5,0,7],[9,7,0]]
grafoTeste2 = [[0,1,2,3,4],[1,0,2,3,4],[2,2,0,3,4],[3,3,3,0,4],[4,4,3,4,0]]
grafoTeste3 = [[0,3],[3,0]] 
print("Escolha o caso de teste entre os 3 possives e veja os valores de entrada deles")
print("Caso 1 Digite 1")
print("Caso 2 digite 2")
print("caso 3 digite 3")
caso = input()
if(caso == '1'):
  carregarGrafo(3,grafoTeste1)
elif(caso == '2'):
  carregarGrafo(5,grafoTeste2)
elif(caso == '3'):
  carregarGrafo(2,grafoTeste3)
else:
  print("caso de teste não encontrado")






    
  
    

    





