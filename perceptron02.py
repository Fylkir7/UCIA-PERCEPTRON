# Importando a biblioteca
from sklearn.linear_model import Perceptron

# Dados de Entrada

# Ensolarado, Final de Semana, Parque Lotado. 0 = não, 1 = sim

X = [[0,0,0], [0,1,0], [1,0,0], [1,1,0], [0,0,1], [0,1,1], [1,0,1], [1,1,1]]

# Dados de Saída 

# Ir ao parque? 0 = não, 1 = sim

Y = [0, 1, 1, 1, 0, 0, 0, 0]

# Criando e treinando o Perceptron

modelo = Perceptron()
modelo.fit(X, Y)

# Testando o modelo

print("Previsões:")
testes = [[0,0,0], [0,1,0], [1,0,0], [1,1,0], [0,0,1], [0,1,1], [1,0,1], [1,1,1]]
for teste in testes:
  previsao = modelo.predict([teste])
  print (f"Ensolarado: {teste[0]}, Final de Semana: {teste[1]}, Parque Lotado: {teste[2]} => Ir ao Parque? {'Sim' if previsao[0] == 1 else 'Não'}")
