nota1 = float(
    input("Digite uma nota"))

nota2 = float(
    input("Digite a segunda nota")),
media = float(nota1+nota2)/2

if(media >=7 ):
    print( f"Sua nota é: {media}, Passou de ano")
elif(media<=5):
    print( f"Sua nota é {media}, Reprovou de ano")
else:
    print( f"Fciou de recuperação")