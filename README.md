# Constraint Satisfaction Solver

### Created for CS 4365 Artificial Intelligence.

Uses the most constrained variable heuristic when choosing a variable to assign and uses the most constraining variable heuristic to break ties within those.

Uses the least constraining value heuristic to choose the value to assign for the chosen variable, breaking ties by choosing the smallest value.

Optionally uses forward checking to eliminate search paths faster.

## Solver Usage
solver.py is the assignment for class, and usage is simple. Via command line, first argument is the variable file, second is the constraint file, and third is option for using forward checking or not. See below for format of the variable (.var) file and the constraint (.con) file.

`python solver.py <.var file> <.con file> none|fc`

## CSP Usage
**Constructor:** `csp = CSP(fc)` where fc is a boolean indicating whether to use forward checking or not

**Add your variables:** `csp.addVariable(varName, domain)` where varname is a single character `"a"` and domain is a list of values `[1, 2, 3]`

**Add the constraints:** `csp.addConstraint(constraint_function, variables)` where constraint function is a lambda that takes two variables as input and returns whether they are satisfactory or not. Variables is a two-list that has the variables in the order to they need to be passed into the function for evaluating the constraint. `csp.addConstraint(lambda x, y: x > y, ['A', 'B'])` would indicate the constraint `A > B`

**Find the solution:** `csp.solve()` returns True or False, indicating whether a solution has been found or not. For the purposes of this homework, it will also print to stdout as it solves, with the last line indicating valid assignment or failure. Ideally, it would return the valid assignment, but that's not how this is graded so it doesn't. See below for example output.

## Variable File
Each variable (single character) on its own line, followed by allowed domain

Example:

```text
A: 1 2 3 4 5
B: 1 2 3 4
C: 1 2 3 4 5 6 7 8
D: 5 7 9 11
E: 3 4 5 6
F: 1 5 10
G: 5 6 7 8 9
```


## Constraint file
Each constraint on its own line, with either `<` `>` `=` `!` as possible operators
```text
A = G
A > B
C > B
D > E
G > C
```

## Example Output from solver
Running `python solver.py examples/ex3.var examples/ex3.con none`:

```text
1. F=1, B=1, D=7, E=3, G=9, A=1  failure
2. F=1, B=1, D=7, E=3, G=9, A=2  failure
3. F=1, B=1, D=7, E=3, G=9, A=3  failure
4. F=1, B=1, D=7, E=3, G=9, A=4  failure
5. F=1, B=1, D=7, E=3, G=9, A=5  failure
6. F=1, B=1, D=7, E=3, G=8, A=1  failure
7. F=1, B=1, D=7, E=3, G=8, A=2  failure
8. F=1, B=1, D=7, E=3, G=8, A=3  failure
9. F=1, B=1, D=7, E=3, G=8, A=4  failure
10. F=1, B=1, D=7, E=3, G=8, A=5  failure
11. F=1, B=1, D=7, E=3, G=7, A=1  failure
12. F=1, B=1, D=7, E=3, G=7, A=2  failure
13. F=1, B=1, D=7, E=3, G=7, A=3  failure
14. F=1, B=1, D=7, E=3, G=7, A=4  failure
15. F=1, B=1, D=7, E=3, G=7, A=5  failure
16. F=1, B=1, D=7, E=3, G=5, A=1  failure
17. F=1, B=1, D=7, E=3, G=5, A=2  failure
18. F=1, B=1, D=7, E=3, G=5, A=3  failure
19. F=1, B=1, D=7, E=3, G=5, A=4  failure
20. F=1, B=1, D=7, E=3, G=5, A=5, C=1  failure
21. F=1, B=1, D=7, E=3, G=5, A=5, C=2  solution
```

Running `python solver.py examples/ex3.var examples/ex3.con none`:

```text
1. F=1, B=1, A=5, G=5, C=2, D=7, E=3  solution
```