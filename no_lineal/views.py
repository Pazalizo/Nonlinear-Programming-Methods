from django.shortcuts import render
from .forms import seccion_dorada_formulario, multiplicadores_formulario, cuadratica_formulario
import re
import numpy as np
import sympy as sp
from .forms import GradienteFormulario
from scipy.optimize import minimize

def seccion_dorada(request):
    if request.method == 'POST':
        form = seccion_dorada_formulario(request.POST)
        if form.is_valid():
            if 'button2' in request.POST:
                numeros_calcular = []
                filas = 0
                columnas = 2
                for key, value in request.POST.items():
                    # Ejemplo de uso
                    if (key == 'button2' or key == 'csrfmiddlewaretoken'):
                        pass
                    else:
                        filas = filas + 1
                filas = filas/2
                print(filas)
                matriz_vacia = [[None for _ in range(columnas)] for _ in range(int(filas))]
                # Imprimir todos los datos recibidos por POST en la consola
                i = 0
                j = 0
                for key, value in request.POST.items():
                    if key not in ['button2', 'csrfmiddlewaretoken']:
                        def crear_lambda(condicion_str):
                            return eval(condicion_str)
                        a = 'lambda x:' + str(value)
                        print(f'en la posicion {i}{j} se guarda {a}')
                        condicion = crear_lambda(a)
                        matriz_vacia[i][j] = condicion
                        if j == 0:
                            # Usar una expresión regular para encontrar todos los números en la cadena
                            numeros = re.findall(r'-?\d+', a)
                            # Convertir los números encontrados a enteros
                            numeros_int = list(map(int, numeros))
                            numeros_calcular.append(numeros_int)
                        j += 1
                        if j >= columnas:
                            j = 0
                            i += 1
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

                def creacion(x):
                    for condicion, funcion in matriz_vacia:
                        if condicion(x):
                            resultado = funcion(x)
                            return resultado
                        
                def encontrar_min_y_max(matriz):
                    # Inicializar los valores mínimo y máximo con None
                    min_valor = None
                    max_valor = None

                    for fila in matriz:           
                        for elemento in fila:                    
                            if min_valor is None or elemento < min_valor:
                                min_valor = elemento
                            if max_valor is None or elemento > max_valor:
                                max_valor = elemento
        
                    return min_valor, max_valor
                
                # Encontrar los valores mínimo y máximo
                min_valor, max_valor = encontrar_min_y_max(numeros_calcular)
                
                # Imprimir los resultados
                print(f'El valor mínimo es: {min_valor}')
                print(f'El valor máximo es: {max_valor}')
                print(numeros_calcular)
                x_max2 = golden_section_maximize(creacion, min_valor, max_valor)
                resultado2 = str(creacion(x_max2)) + " en x = " + str(x_max2)
                print(resultado2)
            return render(request, 'seccion_dorada.html', {'form': form, 'resultado': resultado2})
    else:
        form = seccion_dorada_formulario()
    return render(request, 'seccion_dorada.html', {'form': form})

def multiplicadores(request):
    if request.method == 'POST':
        form = multiplicadores_formulario(request.POST)
        if form.is_valid():
            if 'button2' in request.POST:
                restricciones_lambda = []
                for key, value in request.POST.items():
                    #print(key, value)
                    if key not in ['button2', 'csrfmiddlewaretoken', 'field1']:
                        
                        def crear_lambda(condicion_str):
                            return eval(condicion_str)
                        
                        def extract_letters_regex(expression):
                            return re.findall(r'[a-zA-Z]', expression)
                        
                        variables_extraidas = extract_letters_regex(value)
                        texto_auxiliar = value
                        for variable in variables_extraidas:
                            texto_auxiliar = texto_auxiliar.replace(variable, 'vars[' + str(variables_extraidas.index(variable)) + ']')
                        #print(texto_auxiliar)
                        a = 'lambda vars:' + str(texto_auxiliar)
                        print(a)
                        condicion = crear_lambda(a)
                        restricciones_lambda.append(condicion)
                        
                    if key == 'field1':
                        
                        def crear_lambda(condicion_str):
                            return eval(condicion_str)
                        
                        def extract_letters_regex(expression):
                            return re.findall(r'[a-zA-Z]', expression)
                        
                        variables_extraidas = extract_letters_regex(value)
                        texto_auxiliar = value
                        for variable in variables_extraidas:
                            texto_auxiliar = texto_auxiliar.replace(variable, 'vars[' + str(variables_extraidas.index(variable)) + ']')
                        #print(texto_auxiliar)
                        a = 'lambda vars:' + str(texto_auxiliar)
                        print(a)
                        condicion = crear_lambda(a)
                        funcion_objetivo = condicion
                      
                def create_variables_from_strings(var_names):
                    variables = {}
                    for name in var_names:
                        variables[name] = sp.symbols(name)
                    return variables

                # Crear las variables SymPy
                variables = create_variables_from_strings(variables_extraidas)

                valores = []
                for valor in variables.values():
                    valores.append(valor)
                print(valores)
                print(variables)

                # Convertir las funciones lambda en expresiones de SymPy
                objective = sp.sympify(funcion_objetivo(valores))
                constraints = [sp.sympify(c(valores)) for c in restricciones_lambda]

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
                return render(request, 'multiplicadores.html', {'form': form, 'resultado': valores, 'soluciones': soluciones})
    else:
        form = multiplicadores_formulario()
    return render(request, 'multiplicadores.html', {'form': form})

def gradient_ascent(f, grad_f, x0, alpha=0.1, tolerance=1e-5, max_iterations=1000):
    x_k = x0
    results = []

    for i in range(max_iterations):
        grad = np.array(grad_f(*x_k))  # Convertir gradiente a array de NumPy
        x_k_next = x_k + alpha * grad
        f_k = f(*x_k)
        f_k_next = f(*x_k_next)

        # Guardar los resultados de la iteración
        results.append(f"Iteración {i}: x = {x_k}, f(x) = {f_k}, grad f(x) = {grad}")

        # Verificar la condición de parada
        if abs(f_k_next - f_k) < tolerance:
            x_k = x_k_next
            break

        x_k = x_k_next

    # Resultados finales
    results.append(f"\nPunto óptimo: x = {x_k}")
    results.append(f"Valor máximo de la función: f(x) = {f(*x_k)}")
    
    return results

def gradiente(request):
    if request.method == 'POST':
        form = GradienteFormulario(request.POST)
        if form.is_valid():
            funcion_objetivo = form.cleaned_data['funcion_objetivo']
            
            # Definir las variables simbólicas
            x1, x2 = sp.symbols('x1 x2')
            
            # Convertir la cadena de la función a una función simbólica
            f_sym = sp.sympify(funcion_objetivo)
            
            # Convertir la función simbólica a una función de Python
            f = sp.lambdify((x1, x2), f_sym, 'numpy')
            
            # Calcular el gradiente de la función simbólica
            grad_f_sym = [sp.diff(f_sym, var) for var in (x1, x2)]
            
            # Convertir el gradiente simbólico a una función de Python
            grad_f = sp.lambdify((x1, x2), grad_f_sym, 'numpy')
            
            # Punto inicial
            x0 = np.array([1.0, 1.0])
            
            # Llamar a la función de ascenso más pronunciado
            resultados = gradient_ascent(f, grad_f, x0)
            
            print(resultados[-1])
            
            return render(request, 'gradiente.html', {'form': form, 'resultado': resultados[-1]})
    else:
        form = GradienteFormulario()
    return render(request, 'gradiente.html', {'form': form})

def cuadratica(request):
    if request.method == 'POST':
        form = cuadratica_formulario(request.POST)
        if form.is_valid():
            if 'button2' in request.POST:
                for key, value in request.POST.items():
                    #print(key, value)
                    if key == 'field1':
                        funcion_objetivo = value
                    if key == 'field2':
                        restriccion = value
                # Solicitar al usuario que ingrese la función objetivo y la restricción
                print(funcion_objetivo)
                print(restriccion)
                objective_function_str = funcion_objetivo
                constraint_str = restriccion

                # Convertir las cadenas de texto a expresiones simbólicas
                x1, x2 = sp.symbols('x1 x2')
                objective_function_expr = sp.sympify(objective_function_str)
                constraint_expr = sp.sympify(constraint_str)

                # Definir la función objetivo y la restricción
                def objective_function(x):
                    return -objective_function_expr.subs({x1: x[0], x2: x[1]})

                def constraint(x):
                    return constraint_expr.subs({x1: x[0], x2: x[1]})

                x0 = [0.5, 0.5]
                result = minimize(objective_function, x0, constraints={'type': 'ineq', 'fun': constraint})

                # Imprimir los resultados
                print("Solución óptima aproximada:")
                print("x1 =", result.x[0])
                print("x2 =", result.x[1])
                print("Valor óptimo de la función objetivo f(x) =", -result.fun)

        return render(request, 'programacion_cuadratica.html', {'form': form, 'resultado': -result.fun})
    else:
        form = cuadratica_formulario()
    return render(request, 'programacion_cuadratica.html', {'form': form})


def combinaciones_lineales(request):
    return render(request, 'combinaciones_lineales.html')

def programacion_estocastica(request):
    return render(request, 'programacion_estocastica.html')

def programacion_separable(request):
    return render(request, 'programacion_separable.html')

def sumt(request):
    return render(request, 'sumt.html')
    