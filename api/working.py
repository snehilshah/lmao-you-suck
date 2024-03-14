import csv

results = []
with open("api/new_agri.txt") as csvfile:
    # reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in csvfile: # each row is a list
        results.append(row.strip())

print(results)