# extractor.py

from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

class PDFExtractor(object):

    def pdf_to_text(self, pdf_file, pages=None):
        # allows multiple pages to be passed in as a parameter
        if pages:
            num_of_pages = set(pages)
        else:
            num_of_pages = set()
        
        output = StringIO()
        manager = PDFResourceManager()

        # parameters require a resource manager and an output text stream
        converter = TextConverter(manager, output, laparams=LAParams())

        # parameters require a resource manager and a text converter
        interpreter = PDFPageInterpreter(manager, converter)

        
        