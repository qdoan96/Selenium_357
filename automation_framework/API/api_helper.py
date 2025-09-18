import requests

class APIHelper:
   def get_data(self, url, params=None):
       try:
           response = requests.get(url, params=params)
           response.raise_for_status()  # Ném lỗi nếu mã trạng thái là 4xx hoặc 5xx
           return response.json()
       except requests.exceptions.RequestException as e:
           print(f"Lỗi khi thực hiện yêu cầu GET: {e}")
           return None
           
   def post_data(self, url, data=None):
       try:
           response = requests.post(url, json=data)
           response.raise_for_status()
           return response.json()
       except requests.exceptions.RequestException as e:
           print(f"Lỗi khi thực hiện yêu cầu POST: {e}")
           return None