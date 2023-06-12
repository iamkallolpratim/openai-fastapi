from database.database import database
from bs4 import BeautifulSoup
from collections import deque
from html.parser import HTMLParser
from dotenv import load_dotenv
import openai
import os
import requests
from models.url import URL
from urllib.parse import urljoin, urlparse
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from datetime import datetime

headers = {'User-Agent': 'Mozilla/5.0'}


load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")
collection = database.urls
collection_crawl_data = database['crawler-data']
HTTP_URL_PATTERN = r'^http[s]{0,1}://.+$'

def hello_world(q):
    try:
        if not q:
            raise ValueError("Parameter 'q' is required")
        response = {"message": "Hello World " + str(q)}
        return response
    except ValueError as e:
        error_message = "An error occurred: " + str(e)
        return {"error": error_message}


def generate_text(prompt):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Make a sentence from the following words: {prompt}"}
        ]
    )
    return response['choices'][0]['message']['content']




def remove_newlines(serie):
    serie = serie.str.replace('\n', ' ')
    serie = serie.str.replace('\\n', ' ')
    serie = serie.str.replace('  ', ' ')
    serie = serie.str.replace('  ', ' ')
    return serie



def crawl_url(url, visited_urls):
    visited_urls.add(url)
    
    if url.startswith("javascript:"):
        return
    
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError as e:
        print(f"ConnectionError: Failed to establish a connection with {url}")
        return
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    data = {
        "text": remove_newlines(soup.get_text()),
    }

    timestamp = datetime.now()
    
    
    collection_crawl_data.insert_one({
        "siteId": url,
        "url": url,
        "data": data,
        "timestamp": timestamp
    })

    for link in soup.find_all("a"):
        child_url = link.get("href")
        if child_url and not child_url.startswith("#") and not child_url.startswith("javascript:"):
            absolute_url = urljoin(url, child_url)
            if absolute_url not in visited_urls:
                crawl_url(absolute_url, visited_urls)



async def process_url_handler(data: dict):
    timestamp = datetime.utcnow()
    base_url = data.get("url")
    local_domain = urlparse(base_url).netloc
    queue = deque([base_url])
    visited_urls = set([base_url])
    item = {
        "url": data.get("url"),
        "timestamp": timestamp,
        "userID": data.get("userID")
    }
    collection.insert_one(item)
    # Start crawling
    while queue:
        base_url = queue.pop()
        print(base_url)  # for debugging and to see the progress
        crawl_url(base_url, visited_urls)
    return {"message": f"URLs processed and saved successfully. {data}"}
