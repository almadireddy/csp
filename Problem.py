class Problem:
    def __init__(self, forward_checking):
        self.variables = {}
        self.constraints = []
        self.forward_checking = forward_checking
        self.call_depth = 0


    # add a variable to solve for
    def addVariable(self, variable, domain):
        if variable not in self.variables:
            self.variables[variable] = (domain, domain)       # variable is variableName:(domain, remaining Domain)
        else:
            print "u dumb, that's a duplicate variable im skipping."


    # add a constraint function for variables
    # constraint looks like (constraintFunction, variables to constrain)
    def addConstraint(self, constraint_function, variables):
        self.constraints.append((constraint_function, variables))


    # call to start the solver
    # return dictionary of assignments or false
    def solve(self):
        assignments = {}
        if self.solve_recursive(assignments):
            return assignments
        else:
            return False


    # the recursive part of the solver
    # performs backtracking search
    # this maps almost exactly to pseudocode in slides
    def solve_recursive(self, assignments):
        # base case
        if len(assignments) == len(self.variables):
            if self.goalTest(assignments):
                # if self.call_depth < 30:
                self.print_assignments(assignments, 'solution')
                return assignments
            else:
                return False

        var = self.select_unassigned_variable(assignments)  # complete this function
        for value in self.order_domain_values(var):         # complete this function
            if self.check_consistency(var, value, assignments):
                assignments[var] = value
                result = self.solve_recursive(assignments)

                if result is not False:
                    remaining_domains = self.variables[var][1]
                    constraints = self.get_constraints(var)

                    return result

                # if self.call_depth < 30:
                self.print_assignments(assignments, 'failure')
                self.call_depth += 1

                assignments.pop(var)

        return False


    def select_unassigned_variable(self, assignments):
        unassigned = self.get_unassigned(assignments)
        valid_constraints = []

        to_pick_from = []

        for u in unassigned:
            constraints = self.get_constraints(u)

            for c in constraints:
                if c[1][0] in assignments or c[1][1] in assignments:
                    valid_constraints.append(c)

            new_remaining_domain = []
            remaining_domain = self.variables[u][1]

            for val in remaining_domain:
                if self.check_consistency(u, val, assignments):
                    new_remaining_domain.append(val)

            to_pick_from.append([u, new_remaining_domain, 0])

        to_pick_from.sort(key=lambda t: len(t[1]))

        # the most constraining out of these
        to_tie_break = []
        min_val = len(to_pick_from[0][1])

        for a in to_pick_from:
            if len(a[1]) is min_val:
                to_tie_break.append(a)

        for var in to_tie_break:
            unassigned_constraints = []
            constraints = self.get_constraints(var[0])

            for c in constraints:
                if c[1][0] not in assignments and c[1][1] not in assignments:
                    unassigned_constraints.append(c)

            var[2] = len(unassigned_constraints)

        to_tie_break.sort(key=lambda t: int(t[2]), reverse=True)

        return to_tie_break[0][0]



    def order_domain_values(self, var):
        # self.variables[var] is (domain, remainingDomain)
        # we return the remaining domain
        # (for now just as-is without ordering)
        constraints = self.get_constraints(var)
        domains = self.variables[var][1]

        to_pick_from = []

        return self.variables[var][1]


    def check_consistency(self, var, value, assignments):
        # this will check whether the assigned value is consistent
        constraints = self.get_constraints(var)

        for con in constraints:             # for each constraint involving this variable
            index_of_var = con[1].index(var)
            index_of_other_var = 0 if index_of_var is 1 else 1
            other_var = con[1][index_of_other_var]

            if con[1][1] in assignments:
                to_pass = [0, 0]
                to_pass[index_of_var] = value
                to_pass[index_of_other_var] = assignments[other_var]
                if not con[0](to_pass):   # check if value is consistent
                    return False

            else:
                return True

        return True


    def goalTest(self, assignments):
        for key in self.variables:
            if key not in assignments:
                return False    # return false if not all variables have been assigned

        for constraint in self.constraints:
            v1 = assignments[constraint[1][0]]  # getting assigned value by name of variable
            v2 = assignments[constraint[1][1]]

            if not constraint[0]([v1, v2]):
                return False                    # if constraint doesnt hold return false

        return True


    def get_constraints(self, var):
        constraints = []  # the constraints involving this variable

        for a in self.constraints:
            if var in a[1]:  # if the variable is in the listed arguments for the constraint
                constraints.append(a)

        return constraints


    def get_unassigned(self, assignments):
        unassigned = []
        for a in self.variables:
            if a not in assignments:
                unassigned.append(a)

        return unassigned


    def print_assignments(self, assignments, status):
        # this function prints in the proper way
        print str(self.call_depth + 1) + '.',

        for a in assignments:
            print str(a) + '=' + str(assignments[a]) + ',',

        print status
