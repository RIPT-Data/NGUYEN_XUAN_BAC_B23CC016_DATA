# Thực hiện lấy dữ liệu từ một trang web dantri.com để lấy điểm thi THPT 2024 của 100 thí sinh tỉnh Nam Định bằng ngôn ngư python
## Bước 1: Import các thư viện cần thiết
* Sử dụng requests để gửi yêu cầu HTTP và lấy dữ liệu.
* Sử dụng time để quản lý thời gian nghỉ giữa các lần yêu cầu.
* Sử dụng pandas để xử lý dữ liệu và lưu dữ liệu thành file Excel.
```python
import requests  # Thư viện gửi yêu cầu HTTP
import time  # Thư viện quản lý thời gian nghỉ
import pandas as pd  # Thư viện xử lý dữ liệu dạng bảng và ghi file Excel

```
## Bước 2: Khởi tạo danh sách lưu dữ liệu
* Tạo một danh sách rỗng có tên data để lưu các dữ liệu thu thập được từ quá trình web scraping.
```python
data = []  # Khởi tạo danh sách để lưu dữ liệu
```
## Bước 3: Vòng lặp để gửi yêu cầu và thu thập dữ liệu
* Tạo một vòng lặp for để gửi yêu cầu đến URL với các ID là SBD từ **25000001** đến **25000100**.
* Tạo URL bằng cách nối ID vào phần đuôi của URL cơ bản.
* Gửi yêu cầu GET đến URL với requests.request.
``` python
for x in range(25000001, 25000100):
    scraping_url = "https://dantri.com.vn/thpt/1/0/99/" + str(x) + "/2024/0.2/search-gradle.htm"
    payload = {}
    headers = {}
```
## Bước 4: Xử lý phản hồi và lấy dữ liệu
* Kiểm tra mã trạng thái phản hồi (HTTP status code).
* Nếu phản hồi thành công (status code 200), phân tích phản hồi JSON và lấy thông tin về điểm thi của học sinh.
* Tạo một từ điển chứa các thông tin về điểm thi và thêm vào danh sách data.
```python

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
```
## Bước 5: Quản lý lỗi và nghỉ giữa các lần yêu cầu
* Nếu có lỗi xảy ra trong quá trình gửi yêu cầu hoặc xử lý dữ liệu, in ra thông báo lỗi.
* Đặt thời gian nghỉ giữa mỗi yêu cầu để tránh quá tải server.
```python

        else:
            print(f"Request failed for ID {x}: {response.status_code}")
        time.sleep(1)  # Nghỉ 1 giây giữa các yêu cầu

    except Exception as e:
        print(f"Error occurred for ID {x}: {e}")
```
## Bước 6: Chuyển dữ liệu thành DataFrame và ghi ra file Excel
* Sau khi hoàn tất quá trình thu thập dữ liệu, chuyển danh sách data thành một DataFrame của pandas.
* Ghi dữ liệu vào file Excel với tên **diem_thi.xlsx.**
```python

df = pd.DataFrame(data)  # Chuyển danh sách thành DataFrame
df.to_excel('diem_thi.xlsx', index=False)  # Ghi dữ liệu vào file Excel
```
## Bước 7: In ra danh sách diêm
* In ra thông báo khi quá trình lưu file Excel hoàn tất.
```python

print("Data saved to diem_thi.xlsx")  

```
* Dữ liệu điểm thi của các học sinh sẽ được lưu vào file Excel **diem_thi.xlsx.**
