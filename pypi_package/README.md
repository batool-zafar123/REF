# Matrix Solver (`matrix-solver-ref`)

A simple, beginner-friendly Python library for linear algebra and matrix operations. Unlike complex scientific libraries, `matrix-solver-ref` provides straightforward functions to compute Row Echelon Form (REF), Reduced Row Echelon Form (RREF), solve linear systems, check consistency, and visualize 2D equations with zero boilerplate.

## Installation

```bash
pip install matrix-solver-ref
```

## Quick Start

Import the library using either `matrix_solver_ref` or `ref`:

```python
import matrix_solver_ref as msr  # or: import ref as msr
```

---

## Beginner-Friendly Functions

Each function can be used **programmatically** (passing a matrix directly) or **interactively** (calling without arguments to be guided through terminal prompts).

### 1. Convert Matrix to Row Echelon Form (`to_ref`)
Transforms any matrix into Row Echelon Form (REF) using Gaussian elimination.

```python
matrix = [
    [2.0, 1.0, -1.0],
    [-3.0, -1.0, 2.0],
    [-2.0, 1.0, 2.0]
]

# Get the REF matrix (returns a new list of lists)
ref_matrix = msr.to_ref(matrix, show_steps=True)
print(ref_matrix)

# Or launch interactive terminal prompts:
# msr.to_ref()
```

### 2. Convert Matrix to Reduced Row Echelon Form (`to_rref`)
Transforms any matrix into Reduced Row Echelon Form (RREF) using Gauss-Jordan elimination.

```python
matrix = [
    [1.0, 2.0],
    [3.0, 4.0]
]

rref_matrix = msr.to_rref(matrix, show_steps=True)
print(rref_matrix)

# Interactive mode:
# msr.to_rref()
```

### 3. Solve a System of Linear Equations (`solve_system`)
Solves an augmented matrix $[A | B]$ representing a linear system.

```python
# System:
#  1x + 2y = 5
#  3x + 4y = 11
augmented_matrix = [
    [1.0, 2.0, 5.0],
    [3.0, 4.0, 11.0]
]

# Solve and optionally show a 2D plot for 2-variable systems
solution = msr.solve_system(augmented_matrix, plot=True)
print(solution)  # {'X1': 1.0, 'X2': 2.0}

# Interactive mode (prompts for equations and constants):
# msr.solve_system()
```

### 4. Check Consistency of a System (`is_consistent`)
Quickly check whether a system of linear equations has at least one solution or is inconsistent.

```python
augmented_matrix = [
    [1.0, 2.0, 5.0],
    [2.0, 4.0, 12.0]  # Inconsistent: 0 = 2
]

consistent = msr.is_consistent(augmented_matrix)
print("Consistent?", consistent)  # False
```

### 5. Plot 2D Linear Systems (`plot_system`)
Visually displays 2 linear equations on a 2D Cartesian plane with their intersection point using `matplotlib`.

```python
matrix_2d = [
    [1.0, 2.0, 5.0],   # x + 2y = 5
    [3.0, 4.0, 11.0]   # 3x + 4y = 11
]

msr.plot_system(matrix_2d)

# Or prompt for the 2 equations interactively:
# msr.plot_system()
```

---

## Interactive Mode

If you call any function without arguments, `matrix-solver-ref` will automatically guide you with clear questions in your terminal:

* **Matrix functions (`to_ref`, `to_rref`):** asks for total rows, columns, and each element.
* **System functions (`solve_system`, `is_consistent`):** asks for number of equations, variables, coefficients, and constants.
* **Plot function (`plot_system`):** asks for $X$ coefficient, $Y$ coefficient, and constant for each of the two lines.

## License
MIT License.
