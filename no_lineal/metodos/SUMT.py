from scipy.optimize import minimize

# Definir la función objetivo y las restricciones
def objective_function(x):
    return (x[0] - 1)**2 + (x[1] - 2.5)**2

def constraint1(x):
    return x[0] + x[1] - 3

# Definir las condiciones iniciales
initial_guess = [0, 0]

# Resolver el problema de optimización utilizando el algoritmo SUMT
result = minimize(objective_function, initial_guess, constraints={'type': 'eq', 'fun': constraint1}, method='SLSQP')

# Imprimir los resultados
print("Solución óptima encontrada:")
print("x1 =", result.x[0])
print("x2 =", result.x[1])
print("Valor de la función objetivo en la solución óptima:", result.fun)
