from tabulate import tabulate
import csv
import sys

if len(sys.argv) <= 1:
    sys.exit("Too Few Argument")
else:
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
def main():
    lis=list()
    file_name = "sicilian.csv" if sys.argv[1] == "sicilian.csv" else "regular.csv"
    with open(file_name) as file:
        read=csv.DictReader(file)
        for line in read:
             lis.append(line)
    table=tabulate(lis,headers="keys",tablefmt="grid")
    print(table)

if __name__ == "__main__":
    main()
