import sys
from Problem import Problem
args = sys.argv[:]

if not len(args) == 4:
    print("Expected 3 arguments: .var file, .con file, fc/none")
    exit(0)
else:
    if not str(args[1]).endswith('.var'):
        print("Expected .var file that contains the variables")
        exit(0)
    if not str(args[2]).endswith('.con'):
        print("Expected .con file that contains the constraints")
        exit(0)
    if not (args[3] == 'none' or args[3] == 'fc'):
        print("Expected either none (backtracking) or fc (forward-checking) for consistency enforcing")
        exit(0)

# all checks have worked and args contains correct input

# set up names to open and make problem object
varFileName = args[1]           # name of var file
constraintFileName = args[2]    # name of constraint file
checkingMethod = True if args[3] == 'fc' else False    # name of checking method

problem = Problem(forward_checking=checkingMethod)

# open and add variable from var file to the problem
varFile = open(varFileName, 'r')
for line in varFile:
    var = line[0]
    domain = line[3:].strip('\n').split(' ')
    if '' in domain:
        domain.remove('')
    problem.addVariable(var, domain)

varFile.close()

# define the functions for each of the possible constraints to check whether constraint is held
# they all take an array of values to apply to the two variables in the constraint
# look at check_consistency() in Problem.py
def equals(arr):
    return arr[0] == arr[1]

def greaterThan(arr):
    return arr[0] > arr[1]

def lessThan(arr):
    return arr[0] < arr[1]

def notEquals(arr):
    return arr[0] != arr[1]

# dictionary for switch based on input
funcSelector = {
    "=": equals,
    ">": greaterThan,
    "<": lessThan,
    "!": notEquals
}

# open and read in from constraint file, and add to Problem
conFile = open(constraintFileName, 'r')
for line in conFile:
    lin = line.strip('\n').split(" ")
    # lin now looks like ['X', '>', 'Y']

    arg = [lin[0], lin[2]]  # the arguments to pass into the addConstraint
    operator = lin[1]     # the constraint function that will be called
    problem.addConstraint(funcSelector.get(str(operator)), arg)
conFile.close()

# solve it, solved will contain the assignments or false
solved = problem.solve()  # true or false
