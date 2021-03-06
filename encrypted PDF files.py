import shutil, os, PyPDF2, time

os.chdir(r"Working Directory")

source_dir = r"Source PDF"

dest_dir = r"Destination PDF"

for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file.endswith(".pdf"):
            shutil.copy(os.path.join(root, file), dest_dir)


for i in os.listdir(dest_dir):
    joinedfiles = open(os.path.join(dest_dir, i), "rb")
    pdfreader = PyPDF2.PdfFileReader(joinedfiles)
    pdfwriter = PyPDF2.PdfFileWriter()
    for j in range(pdfreader.numPages):
        pdfwriter.addPage(pdfreader.getPage(j))
    pdfwriter.encrypt("hello9")
    results = open(os.path.join(dest_dir, "encrypted"+i), "wb")
    pdfwriter.write(results)
    results.close()
    joinedfiles.close()

time.sleep(2)

for i in os.listdir(dest_dir):
    if not i.startswith("encrypted"):
        os.remove(os.path.join(dest_dir, i))
