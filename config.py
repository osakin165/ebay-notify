import os

# Discord通知用Webhook URL
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# eBay App ID（承認後にRenderへ追加）
EBAY_APP_ID = os.getenv("EBAY_APP_ID")

SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
SHEET_NAME = "Wantlist"  # シート名に合わせて変更してOK
