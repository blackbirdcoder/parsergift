import requests
import data # noqa


def get_document(url, parameter=None):
    """
    Create session makes a request to the specified address,
    returns content on success, otherwise it will show an error
    :param url: string with the site address
    :param parameter: parameters for address
    :return: object page content
    """
    session = requests.Session()
    headers = {
        'User-Agent':  data.USER_AGENT
    }
    response = session.get(url, headers=headers, params=parameter)
    try:
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as error:
        print(error)
