import sys

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
