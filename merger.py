from PyPDF2 import PdfMerger, PdfReader

arquivos = ["IMG_0192.pdf", "IMG_0193.pdf",
            "IMG_0194.pdf", "IMG_0195.pdf", "IMG_0196.pdf", "IMG_0197.pdf",]

merger = PdfMerger()
for i in range(len(arquivos)):
    merger.append(PdfReader(open(arquivos[i], 'rb')))

merger.write("merged_file.pdf")
