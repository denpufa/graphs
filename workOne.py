from math import sqrt
vertices = 0
grafo = 0


arquivo_path = './dados.txt'

#grafo onde armazenha os valores entre as arestas
def carregarGrafo(teste,grafoTeste):
  vertices = teste
  grafo = [[0]*vertices for x in range(vertices)]
  for x in range(len(grafo)):
    for y in range(len(grafo[x])):
      aresta = grafoTeste[x][y]
      if aresta > 0 :
        grafo[x][y] = aresta


# usando floyd-warshall
#retorna o caminho
def menor(inicial,presiso_pegar) :
  for k in range(len(grafo)) :
    for i in range(len(grafo)) :
      for j in range(len(grafo)) :
          if grafo[i][j] > grafo[i][k] + grafo[k][j] :
            grafo[i][j] = grafo[i][k] + grafo[k][j]
  melhor = list()
  melhor.append(inicial)
  i = inicial 
  while(len(melhor) != presiso_pegar) :
    menor = 10*10**5
    menor_indice = 0
    for x in range(len(presiso_pegar)):
      if grafo[i][presiso_pegar[x]] < menor:
        menor = grafo[i][presiso_pegar[x]]
        menor_indice = x
    melhor.append(menor_indice)
    del presiso_pegar[x]
  return melhor   

  

  
#Salva em um arquivo a saída para recordar o teste
def SalvarOutput(valorDeTeste):
  arquivo = open("teste.txt", "a")
  arquivo.write("-----SÁIDA DO TESTE--------")
  arquivo.write(str(valorDeTeste))


def melhorCaminho(inicial,presiso_pegar):
  res = menor(inicial,presiso_pegar)
  print('Um bom caminho paa  essa sequência de pratileiras  é : ',res)
  SalvarOutput(res)

def carregarTudoDeArquivo():
  arquivo_aberto  = open(arquivo_path,'rb')
  line_count = 0
  for line in arquivo_aberto.readlines() :
    if line_count == 0 :
      vertice = line[0]
      numeros = line[1:].split()
      grafo = [[0]*sqrt(numeros) for x in range(sqrt(numeros))]
      i = 0
      for x in sqrt(numeros):
        for y in sqrt(numeros):
          grafo[x][y] = numeros[i]
          i += 1
      line_count += 1
    if line_count == 2:
      presiso_pegar4 = [int(x) for x in line.split()]



      
  

#interface de teste
grafoTeste1 = [[0,5,9],[5,0,7],[9,7,0]]
presiso_pegar1 = [0,3]
grafoTeste2 = [[0,1,2,3,4],[1,0,2,3,4],[2,2,0,3,4],[3,3,3,0,4],[4,4,3,4,0]]
presiso_pegar2 = [1,5,3]
grafoTeste3 = [[0,3],[3,0]]
presiso_pegar3 = [0,1] 
presiso_pegar4 = []

print("Escolha o caso de teste entre os 3 possives e veja os valores de entrada deles")
print("Caso 1 Digite 1")
print("Caso 2 digite 2")
print("caso 3 digite 3")
print("testar do arquivo digite 4")
caso = input()
if caso == '1' :
  carregarGrafo(3,grafoTeste1)
  print("dados de entrada grafo:",grafoTeste1,"passar nas seguintes pratileiras: ",presiso_pegar1)
  melhorCaminho(0,presiso_pegar1)
elif caso == '2' :
  carregarGrafo(5,grafoTeste2)
  print("dados de entrada grafo:",grafoTeste2,"passar nas seguintes pratileiras: ",presiso_pegar2)
  melhorCaminho(3,presiso_pegar2)
elif caso == '3' :
  carregarGrafo(2,grafoTeste3)
  print("dados de entrada grafo:",grafoTeste3,"passar nas seguintes pratileiras: ",presiso_pegar3)
  melhorCaminho(1,presiso_pegar3)
elif caso == '4':
  carregarTudoDeArquivo()
  print("dados de entrada",grafo,presiso_pegar4)
  melhorCaminho(0,presiso_pegar4)
else:  
  print("caso de teste não encontrado")






    
  
    

    





