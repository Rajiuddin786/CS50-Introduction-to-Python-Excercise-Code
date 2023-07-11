import csv
import sys

if len(sys.argv) != 3:
    sys.exit("Invalid Input")

try:
    student = []
    with open(sys.argv[1]) as file:
        read = csv.reader(file)
        header = next(read)
        for row in read:
            student.append({"frist":row[0].replace('"'),"last":row[1].replace('"'),"house":row[2]})
except FileNotFoundError:
    sys.exit(f"Could not find {sys.argv[1]}")
except IOError:
    sys.exit("Error: An I/O error occurred while reading or writing the files.")

with open(sys.argv[2],"a",newline='') as file:
    write = csv.DictWriter(file,fieldnames=["frist","last","house"])
    write.writeheader()
    write.writerows(student)
sys.exit(0)