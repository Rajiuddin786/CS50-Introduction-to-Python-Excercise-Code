from csv import reader,DictReader,writer,DictWriter
import sys

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
    try:
        with open(output_file,"w",newline="") as file:
            header = ["frist","last","house"]
            write = DictWriter(file,fieldnames=header)
            with open(input_file) as fil:
                read = DictReader(fil)
                write.writeheader()
                for row in read:
                    frist,last = row["name"].split(",")
                    write.writerow({"frist":frist.strip(),"last":last.strip(),"house":row["house"].strip()})
    except FileNotFoundError:
        sys.exit(f"Could not file{input_file}")

if __name__ == "__main__":
    main()