'''   convert html code or file/doc into pdf aswell as url of any site and it convert into pdf 
#  Module => pdfkit && wkhtmltopdf
'''

import pdfkit
from weasyprint import HTML

def final_output(pdfconfig, options):
    ''' selecting convertion type and procedure'''
    while True:
        select = ''' 1: Document or HTML FILE \n 2: URL(SITE)'''
        print(select)
        user_input = int(input('select above option : '))

        try :
            if user_input < 3 and user_input > 0:
                output_data = input('Enter file path or url : ')
                pdf_name = input('Enter PDF Name : ')

                if user_input == 1:
                    try:
                        pdfkit.from_file(output_data, f'{pdf_name}.pdf', configuration=pdfconfig, options=options)
                    except Exception :
                        print("Can't cange this data some issue occur")
                    break
                elif user_input == 2:
                    try:
                        pdfkit.from_url(output_data, f'{pdf_name}.pdf', configuration=pdfconfig, options=options)
                    except :
                        print('Issue occur while url conversion')
                    break
        except :
            print('Invalid input')


if __name__=='__main__':
    wkhtml_path = '/usr/bin/wkhtmltopdf'
    pdfconfig = pdfkit.configuration(wkhtmltopdf = wkhtml_path)
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'enable-local-file-access': None,  
        'javascript-delay': '1000',       
        'no-stop-slow-scripts': None,      
        'load-error-handling': 'ignore',   
        'zoom': '1.0',                     
    }

    #  calling file & url convertion method
    final_output(pdfconfig, options)