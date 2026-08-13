# Matrix Solver

A simple Python library that converts matrices into Row Echelon Form (REF) and Reduced Row Echelon Form (RREF). 
It also provides functionalities to check consistency, solve linear systems, and visualize 2D systems.

## Installation

```bash
pip install matrix-solver-ref
```

## Usage

You can import the library and pass a matrix directly to the `system` function to see the results printed in your terminal:

```python
import ref

# Define your matrix (e.g. 2 equations, 3 variables/constants)
# Each row represents an equation, and the last element is the constant.
my_matrix = [
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0]
]

# Run the solver on your matrix
ref.system(my_matrix)
```

Alternatively, you can run the interactive prompt:

```python
import ref

# Run the interactive solver
ref.main()
```
