import requests
from config import DISCORD_WEBHOOK_URL

def send_discord_notification(artist, title, ebay_item):
    message = f"""📢 **eBay出品通知**
"**{artist} - {title}**" が見つかりました！

💿 タイトル: {ebay_item['title']}
💰 価格: {ebay_item['price']} USD
🔗 [商品ページ]({ebay_item['url']})
"""

    payload = {"content": message}
    response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
    response.raise_for_status()

