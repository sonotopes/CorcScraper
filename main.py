from selectolax.parser import HTMLParser
from utils.extract import extract_all_html
from config.tools import get_config
from utils.parse import parse_raw_attributes
from utils.process import save_to_file
from utils.process import format_and_transform
import pandas as pd

if __name__ == '__main__':

    config_settings = get_config()

    html = extract_all_html(
        from_url=config_settings.get('URL'),
        wait_for=config_settings.get('body_node').get('selector')
    )

    html_tree = HTMLParser(html)
    divs = html_tree.css(config_settings.get('body_node').get('selector'))

    real_estate_data = []

    for d in divs:
        attrs = parse_raw_attributes(d, config_settings.get("item"))
        format_and_transform(attrs)
        print(attrs)
        real_estate_data.append(attrs)
        save_to_file("extract", real_estate_data)

