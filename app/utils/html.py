import lxml
from lxml.html.clean import Cleaner

HTML_CLEANER = Cleaner()
HTML_CLEANER.javascript = True
HTML_CLEANER.style = True


def clear_scripts(html_content):
    parsed_html = lxml.html.fromstring(html_content)
    cleaned_html = HTML_CLEANER.clean_html(parsed_html)
    return lxml.html.tostring(cleaned_html)
