from pypdf import PdfWriter
import glob


globnames = glob.glob("./*.pdf")

finalnames = []
for filename in globnames:
    filename = filename.replace("\\", "")
    filename = filename.replace(".", "")
    finalnames.append(filename[:4])

print(finalnames)

merger = PdfWriter()
prev = -1

for filename, file in zip(finalnames, globnames):
    if prev == filename or prev == -1:
        merger.append(file)
        prev = filename

    else:
        merger.write(f"out/{prev}.pdf")
        merger.close()
        merger = PdfWriter()
        merger.append(file)
        prev = filename

merger.write(f"out/{prev}.pdf")
merger.close()
