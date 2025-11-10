from tabulate import tabulate
import csv
import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    table = []
    with open(sys.argv[1]) as f:
        reader = csv.DictReader(f)
        for row in reader:
            table.append(row)
    
    print(tabulate(table, headers="keys", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
