# kadai6-1.py

import requests
import json

# -----------------------------------------------
# データの種類: 労働力調査（基本集計）2023年平均結果
# 統計表ID: 0003423642
# エンドポイント: https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData
# 機能: 指定された統計表IDのデータをJSON形式で取得
# APIキー: 各自取得したe-Stat APIキーを使う（下の"YOUR_APP_ID"を自分のに変更）
# -----------------------------------------------

app_id = "56b95428663b8d68068d887950ff04c21b03a11"  # ← 自分のAPIキーに置き換えて！

url = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": app_id,
    "statsDataId": "0003423642",  # 労働力調査の統計表ID
    "lang": "J",                  # 日本語
    "metaGetFlg": "Y",
    "cntGetFlg": "N"
}

response = requests.get(url, params=params)
data = response.json()

# 取得したデータのうち、最初の5項目だけ表示（結果が多すぎるので）
for i, item in enumerate(data["GET_STATS_DATA"]["STATISTICAL_DATA"]["DATA_INF"]["VALUE"][:5]):
    print(f"{i+1}. {item}")
