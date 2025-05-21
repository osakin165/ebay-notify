import requests
import re
from config import EBAY_APP_ID

def clean_query(query):
    # エラーを引き起こす記号を除去し、文字数も制限
    query = re.sub(r"[\"'&/\\%+]", "", query)
    return query[:50]

def search_ebay_items(query):
    url = "https://svcs.ebay.com/services/search/FindingService/v1"

    safe_query = clean_query(query)

    params = {
        "OPERATION-NAME": "findItemsByKeywords",
        "SERVICE-VERSION": "1.0.0",
        "SECURITY-APPNAME": EBAY_APP_ID,
        "RESPONSE-DATA-FORMAT": "JSON",
        "REST-PAYLOAD": "true",
        "keywords": safe_query,
        "paginationInput.entriesPerPage": 5,
        "GLOBAL-ID": "EBAY-US",
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"[ERROR] Skipped keyword '{safe_query}' due to HTTPError: {e}")
        return []
    except Exception as e:
        print(f"[ERROR] Unexpected error for '{safe_query}': {e}")
        return []

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
