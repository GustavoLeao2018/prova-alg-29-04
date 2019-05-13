"""
2) Em um formulário, é perguntado ao respondente se ele trabalha na iniciativa privada, 
se ele é funcionário público, ou se é aponsentado, sendo apenas estas as opções 
válidas.
Implemente um algoritmo que agrupe as respostas a esta questão, executando no 
máximo N operações de comparação.
"""

from random import randint

lista = []
lista_opcoes = [ "Aposentado", "Funcionario Público", "Iniciativa Privada" ]

for i in range(randint(0, 100)):
    lista.append(randint(0, 2))

def pesquisa(lista): 
    tamanho = len(lista) 
    for i in range(tamanho):
        for j in range(0, tamanho-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j] 


pesquisa(lista) 
  
print("Resposta lista de locais de trabalho:")
for indice in range(len(lista)): 
    print (f"Pessoa: {indice} | Trabalho: {lista_opcoes[lista[indice]]}")

    
    """
    bubble sort: n / n²
    ordenação: n * log N
    particionamento de dikstra 
    
    """
    
    
