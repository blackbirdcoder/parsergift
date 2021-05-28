# ============ Important data ================
TARGET_URL = 'https://giftpack.ru'
TARGET_PATH = '/catalog/'
# parameter for navigating through product pages
NAVIGATION_NAME = 'PAGEN_2'
# pretend to be different
USER_AGENT = 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.1; Trident/4.0)'
# parser HTML
MARKUP_ANALYZER = 'lxml'
# Result folder
RESULT_FOLDER = 'output'
# Progress bar settings
PROGRESS_BAR_SETTING = '{l_bar}{bar:10}{r_bar}{bar:-10b}'
# ============= settings for spreadsheet ======
spreadsheet_name = 'goods.xlsx'
heading_style = {'bold': True}
headings = [('A1', 'Категория'), ('B1', 'Артикул'),
            ('C1', 'Описание'), ('D1', 'Изображение'),
            ('E1', 'Цена'), ('F1', 'Валюта')]
column_width = [('A:A', 27), ('B:B', 20), ('C:C', 75), ('D:D', 20), ('E:E', 10), ('F:F', 10)]
# ==================== intro ==================
INTRO = fr"""
    ------------------------------------------------
    ___  ____ ____ ____ ____ ____    ____ _ ____ ___ 
    |__] |__| |__/ [__  |___ |__/    | __ | |___  |  
    |    |  | |  \ ___] |___ |  \    |__] | |     |  

         Data from the site {TARGET_URL}
             turns into an excel table
    ------------------------------------------------
    """
