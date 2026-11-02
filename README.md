# Linear System Solver (`matrix-solver-ref`)

This tool provides a straightforward, beginner-friendly way to solve systems of linear equations and perform matrix operations using **Gaussian Elimination** and **Gauss-Jordan Elimination** to transform matrices into **Row Echelon Form (REF)** and **Reduced Row Echelon Form (RREF)**.

Available as both a standalone script and a pip-installable module with beginner-tailored functions.

---

## Installation

Install directly from PyPI:
```bash
pip install matrix-solver-ref
```

---

## Functions Reference

Import as either `matrix_solver_ref` or `ref`:

```python
import matrix_solver_ref as msr  # or: import ref as msr
```

### 1. `to_ref(matrix=None, show_steps=False)`
Converts any matrix into Row Echelon Form (REF).
* If `matrix` is omitted, prompts interactively for rows, columns, and elements.
* Returns a new matrix without mutating original input.

```python
mat = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
ref_mat = msr.to_ref(mat, show_steps=True)
```

### 2. `to_rref(matrix=None, show_steps=False)`
Converts any matrix into Reduced Row Echelon Form (RREF).
* Scales pivots to 1 and eliminates entries both above and below pivots.

```python
mat = [[1, 2], [3, 4]]
rref_mat = msr.to_rref(mat)
```

### 3. `solve_system(matrix=None, plot=False, show_steps=True)`
Solves a linear system represented as an augmented matrix $[A | B]$.
* In interactive mode (`solve_system()`), prompts for equations, variables, and constants.
* Returns a dictionary of variable values (e.g., `{"X1": 1.0, "X2": 2.0}`), `"infinitely many solutions"`, or `None` if inconsistent.
* Supports visual 2D line plotting for $2 \times 3$ systems when `plot=True`.

```python
system = [
    [1.0, 2.0, 5.0],   # x + 2y = 5
    [3.0, 4.0, 11.0]   # 3x + 4y = 11
]
solution = msr.solve_system(system, plot=True)
print(solution)  # {'X1': 1.0, 'X2': 2.0}
```

### 4. `is_consistent(matrix=None, verbose=True)`
Checks whether a linear system has solutions or is inconsistent ($0 = c$).
* Returns `True` or `False`.

```python
inconsistent_system = [
    [1.0, 2.0, 5.0],
    [2.0, 4.0, 12.0]
]
print(msr.is_consistent(inconsistent_system))  # False
```

### 5. `plot_system(matrix=None)`
Plots the 2 linear equations on a 2D Cartesian plane using `matplotlib` and marks the exact intersection solution.

```python
msr.plot_system([[1, 2, 5], [3, 4, 11]])
```

---

## Standalone Script Usage

You can also run the solver directly in your terminal:
```bash
python ref.py
```
Follow the interactive prompts to input equations and coefficients.

---

## Key Features
* **Automated Row Operations:** Handles row swapping, elimination, and scaling automatically.
* **Dual Interface:** Works programmatically in Python scripts and interactively in the terminal.
* **2D Visualizations:** Built-in `matplotlib` integration for 2-variable systems.
* **Numerical Precision:** Uses a small tolerance (`1e-9`) to prevent floating-point inaccuracies.

---

## Prerequisites
* Python >= 3.7
* `numpy`
* `matplotlib`

---

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Contributing
Feel free to open issues or contribute via pull requests!