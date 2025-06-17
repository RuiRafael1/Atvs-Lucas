#criando um vetor com números
vetor = [1,2,3,4,5]
print(vetor)

print(vetor[0])
print(vetor[4])
#Adicionando elementos
vetor.append(6)

frutas = ['maça', 'banana']
frutas.append('laranja')

print(frutas) 

#removendo elementos
vetor.remove(2)
print(vetor)
frutas.remove('maça')
print(frutas)
#tamanho do vetor
print(len(vetor))
print(len(frutas))

#percorrer o vetor
for i in vetor:
    print(i)