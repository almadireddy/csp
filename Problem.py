class Problem:
    def __init__(self, forwardChecking):
        self.variables = {}
        self.constraints = []
        self.forwardChecking = forwardChecking

    def addVariable(self, variable, domain):
        self.variables[variable] = domain       # variable:domain is key:value

    # constraint looks like (constraintFunction, variables to constrain)
    def addConstraint(self, constraintFunction, variables):
        self.constraints.append((constraintFunction, variables))

    def solve(self):
        assignments = {}
        self.solveRecursive(assignments)

    def solveRecursive(self, assignments):
        if self.goalTest(assignments):
            return assignments
        var = self.selectVariable()

    def selectVariable(self):
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
