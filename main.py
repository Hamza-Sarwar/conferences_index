from concurrent.futures import ThreadPoolExecutor

import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_pages():
    pages = []
    for x in range(1, 589):
        pages.append(f'https://conferenceindex.org/conferences?page={x}')
    return pages


def get_conference(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    ul_tags = soup.find_all('ul')

    conferences = []
    for li in ul_tags[1].find_all('li'):
        date = li.contents[0].strip()
        title = li.a.string
        location = li.contents[2].strip()[1:-1]
        url = li.a['href']
        conferences.append({'Date': date, 'Title': title, 'Location': location, 'URL': url})

    # Save the extracted details in a Pandas dataframe
    df = pd.DataFrame(conferences)
    df.to_csv('conferences', mode='a', index=False, header=False)


if __name__ == '__main__':
    pages = get_pages()
    with ThreadPoolExecutor() as executor:
        executor.map(get_conference, pages)
