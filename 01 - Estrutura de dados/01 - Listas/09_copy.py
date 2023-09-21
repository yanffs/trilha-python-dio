lista = [1, "Python", [40, 30, 20]]

lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

l2 = lista.copy()
print(l2)

print(id(l2), id(lista)) # as identidades das listas são diferentes apesas de terem o mesmo conteúdo

l2[0] = 2

print(l2)
print(lista)