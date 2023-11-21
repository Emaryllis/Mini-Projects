# Skyscraper Puzzle Solver

---

## Overview

The Skyscraper Puzzle Solver is encapsulated within the `SkyscraperSolver` class, providing an efficient solution to Skyscraper puzzles. This tool interprets puzzle constraints and produces logical solutions based on specified visibility rules. Below is a guide on how to use and integrate this solver into your projects.

## How to Use

1. **Instantiate the Solver:**

    - Create an instance of the `SkyscraperSolver` class.

2. **Set Puzzle Constraints:**

    - Provide the Skyscraper puzzle constraints using the specified format.

3. **Run Solver:**

    - Execute the `solver` method to obtain solutions based on the provided constraints.

4. **View Output:**
    - Review the solved puzzle grid, revealing the correct placement of skyscrapers.

## Example

Here's an example of using the Skyscraper Puzzle Solver:

```python
from skyscraper_solver import SkyscraperSolver

# Create an instance of the solver
solver_instance = SkyscraperSolver()

# Set puzzle constraints
board = np.array([[0, 2, 2, 3, 1, 0],
                  [3, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 3],
                  [2, 0, 0, 0, 0, 2],
                  [2, 0, 0, 0, 0, 2],
                  [0, 3, 2, 1, 2, 0]])

# Run the solver
solver_instance.solver(board)
```

## Contribution

Contributions to the Skyscraper Puzzle Solver project are welcome! Feel free to report issues, suggest enhancements, or submit pull requests to improve the solver's functionality and usability.
