numeros = [10, 20, 30]
nomes = ["Rafael", "Pedro", "Bruno"]

#Adicionando elementos na lista
nomes.append("Rogério")
nomes.insert(0, "Rodolfo")

print("Quantidade: ", len(nomes))
print("Primeiro nome da lista:", nomes[0])
print("Último nome da lista", nomes[-1])

todosNomesStr = "";
for item in nomes:
    todosNomesStr = todosNomesStr + item + " ";

print("Todos os nomes da lista: " + todosNomesStr)