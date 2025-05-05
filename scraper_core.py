import requests
from bs4 import BeautifulSoup as bs4

def extract_tags(args: list) -> list:
    """
    Extract tags from the command line arguments.

    """
    tags = []
    for tag in args[1:]:
        if tag.startswith('-'):
            tags.append(tag.replace('-', ''))
    return tags



def fetch_url_all_content(url:str) -> str:
    """
    Fetch the content of a URL and return it as a string.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def fetch_url_content(url:str ,args: list)-> str:
    taglist = extract_tags(args)
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = bs4(response.text, 'lxml')
        content = soup.find_all(taglist)
        return content
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def fetch_url_content_by_class(url, class_name,args) -> str:
    """
    Fetch the content of a URL and return it as a string.
    """
    taglist = extract_tags(args)
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = bs4(response.text, 'lxml')
        content = soup.find_all(taglist[0], class_name)
        return content
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None




    