import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, exp, diff, lambdify

#função newton
def Newton(f, df, x, epsilon, Iter):
  #checa de f(x) é maior que a tolerancia
  if abs(f(x)) <= epsilon:
    return x
  
  #inicia contador
  k = 1
  
  #loop enquanto k dentro do limite de iterações
  while k <= Iter:
    
    #x1 é a solução, recebe o chute inicial - f(chute)/derivada de f(chute)
    x1 = x - f(x)/df(x)

    #se f(solucao)<= tolerância retorna x1
    if abs(f(x1)) <= epsilon:
      return(x1)
    
    #atualiza x para a solucao atual e k para k+1
    x = x1
    k = k+1
    #mensagem de erro
  print("Erro: máximo de iterações atingido")
  return x1

#vetor y
y_dados = [10.179, 10.073, 10.505, 10.022, 10.041, 10.557, 10.147, 10.408, 9.785, 9.860]

#função f
mu = symbols('mu')
n = len(y_dados)
soma = sum((y_i - mu)**2 / (mu**2 * y_i) for y_i in y_dados)
f_sim = soma - 1/2

#derivada
df_sim = diff(f_sim, mu)

#converter funções para numéricas 
f_num = lambdify(mu, f_sim, 'numpy')
df_num = lambdify(mu, df_sim, 'numpy')

#chute aleatório
chute_inicial = 20 
#chama newton
raiz = Newton(f_num, df_num, chute_inicial, 0.0001, 50) 
print(round(raiz, 3))

#checagem
print(f_num(35.295))