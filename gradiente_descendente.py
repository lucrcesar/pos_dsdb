import numpy as np

def grad_des(fx, x1, y, m, alpha, max_iter=100, tol=1e-04):
    # Cria uma matriz solução
    solucao = np.full((max_iter, len(x1)), np.nan)
    # Recebe x1, um vetor com um chute inicial
    solucao[0] = x1
    
    # Loop for preenche a matriz com soluções
    for i in range(max_iter-1):
        solucao[i+1] = solucao[i] - alpha * fx(solucao[i], y, m)
        solucao[i+1] = np.clip(solucao[i+1], 0.01, 0.99)
        # Critério de parada
        if np.sum(np.abs(solucao[i+1] - solucao[i])) <= tol:
            break
    print(solucao)
    return solucao

# Função f(x)
y = np.array([4, 6, 5, 7, 7, 2, 5, 7, 5, 5])
m = 7
mu_inicial = max(y/m) + 0.05

def fx(mu, y, m):    
    mu = np.array(mu)
    if np.any(mu <= 0) or np.any(mu >= 1):
        return np.inf
    
    # Verificar se argumentos dos logs são positivos
    if np.any((y / m) / mu <= 0) or np.any((1 - y / mu) <= 0) or np.any((1 - mu) <= 0):
        return np.inf
    
    resultado = 2 * np.sum(y * np.log((y / m) / mu) + (m - y) * np.log((1 - y / mu) / (1 - mu)))
    return resultado - 3.84

# Chama a função grad_des
sol_grad = grad_des(fx=fx, x1=np.array([mu_inicial]), y = y,  m = m, alpha=0.001, max_iter=140)

# Pega a última solução não vazia
ultima_solucao = sol_grad[~np.isnan(sol_grad).any(axis=1)][-1]
print(fx(ultima_solucao, y, m))