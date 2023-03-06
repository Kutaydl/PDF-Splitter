from PyPDF2 import PdfFileReader, PdfFileWriter

filePath = input("Dosya konumuzu girin: ")
first_page = int(input("baslangic sayfasini girin: "))
last_page = int(input("bitis sayfasini girin: "))

split = list(range(first_page,(last_page+1)))

with open(filePath, "rb") as f:
    reader = PdfFileReader(f)
    s_part = PdfFileWriter()

    for page in range(len(reader.pages)):
        if page in split:
            s_part.addPage(reader.getPage(page))
        

    with open("splitPart.pdf", "wb") as f2:
        s_part.write(f2)

