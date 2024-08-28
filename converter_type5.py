from playwright.sync_api import sync_playwright
from urllib.parse import urlparse

def is_url(path):
    """Check if the path is a URL."""
    parsed = urlparse(path)
    return bool(parsed.netloc and parsed.scheme)

def convert_to_pdf(input_path, output_pdf_path):
    """Convert HTML file or URL to PDF using Playwright."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        if is_url(input_path):
            page.set_viewport_size({'width': 1200, 'height': 800})
            page.goto(input_path, wait_until='networkidle')
        else:
            with open(input_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
            page.set_content(html_content, wait_until='networkidle')

        page.screenshot(path='screenshot_before_pdf.png')
        page.emulate_media(media='screen')
        page.pdf(
            path=output_pdf_path,      
            format='A4',                 
            print_background=True,        
            margin={'top': '1in', 'right': '1in', 'bottom': '1in', 'left': '1in'}
        )
        
        browser.close()

def final_output():
    """Select conversion type and procedure."""
    while True:
        select = '''1: Document or HTML FILE\n2: URL (SITE)'''
        print(select)
        user_input = int(input('Select the above option: '))

        try:
            if user_input in [1, 2]:
                input_data = input('Enter file path or URL: ')
                pdf_name = input('Enter PDF Name: ')

                output_pdf_path = f'{pdf_name}.pdf'

                if user_input == 1 or user_input == 2:
                    try:
                        convert_to_pdf(input_data, output_pdf_path)
                        print(f'PDF successfully created: {output_pdf_path}')
                    except Exception as e:
                        print(f"An error occurred: {e}")
                    break
            else:
                print('Invalid option. Please select 1 or 2.')
        except Exception as e:
            print(f'An error occurred: {e}')

if __name__ == '__main__':
    # Call the conversion method
    final_output()
