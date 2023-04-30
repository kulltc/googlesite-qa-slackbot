import html2text

class HTMLToMarkdown:
    def convert(self, html_elements):
        try:
            converter = html2text.HTML2Text()
            converter.ignore_links = True
            converter.ignore_images = True
            markdown_content = ''.join([converter.handle(str(element)) for element in html_elements])
            return markdown_content
        except Exception as e:
            print(f"Error converting HTML to Markdown: {e}")
            return ""
