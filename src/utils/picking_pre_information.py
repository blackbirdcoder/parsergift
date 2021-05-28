from bs4 import BeautifulSoup
from tqdm import tqdm
from data import TARGET_URL, TARGET_PATH, MARKUP_ANALYZER, PROGRESS_BAR_SETTING  # noqa
from .get_document import get_document


def picking_pre_information():
    """
    provides the collection of all the necessary information
    for the further successful retrieval of goods
    :return: list of dictionaries with information about the assortment
    """
    information = []

    def get_paths_assortment():
        """
        getting the paths along which the goods are located
        :return: path list
        """
        paths = []
        document = get_document(TARGET_URL + TARGET_PATH)
        soup = BeautifulSoup(document, MARKUP_ANALYZER)
        elements_a = soup.select('td.section_info>a')
        for current_element_a in elements_a:
            if current_element_a['href']:
                paths.append(current_element_a['href'])
        del soup
        return paths

    paths_assortment = get_paths_assortment()

    def technical_details_about_markup(path):
        """
        works on page elements
        :param path: paths where the goods
        """
        nonlocal information
        category_title = ''
        numbers = []
        document = get_document(TARGET_URL + path)
        soup = BeautifulSoup(document, MARKUP_ANALYZER)
        name_category = soup.select('span.number>span[itemprop="name"]')
        pagination_elements = soup.select('div.nums a[rel="next"]')

        def get_category_title():
            """
            get category name
            """
            nonlocal category_title
            text = name_category[0].get_text().strip()
            if text:
                category_title = text

        get_category_title()

        def get_numbers_pagination():
            """
            getting a list of numbers from pagination items
            """
            nonlocal numbers
            if pagination_elements:
                for current_element in pagination_elements:
                    try:
                        numbers.append(int(current_element.get_text()))
                    except ValueError:
                        numbers.append(1)
            else:
                numbers.append(1)

        get_numbers_pagination()

        def create_report():
            """
            create a report by adding some technical data about the markup
            """
            information.append({'title': category_title, 'path': path, 'number_pages': max(numbers)})

        create_report()
        del soup

    for current_path in tqdm(paths_assortment, desc='Preliminary preparation', bar_format=PROGRESS_BAR_SETTING):
        technical_details_about_markup(current_path)

    return information
