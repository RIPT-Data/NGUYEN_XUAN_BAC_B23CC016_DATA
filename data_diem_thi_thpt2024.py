import requests # type: ignore
import time
import pandas as pd # type: ignore

# Khởi tạo danh sách để lưu dữ liệu
data = []

for x in range(25000001, 25000100):
    scraping_url = "https://dantri.com.vn/thpt/1/0/99/" + str(x) + "/2024/0.2/search-gradle.htm"
    payload = {}
    headers = {}

    try:
        response = requests.request("GET", scraping_url, headers=headers, data=payload)

        if response.status_code == 200:
            info = response.json()['student']
            diem = {
                'SBD': info['sbd'],
                'Toán': info['toan'],
                'Văn': info['van'],
                'Ngoại Ngữ': info['ngoaiNgu'],
                'Sinh Học': info['sinhHoc'],
                'DiemTB Tự Nhiên': info['diemTBTuNhien'],
                'Lịch Sử': info['lichSu'],
                'Địa Lý': info['diaLy'],
                'GDCD': info['gdcd'],
                'DiemTB Xã Hội': info['diemTBXaHoi']
            }
            data.append(diem)  # Thêm dữ liệu vào danh sách

        else:
            print(f"Request failed for ID {x}: {response.status_code}")

        # 
        time.sleep(1)  

    except Exception as e:
        print(f"Error occurred for ID {x}: {e}")

# Chuyển đổi dữ liệu thành DataFrame của pandas
df = pd.DataFrame(data)

# Ghi dữ liệu vào file Excel
df.to_excel('diem_thi.xlsx', index=False)

print("Data saved to diem_thi.xlsx")
