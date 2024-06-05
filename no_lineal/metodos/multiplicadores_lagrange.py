import sympy as sp

def create_variables_from_strings(var_names):
    variables = {}
    for name in var_names:
        variables[name] = sp.symbols(name)
    return variables

# Definir los nombres de las variables
var_names = ['x', 'y', 'z']

# Crear las variables SymPy
variables = create_variables_from_strings(var_names)

valores = []
for valor in variables.values():
    valores.append(valor)
print(valores)
print(variables)

# Definir la función objetivo y las restricciones como funciones lambda
objective_lambda = lambda vars: vars[0]**2 + vars[1]**2 + vars[2]**2
constraints_lambda = [
    lambda vars: 2*vars[0] - 2*vars[1] - vars[2] - 5,
    lambda vars: vars[0] + vars[1] + vars[2] - 3
]

# Convertir las funciones lambda en expresiones de SymPy
objective = sp.sympify(objective_lambda(valores))
constraints = [sp.sympify(c(valores)) for c in constraints_lambda]

# Función para calcular los multiplicadores de Lagrange
def lagrange_multipliers(objective, constraints):
    # Definir las variables y los multiplicadores de Lagrange
    variables = list(objective.free_symbols)
    lambdas = sp.symbols(f'λ:{len(constraints)}')
    
    # Definir la función de Lagrange
    L = objective + sum(lambdas[i] * constraints[i] for i in range(len(constraints)))

    # Calcular las derivadas parciales
    derivs = [sp.diff(L, var) for var in variables]
    derivs += [sp.diff(L, lam) for lam in lambdas]

    # Resolver el sistema de ecuaciones
    sol = sp.solve(derivs, variables + list(lambdas), dict=True)

    # Verificar y extraer las soluciones de manera segura
    soluciones = []
    if isinstance(sol, list) and all(isinstance(s, dict) for s in sol):
        for s in sol:
            try:
                solucion = {var: s[var] for var in variables}
                soluciones.append(solucion)
            except KeyError as e:
                print(f"Variable faltante en la solución: {e}")
                continue
    else:
        print("Soluciones no están en el formato esperado")

    # Calcular el valor de la función en los puntos críticos
    valores = [objective.subs(sol) for sol in soluciones]

    return soluciones, valores

# Calcular los multiplicadores de Lagrange
soluciones, valores = lagrange_multipliers(objective, constraints)

# Imprimir las soluciones
print("Soluciones:", soluciones)
print("Valores de la función en los puntos críticos:", valores)
