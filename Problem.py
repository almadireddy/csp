class Problem:
    def __init__(self, forward_checking):
        self.variables = {}
        self.constraints = []
        self.forward_checking = forward_checking

    # add a variable to solve for
    def addVariable(self, variable, domain):
        self.variables[variable] = (domain, domain)       # variable:domain is key:(domain, remaining Domain)


    # add a constraint function for variables
    # constraint looks like (constraintFunction, variables to constrain)
    def addConstraint(self, constraint_function, variables):
        self.constraints.append((constraint_function, variables))


    # call to start the solver
    # return true or false
    def solve(self):
        assignments = {}
        if self.solve_recursive(assignments):
            return assignments
        else:
            return False

    # the recursive part of the solver
    # performs backtracking search
    def solve_recursive(self, assignments):
        # base case
        if len(assignments) == len(self.variables):
            if self.goalTest(assignments):
                return assignments
            else:
                return False

        var = self.select_unassigned_variable(assignments)
        for value in self.order_domain_values(var):
            if self.check_consistency(var, value):
                assignments[var] = value
                result = self.solve_recursive(assignments)

                if result is not False:
                    return result

                assignments.pop(var)

        return False

    def select_unassigned_variable(self, assignments):
        unassigned = []
        for a in self.variables:
            if a not in assignments:
                unassigned.append(a)

        return unassigned[0]    # return the first unassigned variable for now


    def order_domain_values(self, var):
        # self.variables[var] is (domain, remainingDomain)
        # we return the remaining domain
        # (for now just as-is without ordering)
        return self.variables[var][1]

    def check_consistency(self, var, value):
        # this will check whether the assigned value is consistent
        return True


    def goalTest(self, assignments):
        for key in self.variables:
            if key not in assignments:
                return False    # return false if not all variables have been assigned

        for constraint in self.constraints:
            v1 = assignments[constraint[1][0]]  # getting assigned value by name of variable
            v2 = assignments[constraint[1][1]]
            if not constraint(v1, v2):
                return False                    # if constraint doesnt hold return false

        return True