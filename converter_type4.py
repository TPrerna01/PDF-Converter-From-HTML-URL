from playwright.sync_api import sync_playwright
import pdfkit
import os

class PDFCONVERTER:
    ''' URL to PDF Converter Code'''
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename 

    def pdf_converter(self):
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                page.set_viewport_size({"width": 1280, "height": 1024})
                if os.path.isfile(self.url):
                    with open(self.url, 'r', encoding='utf-8') as file:
                        html_content = file.read()
                    page.set_content(html_content, wait_until='networkidle')
                else:
                    page.goto(self.url, wait_until='networkidle')
                
                    
                page.emulate_media(media='screen')
                page.pdf(path=f'{self.filename}.pdf', format='A4', 
                        print_background=True )
                browser.close()
        except:
            print('some  issue occur')
       

if __name__=='__main__':
    user_input_url = input('Enter URL or Path : ')
    filename = input('Enter the pdf file name : ')

    pdf_convert = PDFCONVERTER(user_input_url, filename)
    pdf_convert.pdf_converter()

# /home/lucifer/Desktop/traning/front end/Bootstrap/Task8.html
#  /home/lucifer/Downloads/corona-free-dark-bootstrap-admin-template-1.0.0/template/index.html