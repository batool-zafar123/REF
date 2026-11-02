"""REF Matrix Solver - Entry script.

This script delegates to the package implementation in `pypi_package/src/ref/core.py`
to prevent duplicate code and ensure a single source of truth.
"""

import os
import sys

_ref_dir = os.path.join(os.path.dirname(__file__), "pypi_package", "src", "ref")
if _ref_dir not in sys.path:
    sys.path.insert(0, _ref_dir)

import core  # noqa: E402

# Beginner-Friendly API
to_ref = core.to_ref
to_rref = core.to_rref
solve_system = core.solve_system
is_consistent = core.is_consistent
plot_system = core.plot_system

# Core & Legacy API
system = core.system
main = core.main
REF = core.REF
REF_1 = core.REF_1
RREF = core.RREF
display = core.display
check_consistent = core.check_consistent
matrix_input = core.matrix_input
line_plot = core.line_plot

__all__ = [
    "to_ref",
    "to_rref",
    "solve_system",
    "is_consistent",
    "plot_system",
    "system",
    "main",
    "REF",
    "REF_1",
    "RREF",
    "display",
    "check_consistent",
    "matrix_input",
    "line_plot",
]

if __name__ == "__main__":
    main()