def StringComTodosOsNomes(nomes):
    retornaNomes = "";
    for item in nomes:
        retornaNomes = retornaNomes + item + " ";
    return retornaNomes;

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

nomes[2] = "Daniel"

todosNomesStr = StringComTodosOsNomes(nomes);
print("Todos os nomes da lista: " + todosNomesStr)

nomes[3] = "Fernando"
todosNomesStr = StringComTodosOsNomes(nomes);
print("Todos os nomes da lista: " + todosNomesStr)

nomes.pop(1);
todosNomesStr = StringComTodosOsNomes(nomes);
print("Todos os nomes da lista: " + todosNomesStr)

nomes.remove("Fernando");
print("Todos os nomes da lista: " + StringComTodosOsNomes(nomes))

if("Daniel" in nomes):
    nomes.remove("Daniel")
   
if("Amanda" in nomes):
    nomes.remove("Amanda")
else:
    print("O nome Amanda não está na lista, então não será removido");
   
print("Todos os nomes da lista: " + StringComTodosOsNomes(nomes))







