from bs4 import BeautifulSoup
from tqdm import tqdm
from data import NAVIGATION_NAME, TARGET_URL, MARKUP_ANALYZER, PROGRESS_BAR_SETTING # noqa
from .get_document import get_document


def take_goods(pre_info: list):
    """
    Extracts goods from a document, goods are collected in a dictionary and stored in the list.
    :param pre_info: list with parameters for successful crawling of all categories
    :return: goods from the store
    """
    content_goods = []
    for current_item in tqdm(pre_info, desc='Retrieving goods', bar_format=PROGRESS_BAR_SETTING):
        path = current_item.get('path')
        number = current_item.get('number_pages')
        for current_number in range(1, number + 1):
            payload = {NAVIGATION_NAME: str(current_number)}
            document = get_document(TARGET_URL + path, parameter=payload)
            soup = BeautifulSoup(document, MARKUP_ANALYZER)
            block_product_card = soup.select('div.catalog_item.item_wrap>div')
            for current_element in block_product_card:
                blank = {'category': current_item.get('title'), 'vendor_code': None, 'desc': None, 'link_image': None,
                         'price': None, 'currency': None}
                vendor_code = current_element.select('div.article_block')
                if vendor_code:
                    blank['vendor_code'] = vendor_code[0].get_text().strip().replace('Арт: ', '')
                desc = current_element.select('div.item-title>a>span')
                if desc:
                    blank['desc'] = desc[0].get_text().strip()
                if current_element.img:
                    blank['link_image'] = TARGET_URL + current_element.img['src']
                price = current_element.select('span.price_value>span.price_value')
                if price:
                    blank['price'] = price[0].get_text().strip()
                currency = current_element.select('span.price_value>span.price_currency')
                if currency:
                    blank['currency'] = currency[0].get_text().strip().replace('.', '')
                content_goods.append(blank)
            del soup
    return content_goods
