1. Justifique por que diversos ambientes de programação disponibilizam algoritmos baseados no Merge Sort como algoritmo de ordenação de elementos por comparação, e qual as vantagens e desvantagens desses algoritmos sobre o Quicksort.


O merge sorge, é mais utilizado por gastar memória, mas compoucos processamentos (menos comparações)
dividindo em pequenos problemas (em dividindo o array em dois), 
recursivamente (por isso o gasto de memória) e após juntando o resultado do array. 
Por isso é mais utilizado pelas linguagens.

Portanto, possui vantagens como:

- funcionar em qualquer tamanho de matriz, ao contrario do quicksort que é recomendado para matrizes menores.
- é bem veloz, por conseguir trabalhar com um tamanho grande dados
- estavel, necessita no pior caso de O(n log).

E desvantagens:

- Divide o array em mais partes ao contrario do merge.
- trabalha melhor com matrizes pequenas.
- não necessita de memória externa ao contrario do merge que necessita para fazer as comparações das 
sublistas criadas.

---- 
# Correção

- estabilidade de chaves
- garantia do tempo de execução
