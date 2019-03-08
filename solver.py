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

varFile = args[1]           # name of var file
constraintFile = args[2]    # name of constraint file
checkingMethod = True if args[3] == 'fc' else False    # name of checking method

def equals(tup):
    return tup[0] == tup[1]

def greaterThan(tup):
    return tup[0] > tup[1]

def lessThan(tup):
    return tup[0] < tup[1]

def notEquals(tup):
    return tup[0] != tup[1]

problem = Problem(forward_checking=checkingMethod)
problem.addVariable('a', [1, 2, 3])
problem.addVariable('b', [3, 4])
problem.addVariable('c', [4, 5, 6])
problem.addVariable('d', [4, 3, 8])
problem.addVariable('e', [4, 3, 8])

problem.addConstraint(equals, ['a', 'b'])
problem.addConstraint(greaterThan, ['c', 'b'])
problem.addConstraint(lessThan, ['c', 'd'])
problem.addConstraint(equals, ['e', 'd'])
solved = problem.solve()  # true or false
if not solved:
    print "FAILURE"
