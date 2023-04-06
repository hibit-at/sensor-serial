import serial
import time
import requests

ser = serial.Serial('COM3', 9600)
time.sleep(2)

url = "https://yourserver.com/your/api/endpoint"

def send_post_request(data):
    payload = {'value': data}
    response = requests.post(url, data=payload)
    print("Status code: ", response.status_code)

start_time = time.time() # プログラム開始時のタイムスタンプを取得
time_interval = 1 # 送信間隔（秒）

try:
    while True:
        current_time = time.time() # 現在時刻のタイムスタンプを取得
        data = ser.readline().decode().strip()
        print("Received data: ", data)
        if current_time - start_time >= time_interval: # 送信間隔が経過しているか確認
            send_post_request(data) # POSTリクエストを送信
            start_time = time.time() # 送信後、開始時刻を更新
except KeyboardInterrupt:
    ser.close()
    print("プログラムを終了しました")
