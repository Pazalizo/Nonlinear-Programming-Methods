from scipy.optimize import minimize
import sympy as sp

# Solicitar al usuario que ingrese la función objetivo y la restricción
objective_function_str = input("Ingrese la función objetivo en términos de x1 y x2: ")
constraint_str = input("Ingrese la restricción en términos de x1 y x2: ")

# Convertir las cadenas de texto a expresiones simbólicas
x1, x2 = sp.symbols('x1 x2')
objective_function_expr = sp.sympify(objective_function_str)
constraint_expr = sp.sympify(constraint_str)

# Definir la función objetivo y la restricción
def objective_function(x):
    return -objective_function_expr.subs({x1: x[0], x2: x[1]})

def constraint(x):
    return constraint_expr.subs({x1: x[0], x2: x[1]})

# Definir el punto inicial
x0 = [0.5, 0.5]

# Resolver el problema de optimización
result = minimize(objective_function, x0, constraints={'type': 'ineq', 'fun': constraint})

# Imprimir los resultados
print("Solución óptima aproximada:")
print("x1 =", result.x[0])
print("x2 =", result.x[1])
print("Valor óptimo de la función objetivo f(x) =", -result.fun)
