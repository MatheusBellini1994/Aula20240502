print('Olá mundo!')
nome = 'Matheus'
sobrenome = 'Bellini'
print('Bem vindo,', nome, sobrenome + "!")


#Quando a variável tem um valor fixo dentro do programa ela é chamdada de constante
x = 7
y = 9
media = (x + y)/2
print('A média entre', x, 'e', y, 'é', media)
# VARIOS
# COMENTARIOS



titulo = 'Taxímetro'
print(f"{titulo:^30}")

preco_km = 5.50
# quant_km = 7.2
quant_km = float(input("Qual a quantidade de quilômetros rodados? "))
# custo_viagem = preco_km * float(quant_km)
custo_viagem = preco_km * quant_km
print("O custo da viagem foi R$", custo_viagem)

print("O custo da viagem foi R${custo_viagem:.2f}.")

print(f"O custo da viagem foi R${custo_viagem:.2f}.")



fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

celsius = (5/9)*(fahrenheit-32)

print(f"{fahrenheit}ºF corresponde a {celsius}ºC")
