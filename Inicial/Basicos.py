variavel = "lalalalala"
variavel_case = "cacacacaca"

# Comentariossssssss

variavel.upper()
variavel_case.lower()

variavel_numero = 23

str(variavel_numero)

lista = ["Abner", "Silva", "Barbosa", 10]
print(len(lista[:2]))

objeto_ou_dicionario = {"nome": "Abner", "sobrenome": "Silva", "idade": 18, "Cidade": "São Paulo"}

del objeto_ou_dicionario["idade"]
print(objeto_ou_dicionario)

lista_de_numeros = [1, 2, 3, 4, 5]
for numero in lista_de_numeros:
    print(numero)

a = 2
if a > 1:
    print("A é maior que 1")
elif a == 1:
    print("A é igual a 1")
else:
    print("A é menor que 1")
