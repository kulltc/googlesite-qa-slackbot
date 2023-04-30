import time
from .web_scraper import WebScraper
from .html_parser import HTMLParser

class GoogleSiteCrawler:
    def __init__(self, cookies, wait_seconds, css_selector):
        self.cookies = cookies
        self.wait_seconds = wait_seconds
        self.css_selector = css_selector

    def crawl(self, starting_url, content_processor_callback):
        url_queue = [starting_url]
        visited_urls = set()

        parser = HTMLParser()
        scraper = WebScraper()

        while url_queue:
            current_url = url_queue.pop(0)
            if current_url not in visited_urls:
                visited_urls.add(current_url)

                html_content = scraper.fetch_content(current_url, self.cookies)
                if html_content:
                    content_processor_callback(html_content, current_url, self.css_selector)

                    links = parser.extract_links(html_content, current_url, domain=starting_url)
                   
                    url_queue.extend(links)

                time.sleep(self.wait_seconds)
