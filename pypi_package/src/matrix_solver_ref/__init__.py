try:
    from ref.core import (
        # Beginner-Friendly API
        to_ref,
        to_rref,
        solve_system,
        is_consistent,
        plot_system,
        # Core & Legacy API
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
except (ModuleNotFoundError, ImportError):
    import ref
    to_ref = ref.to_ref
    to_rref = ref.to_rref
    solve_system = ref.solve_system
    is_consistent = ref.is_consistent
    plot_system = ref.plot_system
    system = ref.system
    main = ref.main
    REF = ref.REF
    REF_1 = ref.REF_1
    RREF = ref.RREF
    display = ref.display
    check_consistent = ref.check_consistent
    matrix_input = ref.matrix_input
    line_plot = ref.line_plot

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
