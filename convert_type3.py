import requests
import pdfkit
from bs4 import BeautifulSoup
import os


class PDFCONVERTER:
    wkhtml_path = '/usr/bin/wkhtmltopdf'
     
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename 
        self.pdfconfig = pdfkit.configuration(wkhtmltopdf = self.wkhtml_path)
        self.options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",                     
        }

    def pdf_converter(self):
                file_data = self.url
        # try : 
                # pdfkit.from_file(self.url, f'{self.filename}.pdf', configuration=self.pdfconfig, options=self.options)
                # print("Can't cange this data some issue occur")
            # try:
                pdfkit.from_string(file_data.prettify(), f'{self.filename}.pdf', configuration=self.pdfconfig, options=self.options)
        #     except :
        #         print('Issue occur while url conversion')
        # except :
        #     print('Invalid input')


if __name__=='__main__':
    user_input_url = input('Enter URL : ')
    response = requests.get(user_input_url)
    url_record = BeautifulSoup(response.text, 'html.parser')
    filename = input('Enter the pdf file name : ')

    #  calling the pdf converter_class
    pdf_convert = PDFCONVERTER(url_record, filename)
    pdf_convert.pdf_converter()
