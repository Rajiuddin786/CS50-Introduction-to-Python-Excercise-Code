import sys
import csv

if len(sys.argv) > 3:
    sys.exit("Too Many Argument")
elif len(sys.argv) < 3:
    sys.exit("Too Few Argument")
else:
    _,b = sys.argv[1].split('.')
    _,y = sys.argv[2].split('.')
    if b != "csv" and y!= "csv":
        sys.exit("Not a CSV file")

def main():
    
