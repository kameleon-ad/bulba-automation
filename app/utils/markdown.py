import html2text


def parse_html_to_md(html_content: str):
    return HTML2MARKDOWN_PARSER.handle(html_content)


HTML2MARKDOWN_PARSER = html2text.HTML2Text()
HTML2MARKDOWN_PARSER.body_width = 0
