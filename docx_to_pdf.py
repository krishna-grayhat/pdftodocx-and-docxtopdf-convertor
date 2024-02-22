from pdf2docx import Converter
from docx2pdf import convert
from tkinter.filedialog import *

user = int(input("""
                press 1 \'For convert pdf to docx file\' 
                press 2 \'For convert docx to pdf file\' 
                ... """))

if user == 1:
    old_file = askopenfilename()
    new_doc = input("give name to save file \'without .docx\' = ")
    new_doc1 = new_doc+".docx"

    obj = Converter(old_file)
    obj.convert(new_doc1)
    obj.close()

elif user == 2:
    old_file = askopenfilename()
    new_pdf = input("give name to save file \'without .pdf\' = ")
    new_pdf1 = new_pdf+".pdf"
    convert(old_file,new_pdf1)

else:
    print("invlaid")