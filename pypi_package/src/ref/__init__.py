from .core import (
    # Public beginner-friendly API
    to_ref,
    to_rref,
    solve_system,
    is_consistent,
    plot_system,
    # Core & legacy utilities
    system,
    main,
    REF,
    REF_1,
    RREF,
    display,
    check_consistent,
    matrix_input,
    line_plot,
)

__all__ = [
    # Beginner-Friendly API
    "to_ref",
    "to_rref",
    "solve_system",
    "is_consistent",
    "plot_system",
    # Core & Legacy API
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
