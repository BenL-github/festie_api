import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    url = 'https://sfoutsidelands.com/lineup/'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    # wait for page load
    time.sleep(3)


    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')


    output = soup.find_all('div', class_='ds-artist-name')

    count = 0
    max_artists = 100
    for artist in output:
        print(artist.text)
        count += 1
        if count == max_artists:
            break

if __name__ == '__main__':
    main()