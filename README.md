# Linear System Solver

This tool provides a straightforward way to solve systems of linear equations using **Gaussian Elimination** and **Gauss-Jordan Elimination** to transform a matrix into **Reduced Row Echelon Form (RREF)**.

## How It Works
The program processes your input using the following logical steps:

1.  **Input:** You define the number of equations and variables, then enter the coefficients and constants for your system.
2.  **Row Echelon Form (REF):** The program converts the matrix into REF by identifying pivots and eliminating entries below them.
3.  **Normalization:** Each pivot is normalized to 1.
4.  **Reduced Row Echelon Form (RREF):** The program performs back-substitution to eliminate entries above the pivots, resulting in the final RREF matrix.
5.  **Consistency Check:** It analyzes the final matrix to determine if the system is:
    * **Consistent:** If the system has a solution (unique or infinite).
    * **Inconsistent:** If the system has no solution (e.g., a row like `[0 0 ... 5]`).

## Key Features
* **Automated Calculation:** Handles row operations (swapping, elimination, and scaling) automatically.
* **Unique Solution Detection:** If the system is 2x3 (two variables), it automatically provides the specific values for the variables.
* **Visual Representation:** If a 2x3 system is provided, the script uses `matplotlib` to plot the two lines, showing their intersection point visually.
* **Numerical Precision:** Uses a small tolerance (`1e-9`) to handle floating-point inaccuracies, ensuring reliable results.

## Prerequisites
To run this script, ensure you have the following installed:
* `python`
* `numpy`
* `matplotlib`

## Usage
1. Run the script in your terminal/IDE.
2. Follow the prompts to enter the number of equations and variables.
3. Input the coefficients row by row as requested.
4. View the original matrix, the final RREF, and the calculated solution.
