import sys
import csv

if len(sys.argv) != 3:
    sys.exit("Error: Please provide exactly two command-line arguments.")

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        if len(rows) == 0 or len(rows[0]) != 2:
            sys.exit("Error: Invalid input CSV format. Expected columns: name, house.")

        with open(output_file, 'w', newline='') as output:
            writer = csv.writer(output)
            writer.writerow(["first", "last", "house"])

            for row in rows:
                name = row[0].split()
                if len(name) != 2:
                    sys.exit(f"Error: Invalid name format in input CSV. Expected 'first last', got '{row[0]}'.")

                first_name, last_name = name
                house = row[1]
                writer.writerow([first_name, last_name, house])

    print(f"Conversion completed. Data written to '{output_file}'.")
    sys.exit(0)

except FileNotFoundError:
    sys.exit(f"Error: File '{input_file}' not found.")
except IOError:
    sys.exit("Error: An I/O error occurred while reading or writing the files.")