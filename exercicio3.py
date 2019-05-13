"""
3) Dada uma matriz de 0s e 1s, como no exemplo:

    000000
    011000
    011010
    000010
    000010

Implemente um programa que conta o número de ilhas de 1s na matriz. "Ilhas" são grupos de 1s contíguos. Os grupos de 1 que formam ilhas devem estar conectados apenas na horizonta ou vertical, e não na diagonal. Por exemplo a seguinte matriz possui apenas uma ilha:

   0000
   0110
   0110
   0000

Já o exemplo a seguir mostra duas ilhas:

   0000
   0100
   0010
   0000

E neste exemplo, o resultado esperado é 2:

   1100
   1100
   0010
   0000
   """


matriz = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0]
]

for l in range(5):
    for c in range(6):
        print(f"{matriz[l][c]}", end=" ")
    print()

def procura(matriz, linha=0, coluna=0, cont_uns=0):
    if linha != len(matriz):
        print(f"{matriz[linha][coluna]}", end=" ")

      

                
        coluna += 1
        if coluna == len(matriz[linha]):
            print()
            coluna = 0
            linha += 1
        
            aux_linha = linha + 1
            aux_coluna = coluna + 1
            if matriz[linha][coluna] == matriz[aux_linha][aux_coluna]  or matriz[linha][coluna] == matriz[linha][aux_coluna]:
                cont_uns += 1

        # print(cont_uns)
        procura(matriz, linha=linha, coluna=coluna, cont_uns=cont_uns)

procura(matriz)


"""
correção

Varrer matriz
se achar 1:
    conta ilha
se 

se for 0: retorna
senão: 
pinta de 0
recurção(x-1, y)
recurção(x+1, y)
recurção(x, y-1)
recurção(x, y+1)


floodfill
""""


def conta_ilha(matriz):
    contador = 0
    for i in range(len(matriz)):
        for y in range(len(matriz[0])):
            if matriz[x][y] == 1:
                contador += 1
                floodfill(matriz,x,y)
    return contador

def floodfill(matriz,x,y):
    # testa se está na matriz
    if x < 0 or y len(matriz): return 
    if y < 0 or y len(metriz): return
    #condição de parada
    if matriz[x][y] == 0:return
    # recurção
    matriz[x][y]=0
    floodfill(matriz,x-1,y)
    floodfill(matriz,x+1,y)
    floodfill(matriz,x,y+1)
    floodfill(matriz,x,y-1)
    
    
# custo de algoritimos

    
    
    
    
    
