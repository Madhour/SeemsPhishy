from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO
from pdfminer.pdfpage import PDFPage
import requests
import unicodedata
import re
import os
from SeemsPhishy.utils import set_logger


class TextParser:

    def __init__(self, files):
        self.files = files  # {header-title : url}
        self.text = {}
        self.log = set_logger("OCR", mode="debug")

    def convert_files(self, filenumber):
        counter = 0
        # download pdfs and parse text
        self.log.debug(self.files)
        self.log.debug(filenumber)
        for key in self.files:
            if counter < int(filenumber):
                # self.downloadPDF(self.files[key], key)
                try:
                    self.log.debug(self.files[key])
                    self.log.debug(key)
                    self.download_pdf(self.files[key], key)
                except Exception as e:
                    self.log.error(e)
                    counter = counter + 1
                    self.log.warn("Exception")
                counter = counter + 1
            else:
                self.log.info("Skipped")

        return self.text

    def text_parser(self, pdf_path, filename):
        self.log.debug(pdf_path)
        self.log.debug(filename)
        # Part 1 (extract text from file)
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        codec = 'utf-8'
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(pdf_path, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page in PDFPage.get_pages(fp, pagenos=set(), maxpages=0, caching=True, check_extractable=False):
            interpreter.process_page(page)

        text = out_text.getvalue()
        fp.close()
        text_converter.close()
        out_text.close()

        text = text.replace("'", "")
        text = text.replace('"', '')

        self.text[filename] = text

        # Part 2 (Create .txt file and save the text from part 1
        # file = open(name_txt_file + '.txt', "w", encoding = "utf-8")
        # file.write(text)
        # file.close()

    def slugify(self, value, allow_unicode=False):
        value = str(value)
        if allow_unicode:
            value = unicodedata.normalize('NFKC', value)
        else:
            value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
        value = re.sub(r'[^\w\s-]', '', value.lower())
        return re.sub(r'[-\s]+', '-', value).strip('-_')

    def download_pdf(self, url_name, filename):
        full_filename = filename
        filename = filename[:25].replace(" ", "_")
        slugified = self.slugify(filename)
        # filepath = f"/dataretrieval/lib/PDF/{slugified}.pdf"
        filepath = f"./{slugified}.pdf"
        response = requests.get(url_name)
        self.log.debug(filename)
        self.log.debug(slugified)
        file = open(filepath, "wb")
        self.log.debug(file)
        file.write(response.content)
        file.close()
        # convert2text
        self.text_parser(filepath, full_filename)
        os.remove(filepath)
