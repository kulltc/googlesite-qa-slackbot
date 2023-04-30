from bs4 import BeautifulSoup
from urllib.parse import urljoin, urldefrag

class HTMLParser:
    def extract_content(self, html, css_selector):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            return soup.select(css_selector)
        except Exception as e:
            print(f"Error extracting content with selector '{css_selector}': {e}")
            return []

    def extract_links(self, html, base_url, domain):
       # try:
        soup = BeautifulSoup(html, 'html.parser')
        new_links = set()
        for link in soup.find_all('a', href=True):
            # Filter out unwanted links
            # Resolve the relative URL to an absolute URL
            absolute_url = urljoin(base_url, link['href'])
            # Normalize the URL by removing the fragment identifier
            normalized_url = self._normalize_url(absolute_url)

            if not normalized_url.startswith(domain) or self._is_unwanted_resource(normalized_url):
                continue

            new_links.add(normalized_url)
        
        return new_links
        #except Exception as e:
        #    print(f"Error extracting links: {e}")
        #    return []

    def _is_unwanted_resource(self, link):
        unwanted_extensions = ('.js', '.css', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.gitkeep')
        return link.lower().endswith(unwanted_extensions)

    def _normalize_url(self, url):
        # Remove the fragment identifier from the URL
        url, _ = urldefrag(url)
        return url