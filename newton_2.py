import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, exp, diff, lambdify

def newton_sistema(F, J, x0, tol=0.0001, max_iter=100):
    x = np.array(x0, dtype=float)
    
    for i in range(max_iter):
        # Avaliar F e J no ponto atual
        Fx = np.array([f(*x) for f in F])
        Jx = np.array([[j(*x) for j in row] for row in J])
        
        # Resolver J * delta = -F
        delta = np.linalg.solve(Jx, -Fx)
        
        x_new = x + delta
        
        if np.linalg.norm(delta) < tol:
            return x_new
        
        x = x_new
    
    return x

# Definir funções e Jacobiana numericamente
x_sym, y_sym = symbols('x y')
f1_sym = x_sym + y_sym - x_sym*y_sym + 2
f2_sym = x_sym * exp(-y_sym) - 1

f1_num = lambdify([x_sym, y_sym], f1_sym, 'numpy')
f2_num = lambdify([x_sym, y_sym], f2_sym, 'numpy')

# Jacobiana
J11 = diff(f1_sym, x_sym)
J12 = diff(f1_sym, y_sym)
J21 = diff(f2_sym, x_sym)
J22 = diff(f2_sym, y_sym)

J11_num = lambdify([x_sym, y_sym], J11, 'numpy')
J12_num = lambdify([x_sym, y_sym], J12, 'numpy')
J21_num = lambdify([x_sym, y_sym], J21, 'numpy')
J22_num = lambdify([x_sym, y_sym], J22, 'numpy')

F = [f1_num, f2_num]
J = [[J11_num, J12_num], [J21_num, J22_num]]

# Chute inicial
x0 = [0.5, 0.5]  # exemplo
raiz = newton_sistema(F, J, x0)
print(f"x = {raiz[0]:.3f}, y = {raiz[1]:.3f}")

x_calc, y_calc = 0.098, -2.325
print(f1_num(x_calc, y_calc))  # Deve ser ~0
print(f2_num(x_calc, y_calc))  # Deve ser ~0