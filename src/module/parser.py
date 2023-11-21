import requests
from bs4 import BeautifulSoup


def get_html(url: str) -> str:
    r = requests.get(url) # get html 
    soup = BeautifulSoup(r.text, "html.parser") # set parser interface
    print("[HTML FOUND]")
    return soup.prettify()
        
def parse_html(html: str, tag: str, tag_class: str = None) -> list:
    soup = BeautifulSoup(html, "html.parser") # set parser interface
    return soup.find_all(tag, class_=tag_class)