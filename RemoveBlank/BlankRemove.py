with open(
    "Blank/01MNoFinal.txt", 'r') as r, open(
        'Blank/output.txt', 'w') as o:

    for line in r:
        if line.strip():
            o.write(line)

f = open("output.txt", "r")


clean = open('Blank/CSV02MPass.txt').read().replace('\n', '')


f = open('Blank/CSV02MPass.txt', 'w')
f.write(clean)
f.close()

print("New text file:\n", f.read())
