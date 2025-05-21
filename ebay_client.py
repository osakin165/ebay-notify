import requests
import logging
import os

logger = logging.getLogger(__name__)

# 必要な環境変数（OAuthトークン）
EBAY_OAUTH_TOKEN = os.getenv("EBAY_OAUTH_TOKEN")

# eBay Browse API のエンドポイント
BROWSE_API_URL = "https://api.ebay.com/buy/browse/v1/item_summary/search"


def search_ebay_items(query, limit=5):
    if not EBAY_OAUTH_TOKEN:
        logger.error("eBay OAuthトークンが設定されていません")
        return []

    headers = {
        "Authorization": f"Bearer {EBAY_OAUTH_TOKEN}",
        "Content-Type": "application/json",
    }

    params = {
        "q": query,
        "limit": limit,
    }

    try:
        response = requests.get(BROWSE_API_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("itemSummaries", [])

    except requests.exceptions.HTTPError as e:
        logger.error(f"[ERROR] Failed to fetch from Browse API: {e}")
        return []
