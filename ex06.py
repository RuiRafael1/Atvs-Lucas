num = int(input("Digite um número para saber sua tabuada"))
num3 = int(input("Digite até onde começai"))

num2 = int(input("Digite até onde o for vai"))

for i in range(num3,num2+1):
    print(f"{num} X {i} = {i*num3}")