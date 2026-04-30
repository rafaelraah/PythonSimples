print("Hello World");
idade=31
print(idade);

entrada = input("Digite o seu nome: ")
print ("Seu nome é:", entrada)

print("O nome", entrada, "tem", len(entrada), "caracteres. As três primeiras letras do nome", entrada, "são", entrada[:3], "e as três últimas são", entrada[-3:])
print("O nome", entrada, "de trás para a frente é", entrada[::-1])
print("Em caixa alta:", entrada.upper())
print("Em caixa baixa:", entrada.lower())
print("A primeira letra do nome", entrada, "é", entrada[0:1])