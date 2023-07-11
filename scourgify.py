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
            row[0].strip('"')
            print(row[0])
            student.append({"frist":row[0],"last":row[0],"house":row[1]})

except FileNotFoundError:
    sys.exit(f"Could not find {sys.argv[1]}")

"""with open(sys.argv[2],"a",newline='') as file:
    write = csv.DictWriter(file,fieldnames=["frist","last","house"])
    write.writeheader()
    write.writerows(student)
exit(code=0)"""