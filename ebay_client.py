import requests
import os

# 必要に応じて環境変数やconfig.pyに移してください
EBAY_APP_ID = os.getenv("EBAY_APP_ID")  # 例: "Your-eBay-AppID"

def search_ebay_items(query, category_id="11233", limit=5):
    url = "https://svcs.ebay.com/services/search/FindingService/v1"
    params = {
        "OPERATION-NAME": "findItemsByKeywords",
        "SERVICE-VERSION": "1.0.0",
        "SECURITY-APPNAME": EBAY_APP_ID,
        "RESPONSE-DATA-FORMAT": "JSON",
        "REST-PAYLOAD": "true",
        "categoryId": category_id,
        "keywords": query,
        "paginationInput.entriesPerPage": limit,
        "GLOBAL-ID": "EBAY-US"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    items = []
    results = response.json().get("findItemsByKeywordsResponse", [])[0].get("searchResult", [])[0].get("item", [])

    for item in results:
        items.append({
            "id": item["itemId"][0],
            "title": item["title"][0],
            "price": item["sellingStatus"][0]["currentPrice"][0]["__value__"],
            "url": item["viewItemURL"][0],
        })

    return items
