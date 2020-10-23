# This is a sample Python script.
import pyttsx3

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from tkinter.filedialog import *
from io import StringIO

ttsEngine = pyttsx3.init()
output_string = StringIO()
filepath = askopenfilename()
with open(filepath, 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)
print(output_string.getvalue())
if __name__ == '__main__':
    ttsEngine.say(output_string.getvalue())
    ttsEngine.runAndWait()

