import requests
from bs4 import BeautifulSoup
import json

item_list = []


def getRepositoryData():
    with open('./data/products.json', 'r') as file:
        data = json.load(file)

        for item in data['items']:
            product = {
                "name": item,
                "resource": "https://github.com/danishi/gc-service-list-api/blob/main/data/products.json"
            }
            item_list.append(product)


def getServiceSite():
    url = 'https://cloud.google.com/products?hl=en'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    service_names = [service.text.strip() for service in soup.select('.CilWo')]
    service_names_set = set(service_names)

    for name in list(service_names_set):
        product = {
            "name": name,
            "resource": url
        }
        item_list.append(product)


def getDiscoveryApi():
    url = "https://www.googleapis.com/discovery/v1/apis"
    response = requests.get(url)
    data = response.json()

    api_titles = [item['title'] for item in data['items']]
    api_titles_set = set(api_titles)

    for title in list(api_titles_set):
        product = {
            "name": title,
            "resource": url
        }
        item_list.append(product)


def saveJsonFile():
    products = {
        "items": item_list,
        "count": len(item_list),
    }

    with open('./docs/products.json', 'w') as file:
        json.dump(products, file)


if __name__ == "__main__":
    getRepositoryData()
    getServiceSite()
    getDiscoveryApi()
    saveJsonFile()
