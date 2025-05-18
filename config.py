import os

# Discord通知用Webhook URL
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# eBay App ID（承認後にRenderへ追加）
EBAY_APP_ID = os.getenv("EBAY_APP_ID")

# Excelファイル名（Renderでは事前アップロードが必要）
EXCEL_FILE_PATH = "ebayプログラム用want list.xlsx"
