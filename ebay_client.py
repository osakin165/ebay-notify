import requests
from config import EBAY_APP_ID

def search_ebay_items(query):
    url = "https://svcs.ebay.com/services/search/FindingService/v1"

    params = {
        "OPERATION-NAME": "findItemsByKeywords",
        "SERVICE-VERSION": "1.0.0",
        "SECURITY-APPNAME": EBAY_APP_ID,
        "RESPONSE-DATA-FORMAT": "JSON",
        "REST-PAYLOAD": "true",
        "keywords": query,
        "paginationInput.entriesPerPage": 5,
        "GLOBAL-ID": "EBAY-US",
        "categoryId": "11233"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    results = []
    items = data.get("findItemsByKeywordsResponse", [{}])[0].get("searchResult", [{}])[0].get("item", [])
    for item in items:
        title = item.get("title", [None])[0]
        url = item.get("viewItemURL", [None])[0]
        price = item.get("sellingStatus", [{}])[0].get("currentPrice", [{}])[0].get("__value__")

        results.append({
            "title": title,
            "url": url,
            "price": price
        })

    return results
