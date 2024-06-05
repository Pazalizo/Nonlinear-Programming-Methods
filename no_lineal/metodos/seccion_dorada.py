import numpy as np

def golden_section_maximize(f, a, b, tol=1e-5):
    phi = (1 + np.sqrt(5)) / 2  # Golden ratio
        
    c = b - (b - a) / phi
    d = a + (b - a) / phi
        
    while abs(c - d) > tol:
        if f(c) < f(d):
             a = c
        else:
            b = d
                
        c = b - (b - a) / phi
        d = a + (b - a) / phi
            
    return (b + a) / 2
    
def objective_function(x):
    if 0 <= x <= 2:
        return 3 * x
    elif 2 < x <= 3:
        return (1/3) * (-x + 20)
    else:
        return float('-inf')

funciones_condiciones = [
    ((lambda x: 0 <= x <= 2), lambda x: 3 * x),
    ((lambda x: 2 < x <= 3), lambda x: (1/3) * (-x + 20))
]
print(funciones_condiciones)
x = 2.0000130601451205  # Puedes cambiar este valor para probar diferentes casos
def creacion(x):
    for condicion, funcion in funciones_condiciones:
        if condicion(x):
            resultado = funcion(x)
            return resultado

resultado1 = creacion(x)
print(resultado1)

x_max = golden_section_maximize(objective_function, 0, 3)
x_max2 = golden_section_maximize(creacion, 0, 3)
resultado2 = str(creacion(x_max2)) + " en x = " + str(x_max2)
resultado = str(objective_function(x_max)) + " en x = " + str(x_max)

print(resultado)
print(resultado2)
        
