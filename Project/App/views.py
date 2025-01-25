from django.shortcuts import render
import numpy as np
def home(request):
    return render(request, 'home.html')

def graphical_method(request):
    return render(request, 'graphical_method.html')

def simplex_method(request):
    return render(request, 'simplex_method.html')

def graphical_steps(request):
    return render(request, 'graphical_steps.html')

def graphical_solve(request):
    return render(request, 'graphical_solve.html')

def graphical_application(request):
    return render(request, 'graphical_application.html')

def simplex_steps(request):
    return render(request, 'simplex_steps.html')

def simplex_solve(request):
    return render(request, 'simplex_solve.html')

def simplex_application(request):
    return render(request, 'simplex_application.html')
from django.shortcuts import render
import numpy as np

from django.shortcuts import render
import numpy as np

from django.shortcuts import render
import numpy as np

def simplex(c, A, b, maximize=True):
    num_constraints, num_variables = A.shape
    slack_vars = np.eye(num_constraints)
    tableau = np.hstack((A, slack_vars, b.reshape(-1, 1)))
    obj_row = np.hstack(((-1 if maximize else 1) * c, np.zeros(num_constraints + 1)))
    tableau = np.vstack((tableau, obj_row))
    num_total_vars = num_variables + num_constraints

    while True:
        if all(tableau[-1, :-1] >= 0):
            break
        pivot_col = np.argmin(tableau[-1, :-1])
        ratios = tableau[:-1, -1] / tableau[:-1, pivot_col]
        ratios[ratios <= 0] = np.inf
        if np.all(ratios == np.inf):
            raise ValueError("The problem is unbounded.")
        pivot_row = np.argmin(ratios)

        if tableau[pivot_row, pivot_col] == 0:
            raise ValueError("Division by zero detected in pivot element.")

        pivot_element = tableau[pivot_row, pivot_col]
        tableau[pivot_row, :] /= pivot_element

        for i in range(tableau.shape[0]):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, pivot_col] * tableau[pivot_row, :]

    solution = np.zeros(num_total_vars)
    for i in range(num_constraints):
        basic_var_index = np.where(tableau[i, :-1] == 1)[0]
        if len(basic_var_index) == 1 and basic_var_index[0] < num_total_vars:
            solution[basic_var_index[0]] = tableau[i, -1]

    optimal_value = tableau[-1, -1]
    return solution[:num_variables], optimal_value

def simplex_solver(request):
    if request.method == 'POST':
        maximize = request.POST.get('type') == 'maximize'
        num_variables = int(request.POST.get('variables'))
        c = np.array([float(x) for x in request.POST.get('objective').split()])
        constraints = request.POST.getlist('constraints')
        print("Constraints: ", constraints)  # Debug print
        A = []
        b = []
        for constraint in constraints:
            parts = constraint.split()
            print("Parts: ", parts)  # Debug print
            A.append([float(x) for x in parts[:-1]])
            b.append(float(parts[-1]))
        A = np.array(A)
        b = np.array(b)
        print("Matrix A: ", A)  # Debug print
        print("Vector b: ", b)  # Debug print
        try:
            solution, optimal_value = simplex(c, A, b, maximize)
            print("Solution: ", solution)  # Debug print
            print("Optimal Value: ", optimal_value)  # Debug print
            return render(request, 'simplex_result.html', {'solution': solution.tolist(), 'optimal_value': optimal_value})
        except ValueError as e:
            return render(request, 'simplex_result.html', {'error': str(e)})
    return render(request, 'simplex_solve.html')

