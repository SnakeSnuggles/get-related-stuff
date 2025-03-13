from pypdf import PdfReader

# creating a pdf reader object
reader = PdfReader('internment.pdf')

# printing number of pages in pdf file
print(len(reader.pages))


for page in reader.pages:
    print(page.extract_text())
