# Importando a biblioteca
from sklearn.linear_model import Perceptron

# Dados de Entrada

# Cansado, Ingredientes em casa, Restaurante aberto, Pagamento recente. 0 = não, 1 = sim

X = [[0,1,1,1], [1,0,1,1], [1,0,0,1], [0,0,1,0], [1,1,1,1], [0,1,0,0], [1,0,0,1], [0,0,0,1]]

# Dados de Saída 

# Comer fora? 0 = não, 1 = sim

Y = [0,1,0,1,1,0,0,0]

# Criando e treinando o Perceptron

modelo = Perceptron()
modelo.fit(X, Y)

# Testando o modelo

print("Previsões:")
testes = [[0,1,1,1], [1,0,1,1], [1,0,0,1], [0,0,1,0], [1,1,1,1], [0,1,0,0], [1,0,0,1], [0,0,0,1]]
for teste in testes:
  previsao = modelo.predict([teste])
  print (f"Cansado: {teste[0]}, Ingredientes em casa: {teste[1]}, Restaurante aberto: {teste[2]}, Pagamento recente: {teste[3]} => Comer fora? {'Sim' if previsao[0] == 1 else 'Não'}")
