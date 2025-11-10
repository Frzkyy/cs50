import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not (sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv")):
    sys.exit("Not a CSV file")

try:
    table = []
    with open(sys.argv[1]) as f:
        reader = csv.DictReader(f)
        for row in reader:
            table.append(row)
    
    for student in table:
        last, first = student["name"].split(", ")
        student["last"] = last
        student["first"] = first
        student.pop("name")
    
    with open(sys.argv[2], 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["first","last","house"])
        writer.writeheader()
        for people in table:
            writer.writerow({"first":people["first"], "last":people["last"], "house":people["house"]})


except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

