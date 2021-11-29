import pdf2image, pytesseract, os
from pytesseract import Output, TesseractError


def pdf_to_text(pdf_path):
    text = ""
    images = pdf2image.convert_from_path(pdf_path)#converts pages to image
    
    for image in images:#for every page (in form of image)
        ocr_dict = pytesseract.image_to_data(image, lang='eng', output_type=Output.DICT)#image_to_string()
        text += " ".join(ocr_dict['text'])

    return text

