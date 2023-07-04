import sys

count = 0
if len(sys.argv) > 2:
    sys.exit('Too Many Argument')
elif len(sys.argv) < 2:
    sys.exit('Too Few Argument')
else:
    a = sys.argv[1].strip().endswith('.py')
    if a == False:
        sys.exit('Not a Python file')
    else:
        with open(sys.argv[1],'r') as file:
            for lines in file:
                if not lines.strip().startswith('#') and lines.strip():
                    count+=1
print(count)