# kadai6-2.py

import requests

# -----------------------------------------------
# オープンデータ名: Open-Meteo API
# 概要: 緯度・経度を指定して、過去・未来の天気情報を取得できる
# エンドポイント: https://api.open-meteo.com/v1/forecast
# 機能: 緯度・経度に応じた予報（気温や降水量など）をJSON形式で返す
# 使い方: URLに緯度経度やパラメータをクエリとして指定してGET送信
# -----------------------------------------------

# 例: 東京の天気予報（緯度35.6895, 経度139.6917）
url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 35.6895,
    "longitude": 139.6917,
    "hourly": "temperature_2m",   # 2m高さの気温を取得
    "forecast_days": 1,
    "timezone": "Asia/Tokyo"
}

response = requests.get(url, params=params)
data = response.json()

# 最初の数時間分の気温データを表示
print("=== 東京の1時間ごとの気温（摂氏）===")
for time, temp in zip(data["hourly"]["time"][:5], data["hourly"]["temperature_2m"][:5]):
    print(f"{time}: {temp}°C")
