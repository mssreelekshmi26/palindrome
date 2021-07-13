import aqgFunction
import os
import math
from enum import Enum
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
# From PDFInterpreter import both PDFResourceManager and PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
# Import this to raise exception whenever text extraction from PDF is not allowed
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from pdfminer.converter import PDFPageAggregator
from datetime import datetime
def read_pdf():
    my_file = "short-stories-for-children.pdf"
    log_file ="short.txt"
    print("start")
    password = ""
    extracted_text = ""
    fp = open(my_file, "rb")
    parser = PDFParser(fp)
    document = PDFDocument(parser, password)
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    for page in PDFPage.create_pages(document):
        page_txt = ""
        page_lines = {}
        line_count = 0

        interpreter.process_page(page)
        layout = device.get_result()
        for obj in layout._objs:
            if isinstance(obj, LTTextBox):
                for o in obj._objs:
                    if isinstance(o, LTTextLine):
                        page_txt += o.get_text()
                        text = o.get_text()
                        extracted_text += page_txt.strip()
    with open(log_file, "w") as f:
        f.write(extracted_text)
    print("file created")
# Create AQG object
read_pdf()
aqg = aqgFunction.AutomaticQuestionGenerator()
inputTextPath = "DB/short-stories-for-children .txt"
readFile = open(inputTextPath, 'r+', encoding="utf8")
# readFile = open(inputTextPath, 'r+', encoding="utf8", errors = 'ignore')

inputText = readFile.read()
# inputText = '''I am Dipta. I love codding. I build my carrier with this.'''
#print(inputText)
questionList = aqg.aqgParse(inputText)
aqg.display(questionList)

# aqg.DisNormal(questionList)
