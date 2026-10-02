import requests
import json

# Tạm thời dùng mã này hoặc thay bằng API key thật của bạn trên sec-api.io
API_KEY = "10f4977bb1671bd790a2510c54f1a642e44f86ed3532a9a2042be082565de587"
URL = f"https://api.sec-api.io/mapping/exchange/NYSE?token={API_KEY}"

print("Bắt đầu kết nối với sec-api.io...")
response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    # Lưu toàn bộ dữ liệu trả về thành file JSON thô
    with open('raw_companies.json', 'w') as f:
        json.dump(data, f)
    print(f"Trích xuất thành công! Đã lưu thông tin của {len(data)} công ty.")
else:
    print(f"Lỗi kết nối API. Mã lỗi: {response.status_code}")
