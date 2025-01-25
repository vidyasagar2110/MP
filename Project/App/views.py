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
from django.http import HttpResponse

def simplex_solver(request):
    if request.method == "POST":
        num_vars = int(request.POST.get("num_vars"))
        num_constraints = int(request.POST.get("num_constraints"))
        optimization = request.POST.get("optimization")  # Maximize or Minimize

        # Parse objective function coefficients (c1, c2, ..., cn)
        c = [float(request.POST.get(f"c{i+1}")) for i in range(num_vars)]

        # Parse constraints (a1_1, a1_2, ..., a1_n, b1, a2_1, ..., b2, ...)
        A = []
        b = []
        for i in range(num_constraints):
            A.append([float(request.POST.get(f"a{i+1}_{j+1}")) for j in range(num_vars)])
            b.append(float(request.POST.get(f"b{i+1}")))

        # Convert to numpy arrays
        c = np.array(c)
        A = np.array(A)
        b = np.array(b)

        # Adjust for minimization (convert to maximization)
        if optimization == "minimize":
            c = -c

        # Solve using the Simplex method
        solution, optimal_value = simplex(c, A, b)

        # Adjust result back for minimization
        if optimization == "minimize":
            optimal_value = -optimal_value

        return render(request, "simplex_result.html", {
            "solution": solution,
            "optimal_value": optimal_value,
        })

    return render(request, "simplex_form.html")


def simplex(c, A, b):
    """Simplex method implementation."""
    num_constraints, num_variables = A.shape
    slack_vars = np.eye(num_constraints)
    tableau = np.hstack((A, slack_vars, b.reshape(-1, 1)))
    obj_row = np.hstack((-c, np.zeros(num_constraints + 1)))
    tableau = np.vstack((tableau, obj_row))
    num_total_vars = num_variables + num_constraints

    while True:
        if all(tableau[-1, :-1] >= 0):
            break
        pivot_col = np.argmin(tableau[-1, :-1])
        ratios = tableau[:-1, -1] / tableau[:-1, pivot_col]
        ratios[ratios <= 0] = np.inf
        pivot_row = np.argmin(ratios)
        if np.all(ratios == np.inf):
            raise ValueError("The problem is unbounded.")
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
