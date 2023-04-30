
from .authentication import Authentication
from .crawler import GoogleSiteCrawler
from .html_parser import HTMLParser
from .html_to_markdown import HTMLToMarkdown
from .file_writer import FileWriter
from urllib.parse import quote
from .__init__ import config

def content_processor_callback(html_content, current_url, css_selector):
    try:
        parser = HTMLParser()
        extracted_elements = parser.extract_content(html_content, css_selector)
        converter = HTMLToMarkdown()
        markdown_content = converter.convert(extracted_elements)
        
        # Use percent encoding to create a safe filename
        encoded_url = quote(current_url, safe='')
        filename = f"./data/site_contents/{encoded_url}.md"

        writer = FileWriter()
        writer.write_to_file(markdown_content, filename)
    except Exception as e:
        print(f"Error processing content for URL '{current_url}': {e}")

def load_site_data():    
    url = config.get('DEFAULT', 'url')
    css_selector = config.get('DEFAULT', 'css_selector')
    wait_seconds = config.getint('DEFAULT', 'wait_seconds')
    cookie_string = config.get('DEFAULT', 'cookie_string')

    auth = Authentication(cookie_string)
    cookies = auth.get_cookies()

    if cookies:
        crawler = GoogleSiteCrawler(cookies, wait_seconds, css_selector)
        crawler.crawl(url, content_processor_callback)
    else:
        print("Authentication failed. Exiting...")
