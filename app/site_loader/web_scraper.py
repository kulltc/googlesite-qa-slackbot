import requests

class WebScraper:
    def fetch_content(self, url, cookies):
        try:
            response = requests.get(url, cookies=cookies)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Error fetching content from {url}: {e}")
            return None
