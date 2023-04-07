import serial
import time
import requests
import json
from local import URL_SEND_ENDPOINT,ACCESS_TOKEN

ser = serial.Serial('COM3', 9600)
time.sleep(2)

def send_post_request(data):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token {ACCESS_TOKEN}"
    }
    response = requests.post(URL_SEND_ENDPOINT, headers=headers, data=json.dumps({'value' : data}))

    print("Status code: ", response.status_code,'data',data)

start_time = time.time() # プログラム開始時のタイムスタンプを取得
time_interval = 10 # 送信間隔（秒）
data_buffer = [] # データを一時的に格納するリスト

try:
    while True:
        current_time = time.time() # 現在時刻のタイムスタンプを取得
        data = ser.readline().decode().strip()
        data_buffer.append(float(data)) # バッファにデータを追加
        print("Received data: ", data)
        if current_time - start_time >= time_interval and data_buffer: # 送信間隔が経過しているか確認
            avg_data = sum(data_buffer) / len(data_buffer) # バッファ内のデータの平均値を計算
            send_post_request(avg_data) # POSTリクエストを送信
            data_buffer = [] # バッファを空にする
            start_time = time.time() # 送信後、開始時刻を更新
except KeyboardInterrupt:
    ser.close()
    print("プログラムを終了しました")
