from bs4 import BeautifulSoup
import requests
import re

def get_urls_with_target(url, target):

    # Fetch the webpage content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all anchor tags with href containing "seinfield"
        raw_links = [a['href'] for a in soup.find_all('a', href=True) if target.lower() in a['href'].lower()]
        # Clean links by replacing '%20' with a space or other character
        return raw_links
    else:
        print(f"Failed to fetch webpage: {response.status_code}")
        return None


def clean_multiple_hyphens(url):
    """
    Replace multiple consecutive hyphens with a single hyphen in a string.

    Args:
        url (str): The input string containing hyphens.

    Returns:
        str: The cleaned string with single hyphens.
    """
    return re.sub(r'-{2,}', '-', url)



def replace_spaces_with_hyphen(raw_links):
    '''
    takes list of strings as input

    replaces any white space with a single -

    '''
    cleaned_links = [ link.replace(' ', '-').replace('\xa0', '-').strip() for link in raw_links]
    # return the list of links
    cleaner_links = [clean_multiple_hyphens(link) for link in cleaned_links]
    return cleaner_links



def remove_from_urls(urls, txt):
    '''
    takes list of strings as input

    removes target txt (aka replaces target with "")

    '''
    return [url.replace(txt, "") for url in urls]

def replace_txt_in_urls(urls, target, change_to):
    '''
    takes list of strings as input

    replaces target txt with something

    '''

    return [url.replace(target, change_to) for url in urls]

