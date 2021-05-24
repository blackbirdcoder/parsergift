# ======== Important data =============
TARGET_URL = 'https://giftpack.ru'
TARGET_PATH = '/catalog/'
# parameter for navigating through product pages
NAVIGATION_NAME = 'PAGEN_2'
# pretend to be different
USER_AGENT = 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.1; Trident/4.0)'
# parser HTML
MARKUP_ANALYZER = 'lxml'

# ============= logo =================
INTRO = fr"""
    ------------------------------------------------
    ___  ____ ____ ____ ____ ____    ____ _ ____ ___ 
    |__] |__| |__/ [__  |___ |__/    | __ | |___  |  
    |    |  | |  \ ___] |___ |  \    |__] | |     |  

         Data from the site {TARGET_URL}
             turns into an excel table
    ------------------------------------------------
    """
