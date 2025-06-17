#Faça um programa para uma caixa eletrônica. O programa deverá 
#perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão de 1, 5, 10, 50 e 100 reais. 
#O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas 
#notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece 
#notas três de 100, uma nota de 50, quatro notas de 10, uma nota de 
#5 e quatro notas de 1.

valor = int(input("Digite o valor do saque"))

resto = valor % 100
cem = valor // 100

resto = resto % 50      
cinquenta = resto // 50

resto = resto % 10        
dez = resto // 10

resto = resto % 5
cinco = resto //5       

resto = resto % 1
um = resto // 1
        
print(f"O valor {valor} gerou:\n {cem} notas de 100,\n {cinquenta} notas de 50,\n {dez} notas de 10, \n {cinco} notas de 5,\n {um} notas de 1")

#if(valor >= 10 and valor <=600):    