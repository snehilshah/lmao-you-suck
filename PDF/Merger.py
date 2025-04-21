from pypdf import PdfWriter
import glob
import os


globnames = glob.glob(".\\2025\\Batch1\\*.pdf")

finalnames = []
for filepath in globnames:
    filename = os.path.basename(filepath)  # Gets "1001 - 2_2.pdf"
    filename = os.path.splitext(filename)[0]  # Removes .pdf extension
    finalnames.append(filename)


print(finalnames)

merger = PdfWriter()
prev = -1

for filename, file in zip(finalnames, globnames):
    filename = str(filename)
    filename = filename.strip()
    filename = filename.split(" - ")[0].strip()
    print("FileName: ", filename)
    print("File: ", file)
    if prev == filename or prev == -1:
        merger.append(file)
        prev = filename

    else:
        merger.write(f"./2025/Batch1/out/{prev}.pdf")
        merger.close()
        merger = PdfWriter()
        merger.append(file)
        prev = filename

merger.write(f"./2025/Batch1/out/{prev}.pdf")
merger.close()
