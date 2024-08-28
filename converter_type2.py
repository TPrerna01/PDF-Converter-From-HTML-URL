'''   convert html code or file/doc into pdf aswell as url of any site and it convert into pdf 
#  Module => weasyprint
'''

from weasyprint import HTML
import os

url = input('Enter URL : ')
file_name = input('Enter Filename : ')

if os.path.isfile(url):
    pdf_file = HTML(filename=url)
    pdf_file.write_pdf(f'{file_name}.pdf')
else:
    pdf_file = HTML(url=url).write_pdf(f'{file_name}.pdf')