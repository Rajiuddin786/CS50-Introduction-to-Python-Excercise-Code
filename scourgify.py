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

input_file = sys.argv[1]
output_file = sys.argv[2]
def main():
    with open(output_file,"w",newline="") as file:
        header = ["frist","last","house"]
        write = csv.writer(file,fieldnames=header)
        with open(input_file) as fil:
            read = csv.reader(file)
            head = next(read)
            for row in read:
                frist,last,house = row.split(",")
                
