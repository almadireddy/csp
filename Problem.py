class Problem:
    def __init__(self, forwardChecking):
        self.variables = {}
        self.constraints = []
        self.forwardChecking = forwardChecking


    def addVariable(self, variable, domain):
        self.variables[variable] = (domain, domain)       # variable:domain is key:(domain, remaining Domain)


    # constraint looks like (constraintFunction, variables to constrain)
    def addConstraint(self, constraint_function, variables):
        self.constraints.append((constraint_function, variables))

    # the main entry point
    def solve(self):
        assignments = {}
        return self.solveRecursive(assignments)


    def solveRecursive(self, assignments):
        if self.goalTest(assignments):
            return assignments
        var = self.selectUnassignedVariable()


    def selectUnassignedVariable(self):
        return self.variables[0]


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


    def orderDomain(self, var):
        return self.variables[var]
