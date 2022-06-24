from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import logging
import argparse
import time


def main(url: str,
         html_element: str,
         is_id: bool,
         identifier: str,
         max_artists: int):

    """
    Scrapes the festival lineup page for artists

    :url:           url of page

    :html_element:  type of html element that has artist info
                    (div, span, p, etc.) & make sure to add https://

    :is_id:         does the html_element with artist name
                    have an id or class identifier?

    :identifier:    the name of id or class

    :max_artists:   the max number of items to retrieve
    """

    # Run Chrome in headless mode (chrome will not pop up)
    # and set web driver logging mode to silent
    options = Options()
    options.headless = True
    logging.getLogger('WDM').setLevel(logging.NOTSET)

    # get url
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    # wait for page load
    time.sleep(5)

    # parse
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # find elements
    if is_id:
        output = soup.find_all(html_element, id=identifier)
    else:
        output = soup.find_all(html_element, class_=identifier)

    count = 0
    for artist in output:
        print(artist.text)
        count += 1
        if count == max_artists:
            break


if __name__ == '__main__':
    # parse arguments
    parser = argparse.ArgumentParser(
        description="Scrape website for artist names")
    parser.add_argument(
        'url',
        type=str, metavar='url',
        help='a url for a page with festival artists -- include http/https://')
    parser.add_argument(
        'html_element',
        type=str,
        metavar='html_element',
        help='html element containing the artist')
    parser.add_argument(
        'id_or_class',
        type=str,
        choices=['id', 'class'],
        help='is the identifier an id or class')
    parser.add_argument(
        'identifier',
        type=str,
        help='name of the id or class')
    parser.add_argument(
        '--max',
        type=int,
        default=100,
        help='max number of items to parse')
    args = parser.parse_args()

    # scrape
    main(
        args.url,
        args.html_element,
        args.id_or_class == 'id',
        args.identifier,
        args.max)
