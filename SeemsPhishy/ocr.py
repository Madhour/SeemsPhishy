from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO
from pdfminer.pdfpage import PDFPage

def data_retpro(pdf_path, name_txt_file):
    
    #Teil 1 (Extrahieren des Textes aus der Datei)
    resource_manager = PDFResourceManager(caching=True)
    out_text = StringIO()
    codec = 'utf-8'
    laParams = LAParams()
    text_converter = TextConverter(resource_manager, out_text, laparams=laParams)
    fp = open(pdf_path, 'rb')
    interpreter = PDFPageInterpreter(resource_manager, text_converter)

    for page in PDFPage.get_pages(fp, pagenos=set(), maxpages=0, password="", caching=True, check_extractable=True):
        interpreter.process_page(page)

    text = out_text.getvalue()
    fp.close()
    text_converter.close()
    out_text.close()
    
    #Teil 2 (Erstellen einer .txt Datei und speichern des Textes aus Teil 1)
    file = open(name_txt_file + '.txt', "w", encoding = "utf-8")
    file.write(text)
    file.close()
