from excel_reader import load_wantlist
from ebay_client import search_ebay_items
from notifier.discord import send_discord_notification
from notifier.gmail import send_gmail_notification
from firestore_client import is_notified, mark_as_notified

def main():
    wantlist = load_wantlist()

    for entry in wantlist:
        artist = entry['artist']
        title = entry['title']
        query = f"{artist} {title}"
        results = search_ebay_items(query)

        for item in results:
            if not is_notified(item['id']):
                # 通知を送る
                send_discord_notification(artist, title, item)
                send_gmail_notification(artist, title, item)
                # 通知済みとしてマーク
                mark_as_notified(item['id'])

if __name__ == "__main__":
    main()
