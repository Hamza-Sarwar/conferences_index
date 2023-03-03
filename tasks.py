from typing import List, Dict

import requests
from bs4 import BeautifulSoup
from validation import Conference
import pandas as pd
def get_conference_data(url):
    updated_url = url[0]
    html_parsed = requests.get(updated_url).text
    soup = BeautifulSoup(html_parsed, 'html.parser')
    # find the card-body div
    card_body = soup.find('div', {'class': 'card-body'})

    # get all the li tags in the first ul
    events = {}
    li_tags = card_body.find('ul', {'class': 'mb-2 list-unstyled'}).find_all('li')
    for li in li_tags:
        key = li.text.split(':')[0].strip()
        value = str(li.text.split(':')[-1].strip().replace('\n', ', '))
        events[key] = value

    description = card_body.find('div', id='event-description').text.strip().replace('\n', ' ')
    events['Description'] = description
    try:
        data = Conference(**events)
    except Exception as e:
        print(e)
    conf = dict(data)
    print(conf)
    df = pd.DataFrame([conf])
    print(df)
    df.to_csv('conferences_data.csv', mode='a', index=False, header=False)


