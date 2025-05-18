import firebase_admin
from firebase_admin import credentials, firestore
import os

# 初期化（すでに初期化済みならスキップされる）
if not firebase_admin._apps:
    cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")  # 環境変数でキーを指定
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

db = firestore.client()
collection_name = "notified_ebay_items"  # コレクション名を指定

def is_notified(item_id):
    doc = db.collection(collection_name).document(item_id).get()
    return doc.exists

def mark_as_notified(item_id):
    db.collection(collection_name).document(item_id).set({"notified": True})
