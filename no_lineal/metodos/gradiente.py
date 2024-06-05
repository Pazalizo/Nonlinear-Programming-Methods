import numpy as np
import sympy as sp

def gradient_ascent(f, grad_f, x0, alpha=0.1, tolerance=1e-5, max_iterations=1000):
    """
    Método del ascenso más pronunciado (gradiente ascendente) para maximizar una función objetivo.
    
    Parámetros:
    f            -- Función objetivo.
    grad_f       -- Gradiente de la función objetivo.
    x0           -- Punto inicial (vector numpy).
    alpha        -- Tamaño del paso.
    tolerance    -- Tolerancia para la condición de parada.
    max_iterations -- Número máximo de iteraciones.
    """
    x_k = x0

    for i in range(max_iterations):
        grad = np.array(grad_f(*x_k))  # Convertir gradiente a array de NumPy
        x_k_next = x_k + alpha * grad
        f_k = f(*x_k)
        f_k_next = f(*x_k_next)

        # Imprimir los resultados de la iteración
        print(f"Iteración {i}: x = {x_k}, f(x) = {f_k}, grad f(x) = {grad}")

        # Verificar la condición de parada
        if abs(f_k_next - f_k) < tolerance:
            x_k = x_k_next
            break

        x_k = x_k_next

    # Resultados finales
    print(f"\nPunto óptimo: x = {x_k}")
    print(f"Valor máximo de la función: f(x) = {f(*x_k)}")

def main():
    # Ingresar la función objetivo desde la consola
    func_str = input("Ingrese la función objetivo (por ejemplo, '4*x1 + 6*x2 - 2*x1**2 - 2*x1*x2 - 2*x2**2'): ")
    
    # Definir las variables simbólicas
    x1, x2 = sp.symbols('x1 x2')
    
    # Convertir la cadena de la función a una función simbólica
    f_sym = sp.sympify(func_str)
    
    # Convertir la función simbólica a una función de Python
    f = sp.lambdify((x1, x2), f_sym, 'numpy')
    
    # Calcular el gradiente de la función simbólica
    grad_f_sym = [sp.diff(f_sym, var) for var in (x1, x2)]
    
    # Convertir el gradiente simbólico a una función de Python
    grad_f = sp.lambdify((x1, x2), grad_f_sym, 'numpy')
    
    # Punto inicial
    x0 = np.array([1.0, 1.0])
    
    # Llamar a la función de ascenso más pronunciado
    gradient_ascent(f, grad_f, x0)

if __name__ == "__main__":
    main()
