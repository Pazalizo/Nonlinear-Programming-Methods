from scipy.optimize import minimize

# Definir la función objetivo y las restricciones
def objective_function(x):
    return -(4*x[0] + 6*x[1] - 2*x[0]**2 - 2*x[0]*x[1] - 2*x[1]**2)

def constraint1(x):
    return 2 - x[0] - 2*x[1]

# Definir el punto inicial
x0 = [0.5, 0.5]

# Resolver el problema de optimización
result = minimize(objective_function, x0, constraints={'type': 'ineq', 'fun': constraint1})

# Imprimir los resultados
print("Solución óptima aproximada:")
print("x1 =", result.x[0])
print("x2 =", result.x[1])
print("Valor óptimo de la función objetivo f(x) =", -result.fun)
